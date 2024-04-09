import os

def write_readme(readme_content, directory):
    """
    Write the README content to a README.md file in the specified directory.
    """
    readme_path = os.path.join(directory, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)
    print(f"README.md has been saved to {directory}")
