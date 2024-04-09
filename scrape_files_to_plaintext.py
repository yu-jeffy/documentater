import os
import argparse

def is_binary(filename):
    """
    Check if a file is binary. This is a simple heuristic based on the presence of null bytes.
    """
    try:
        with open(filename, 'rb') as file:
            for chunk in file.read(1024):
                if b'\0' in chunk:
                    return True
        return False
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return True

def scrape_directory_to_plaintext(directory):
    """
    Recursively scrape the directory, converting files to plaintext and generating a file structure.
    """
    file_structure = []
    all_text_content = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            if not is_binary(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_content:
                        text = file_content.read()
                        all_text_content.append(f"File: {relative_path}\n{text}\n")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
            file_structure.append(relative_path)

    return "\n".join(file_structure), "\n".join(all_text_content)

def main():
    parser = argparse.ArgumentParser(description="Scrape files into plaintext and generate file structure.")
    parser.add_argument("directory", type=str, help="Directory to scrape")
    args = parser.parse_args()

    file_structure, all_text_content = scrape_directory_to_plaintext(args.directory)
    with open("file_structure.txt", "w", encoding="utf-8") as fs_file:
        fs_file.write(file_structure)
    with open("all_text_content.txt", "w", encoding="utf-8") as atc_file:
        atc_file.write(all_text_content)

    print("Scraping complete. File structure and content saved.")

if __name__ == "__main__":
    main()
