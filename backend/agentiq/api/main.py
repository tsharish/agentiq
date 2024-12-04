from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agentiq.settings import ORIGIN

app = FastAPI()

origins = [ORIGIN]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Agentiq"}
