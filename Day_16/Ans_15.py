#Delete a file programmatically.
import os
file_path ="del.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("file removed successfully.")
else:
    print("file not found")
    