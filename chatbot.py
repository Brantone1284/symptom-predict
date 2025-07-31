import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("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")  # Set this in your .env file

def general_query_assistant(query):
    """
    Function to handle any kind of query using OpenAI's Chat API.
    Args:
        query (str): User's question or instruction.
    Returns:
        str: Response from the model.
    """
    system_prompt = (
        "You are a helpful, intelligent assistant that can answer any kind of question clearly and accurately. "
        "You can help with general knowledge, science, technology, history, math, writing, and more. "
        "Always aim to be helpful, honest, and safe."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            max_tokens=700,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error processing query: {str(e)}"

def main():
    print("🤖 General Assistant Chatbot (Type 'exit' to quit)")
    
    while True:
        query = input("\nYou: ")
        if query.lower() == 'exit':
            print("👋 Goodbye!")
            break

        response = general_query_assistant(query)
        print("\nAI: " + response)

if __name__ == "__main__":
    main()
