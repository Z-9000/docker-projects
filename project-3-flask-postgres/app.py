from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppass"),
    )

def init_db():
    """Retries connecting since Postgres may still be starting up when Flask boots."""
    for attempt in range(10):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    visited_at TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully.")
            return
        except psycopg2.OperationalError as e:
            print(f"DB not ready yet (attempt {attempt+1}/10): {e}")
            time.sleep(2)
    raise Exception("Could not connect to database after multiple retries.")

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id, visited_at;")
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"visit_id": row[0], "visited_at": str(row[1])})

@app.route("/visits")
def visits():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, visited_at FROM visits ORDER BY id DESC LIMIT 10;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "visited_at": str(r[1])} for r in rows])

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)