import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load .env variables
load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL")
)

prompt = PromptTemplate.from_template("""
Analyze this legacy code.

Return:
- Summary
- Risks
- Anti-patterns
- Complexity

Code:
{code}
""")

def analyze_with_agent(code):

    formatted_prompt = prompt.format(code=code)

    response = llm.invoke(formatted_prompt)

    content = str(response.content)

    patterns = []

    if "SQL injection" in content:
        patterns.append("SQL_INJECTION")

    if "password" in content:
        patterns.append("HARDCODED_CREDENTIALS")

    if "input validation" in content:
        patterns.append("NO_INPUT_VALIDATION")

    return {
        "summary": content,
        "identified_patterns": patterns,
        "complexity_score": 5,
        "language_detected": "SQL"
    }