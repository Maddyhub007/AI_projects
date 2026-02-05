from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.sentiment import analyze_sentiment
from backend.summarizer import generate_article, summarize_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    text: str

class ArticleRequest(BaseModel):
    topic: str

class SummarizeRequest(BaseModel):
    text: str
    word_limit: int


@app.post("/sentiment")
def sentiment_api(req: SentimentRequest):
    return {"sentiment": analyze_sentiment(req.text)}


@app.post("/article")
def article_api(req: ArticleRequest):
    return {"article": generate_article(req.topic)}


@app.post("/summarize")
def summarize_api(req: SummarizeRequest):
    return {"summary": summarize_text(req.text, req.word_limit)}
