import openai
from app.config import OPENAI_API_KEY
from app.services.prompt_templates import DOC_REVIEW_PROMPT

openai.api_key = OPENAI_API_KEY

def analyze_document(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": DOC_REVIEW_PROMPT + text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

