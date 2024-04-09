import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
def load_prompt_from_file(file_path):
    """
    Load the prompt from a text file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_prompt_to_gpt4(prompt):
    """
    Send the prepared prompt to the OpenAI GPT-4 API and return the generated text.
    """
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt}
                ]
            }
        ],
            max_tokens=1200,
        )

    content = response.choices[0].message.content
    return content

def save_generated_text(generated_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(generated_text)

def main():
    prompt = load_prompt_from_file("prepared_prompt.txt")
    generated_text = send_prompt_to_gpt4(prompt)
    save_generated_text(generated_text, "GENERATED_README.md")
    print("Generated README/Documentation has been saved to GENERATED_README.md")

if __name__ == "__main__":
    main()
