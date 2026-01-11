from fastapi import FastAPI
from app.routes.review import router as review_router

app = FastAPI(title="DocGuard AI V1")

app.include_router(review_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "DocGuard AI is running"}

