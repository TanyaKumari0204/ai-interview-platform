from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
app = FastAPI(title="AI Interview Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Interview Platform API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

Base.metadata.create_all(bind=engine)