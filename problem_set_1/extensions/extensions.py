"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
"""

#While this can be done using conditionals, it will take a lot of time so I am going to use a dictionary

extensions = {
    "txt": "text/plain",
    "zip": "application/zip",
    "gif": "image/gif",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
}

default_extension = "application/octet-stream"

file_name = input("File name:").strip().lower()
ext_start = file_name.rfind(".")
if ext_start == -1:
    file_type = default_extension
else:
    file_extension = file_name[ext_start + 1:]
    file_type = extensions.get(file_extension, default_extension)
print(file_type)
