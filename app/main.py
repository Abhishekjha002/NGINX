from fastapi import FastAPI
import socket

app = FastAPI()
hostname = socket.gethostname()

@app.get("/")
async def root():
    return {
        "message": "Hello from " + hostname
    }
