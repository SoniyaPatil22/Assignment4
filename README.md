# Assignment4
######################   Task 1   ############################
**File Name:** Assignment4Task1FileDoesn'tExist.py
**File Reader with Error Handling**
This Python script reads the contents of a file named sample.txt and prints each line to the console. It includes robust error handling to gracefully manage potential issues such as:

**File Not Found:** If the file sample.txt does not exist, it displays an appropriate error message.

Other Exceptions: Catches and displays any other unexpected errors during the file reading process.

Features
Uses a with statement to handle file operations safely.

Strips newline characters for cleaner output.

Implements exception handling using try-except blocks.

Example Output (if sample.txt doesn't exists):
Error: The file 'sample.txt' does not exist.
****************************************************************************************************
Read and Display File Contents Line by Line **(If File Exists)**
This Python script reads and prints the contents of a file named demoFile.txt line by line, including line numbers for clarity.

**Functionality:**
Opens the file demoFile.txt in read ("r") mode.

Iterates through each line of the file using a for loop.

Prints each line with its corresponding line number.

Uses strip() to remove leading and trailing whitespace from each line before printing.

The code uses a try-except block to gracefully handle errors, but in this version, it only focuses on the case where the file exists.

 Example Output (if demoFile.txt exists):
 Reading file content:
Line 1: This is sample text file.
Line 2: It contains multiple line.

######################   Task 2   ############################
