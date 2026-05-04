import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

MODEL = os.getenv("MODEL")

def analyze_code(code):

    prompt = f"""
    Analyze this legacy code.

    Return ONLY valid JSON.

    {{
      "summary": "",
      "identified_patterns": [],
      "complexity_score": 1,
      "language_detected": ""
    }}

    Code:
    {code}
    """

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

        print("RAW LLM RESPONSE:")
        print(content)

        # Remove markdown formatting
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        # Extract only JSON portion
        start = content.find("{")
        end = content.rfind("}") + 1

        json_content = content[start:end]

        return json.loads(json_content)

    except Exception as e:

        return {
            "summary": f"LLM analysis failed: {str(e)}",
            "identified_patterns": [],
            "complexity_score": 5,
            "language_detected": "UNKNOWN"
        }

def generate_modern_code(code, target_framework="FastAPI"):

    prompt = f"""
    Convert this legacy code into modern {target_framework} code.

    STRICT RULES:
    - Add inline comments explaining improvements
    - Add proper exception handling
    - Remove hardcoded credentials
    - Use modern best practices
    - Return ONLY code
    - No markdown
    - No explanation

    Legacy Code:
    {code}
    """

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:

        return f"Modernization failed: {str(e)}"   
