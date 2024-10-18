import openai 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("api-key")

def generate_story_prompt(genre, theme, character_type):
    # Create a prompt for generating a story idea
    prompt = f"Generate a creative writing prompt for a {genre} story with the theme '{theme}' and a character type of '{character_type}'."
    
    # Call the OpenAI API with the generated prompt
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7  # Controls creativity (higher = more creative)
        )
        return response.choices[0].text.strip()
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the Story Idea Generator!")

    while True:
        # Ask the user for inputs to craft the prompt
        genre = input("Enter a genre for your story (e.g., fantasy, sci-fi, mystery): ")
        theme = input("Enter a theme for your story (e.g., friendship, revenge, courage): ")
        character_type = input("Enter a character type (e.g., detective, wizard, alien): ")

        # Generate and display the story prompt
        story_prompt = generate_story_prompt(genre, theme, character_type)
        print("\nGenerated Story Idea:")
        print(story_prompt)

        # Ask if the user wants to generate another idea
        more = input("\nWould you like to generate another story idea? (yes/no): ").lower()
        if more != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
