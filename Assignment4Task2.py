# Step 1: Take user input and write to a file
try:
    user_input = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
    print("Data successfully written to output.txt.")

    # Step 2: Take more input and append it
    additional_input = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(additional_input + "\n")
    print("Data successfully appended.")

    # Step 3: Read and display final content
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())

except Exception as e:
    print(f"An error occurred: {e}")
