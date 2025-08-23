from fastapi import FastAPI

app = FastAPI(title="Real-Time Docs")

@app.get("/")
def root():
    return {"message": "Welcome to Real-Time Docs API"}
