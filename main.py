from fastapi import FastAPI

app = FastAPI(title="AI Summarization and Sentiment Analysis")

@app.get("/")
def home():
    return {"msg": "Welcome back. This tool can summarize your texts and give a sentiment analysis."}