import os
import sys
from dotenv import load_dotenv 
from google import genai
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', help="The user Prompt")
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = sys.argv[1]
    if args.verbose:
        print("Working on:", user_prompt)

    messages = [
        genai.types.Content(role="User", parts=[genai.types.Part(text=args.prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if args.verbose:
        print("User prompt:", sys.argv[1])
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
