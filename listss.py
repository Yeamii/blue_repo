import os

# Get the current working directory
current_dir = os.getcwd()

# List files in the directory
file_list = os.listdir(current_dir)

# Create a list of dictionaries representing each file
file_info_list = []
for file_name in file_list:
    file_path = os.path.join(current_dir, file_name)
    file_info = {
        'name': file_name,
        'path': file_path,
        'size': os.path.getsize(file_path),
        'modified': os.path.getmtime(file_path)
    }
    file_info_list.append(file_info)

# Print the list of file dictionaries
for file_info in file_info_list:
    print(file_info)