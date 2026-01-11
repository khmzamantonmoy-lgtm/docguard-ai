import openai
import json
from app.config import OPENAI_API_KEY
from app.services.prompt_templates import DOC_REVIEW_PROMPT

openai.api_key = OPENAI_API_KEY

def analyze_document(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a legal document reviewer. Return valid JSON only."
            },
            {
                "role": "user",
                "content": DOC_REVIEW_PROMPT + text + """
                
Return JSON exactly in this format:
{
  "summary": "",
  "risks": "",
  "missing_clauses": ""
}
"""
            }
        ],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)
