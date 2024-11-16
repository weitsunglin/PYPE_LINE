import os

def run():
    directory = "F:\_project"
    print(f"Listing files in directory: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))
