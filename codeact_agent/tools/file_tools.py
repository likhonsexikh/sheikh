import os

def create_file(filename: str, content: str) -> str:
    """
    Creates a file with the given filename and content.
    This is a self-contained tool and has no external dependencies
    beyond the standard library.

    :param filename: The name of the file to create.
    :param content: The content to write to the file.
    :return: A message indicating success or failure.
    """
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"File '{filename}' created successfully."
    except Exception as e:
        return f"Error creating file: {e}"
