from pydantic import BaseModel

class ReviewResponse(BaseModel):
    summary: str
    risks: str
    missing_clauses: str

