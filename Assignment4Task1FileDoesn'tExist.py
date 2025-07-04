try:
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  # Removes newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

