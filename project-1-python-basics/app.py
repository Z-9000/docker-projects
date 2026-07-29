import time

def main():
    print("Hello from inside a Docker container!")
    print("Counting sheep to prove I'm alive...")
    for i in range(1, 6):
        print(f"Sheep #{i} 🐑")
        time.sleep(1)
    print("Done counting. Bye!")

if __name__ == "__main__":
    main()