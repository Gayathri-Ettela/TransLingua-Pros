from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def translate_text(text, source_language, target_language):
    try:
        prompt = f"""
You are an expert multilingual translator.

If source language is 'Auto', detect it automatically.

Translate the following text from {source_language} to {target_language}.
Preserve meaning, tone, grammar, and formatting.
Return ONLY the translated text.

Text:
{text}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error during translation: {e}"
