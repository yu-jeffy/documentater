import json

def load_file_content(file_path):
    """
    Load the content of a file into a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def prepare_prompt(file_structure_path, all_text_content_path):
    """
    Prepare the prompt for the GPT-4 API by combining the file structure and all text content.
    """
    file_structure = load_file_content(file_structure_path)
    all_text_content = load_file_content(all_text_content_path)

    prompt = f"Given the following file structure:\n{file_structure}\n\n" \
             f"and the content of the files:\n{all_text_content}\n\n" \
             "Generate a comprehensive README/documentation for the project."
    
    return prompt

def main():
    prompt = prepare_prompt("file_structure.txt", "all_text_content.txt")
    
    # For demonstration, we'll just print the prompt to the console.
    # In a real application, this would be sent to the GPT-4 API.
    print(prompt)

if __name__ == "__main__":
    main()
