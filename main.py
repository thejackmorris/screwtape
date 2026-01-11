import os
from dotenv import load_dotenv

from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    print("Hello from screwtape!")
    if api_key == None:
        raise RuntimeError("no key")
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model='gemini-2.5-flash', contents='testing, give a one sentence confirmation the connection works.')
    print(response.text)

if __name__ == "__main__":
    main()
