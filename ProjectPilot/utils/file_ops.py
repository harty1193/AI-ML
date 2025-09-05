

def create_text_file(file_path, content):
    import pandas as pd
    with open(file=file_path, mode='w') as file:
        file.write(content)
    print("Created and written to the file successfully.")


def add_content_to_file(file_path, content):
    with open(file=file_path, mode='a') as file:
        file.write(content)
    print("Content added successfully.")


if __name__ == "__main__":
    create_text_file("data\sample1.txt", "Hello, World! This is a sample text file.")
    add_content_to_file("data\sample.txt", "\nThis is an additional line.")
