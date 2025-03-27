# Use with statement to handle file exceptions.
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file("data.txt")
read_file("missing_file.txt")
