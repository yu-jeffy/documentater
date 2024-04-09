import argparse
from scrape_files_to_plaintext import scrape_directory_to_plaintext
from prepare_prompt_for_gpt4 import prepare_prompt
from send_prompt_to_gpt4 import send_prompt_to_gpt4
from write_readme import write_readme

def main(directory):
    # Step 1: Scrape the directory to plaintext and generate file structure
    file_structure, all_text_content = scrape_directory_to_plaintext(directory)
    
    # Step 2: Prepare the prompt for GPT-4 directly with the content
    prompt = prepare_prompt(file_structure, all_text_content)  # Use the content directly
    
    # Step 3: Send the prompt to GPT-4 and get the generated README/documentation
    generated_text = send_prompt_to_gpt4(prompt)
    
    # Step 4: Write the generated README/documentation to a file in the specified directory
    write_readme(generated_text, directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate README/documentation for a project directory.")
    parser.add_argument("directory", type=str, help="Directory to process")
    args = parser.parse_args()
    
    main(args.directory)
