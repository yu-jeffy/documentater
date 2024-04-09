import os
import argparse
import fnmatch

def load_gitignore_patterns(directory):
    """
    Load and return patterns from .gitignore if it exists.
    """
    gitignore_path = os.path.join(directory, '.gitignore')
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            patterns = file.read().splitlines()
    return patterns

def should_skip(path, patterns, default_skip_list):
    """
    Determine if a file or directory should be skipped based on .gitignore patterns and default skip list.
    """
    for pattern in patterns + default_skip_list:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def scrape_directory_to_plaintext(directory):
    """
    Recursively scrape the directory, converting files to plaintext and generating a file structure.
    """
    gitignore_patterns = load_gitignore_patterns(directory)
    default_skip_list = ['README*', '.DS_Store', 'node_modules/*']
    file_structure = []
    all_text_content = []

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not should_skip(os.path.join(root, d), gitignore_patterns, default_skip_list)]
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            if not should_skip(file_path, gitignore_patterns, default_skip_list) and not is_binary(file_path):
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
    with open("file_structure.txt", "w", encoding='utf-8') as fs_file:
        fs_file.write(file_structure)
    with open("all_text_content.txt", "w", encoding='utf-8') as atc_file:
        atc_file.write(all_text_content)

    print("Scraping complete. File structure and content saved.")

if __name__ == "__main__":
    main()
