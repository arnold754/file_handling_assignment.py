def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Line 3: Hello World!\n")
        print("File 'my_file.txt' created successfully.")
    except FileNotFoundError:
        print("File not found or unable to create file.")
    except PermissionError:
        print("Permission denied to create file.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':\n", content)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read file.")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appended text.\n")
            file.write("67890\n")
            file.write("Line 6: Additional line.\n")
        print("Content appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to append file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("File operations completed. ")
if __name__ == "__main__":
    create_file()

    read_file()


    append_file()
