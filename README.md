# Documentater

## Overview

Documentater is a cutting-edge project focused on utilizing AI, specifically OpenAI's GPT-4, to generate comprehensive documentation for your entire codebase automatically. By analyzing your file structure and the content of your files, Documentater streamlines the documentation process, making it more efficient and less time-consuming. This innovative approach ensures that your project is accessible and well-understood by new contributors, team members, and stakeholders, fostering a collaborative and informed development environment.

## Features

- **Automatic README Generation**: Utilizes GPT-4's powerful natural language understanding capabilities to generate detailed README files based on your project's codebase and file structure.
- **Environment Configuration Support**: Comes with `.env` file support out of the box, ensuring that your project's environment variables are managed securely and effectively.
- **Extensible Python Scripts**: Includes Python scripts for preparing prompts, sending them to GPT-4, and saving the generated text. These scripts can be easily extended or customized to fit your project's specific needs.
- **Comprehensive Git Integration**: Fully integrates with Git, allowing for seamless usage within your current version control workflow. The project structure includes a `.gitignore` file to ensure proper handling of unnecessary files and directories.
- **License Management**: The project is licensed under the MIT License, providing flexibility for both commercial and personal use while ensuring that your work remains protected.

## How It Works

Documentater operates in four key steps:
1. **Scrape Project Directory**: Firstly, the `scrape_files_to_plaintext.py` script analyzes your project directory, converting all relevant files into plaintext while respecting `.gitignore` patterns to compile the information needed for documentation.
2. **Prepare GPT-4 Prompt**: The `prepare_prompt_for_gpt4.py` script then takes this plaintext representation of your codebase and prepares a prompt that is conducive to generating meaningful documentation, ensuring that all key aspects of your project are considered.
3. **Generate Documentation via GPT-4**: This prompt is sent to GPT-4 using `send_prompt_to_gpt4.py`, which handles the communication with OpenAI's API to generate a comprehensive readme or documentation based on the input provided.
4. **Save Generated Documentation**: Finally, the generated documentation is saved back into your project directory using `write_readme.py`, ready for review and deployment alongside your project.

## Installation and Usage

To use Documentater, you'll need Python 3.8 or later and an OpenAI API key. Follow these steps to get started:

1. **Clone the Repository**:
```
git clone https://github.com/yu-jeffy/documentater.git
```

2. **Install Dependencies**:
```
pip install -r requirements.txt
```

3. **Configure Environment Variables**:
Copy `.env.example` to `.env` and insert your OpenAI API key:
```
OPENAI_API_KEY="your_openai_api_key_here"
```

4. **Run Main Script**:
Navigate to the project directory and run:
```
python main.py <path_to_your_codebase_directory>
```

This will start the documentation generation process, and the generated README/documentation will be saved in the specified directory.

## Contribution

Contributions are welcome! Whether it's extending functionalities, improving the docs, or reporting issues, your input helps make Documentater better for everyone.

## License

Documentater is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Documentater exemplifies the potential of AI in streamlining and automating critical aspects of software development, such as documentation. By leveraging the capabilities of GPT-4, it ensures that documenting your project is no longer a tedious task, but a seamless part of your development workflow.