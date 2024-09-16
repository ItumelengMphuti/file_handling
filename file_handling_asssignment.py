# File Creation and Writing
try:
    with open('my_file.txt', 'w') as file:
        # Writing three lines of text to the file
        file.write("Hello, this is the first line.\n")
        file.write("My name is Jane Doe.\n")
        file.write("The number 12345 is written here.\n")
    print("File created and text written successfully.")
except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        print("\nContents of 'my_file.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found: The file does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("New Line 1.\n")
        file.write("New Line 2\n")
        file.write("And a final line: 67890.\n")
    print("Text appended successfully.")
except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")


try:
    # Reading the final content after appending
    with open('my_file.txt', 'r') as file:
        print("\nFinal contents of 'my_file.txt' after appending:")
        final_content = file.read()
        print(final_content)
except FileNotFoundError:
    print("File not found: The file does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File operations complete.")
