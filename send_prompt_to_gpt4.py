import openai
import os

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
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the latest available version
        prompt=prompt,
        max_tokens=2048,  # Adjust based on your needs
        temperature=0.7,  # Adjust for creativity level
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

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
