from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key="YOUR_API_KEY")

@app.get("/")
def home():
    return {"message": "AI Agent Running 🚀"}

@app.get("/chat")
def chat(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return {"response": response.text}
