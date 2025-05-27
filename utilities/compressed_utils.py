import os
import zipfile

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(root)
    zip_file = os.path.join(root, r'Linear Regression\data\archive.zip')
    extract_directory = os.path.join(root, r'Linear Regression\data')
    extract_zip(zip_file, extract_directory)