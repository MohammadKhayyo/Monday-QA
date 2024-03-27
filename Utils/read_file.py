def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents
