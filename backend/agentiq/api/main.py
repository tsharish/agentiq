from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from agentiq.settings import ORIGIN
from agentiq.api.security import authenticate_user, create_access_token
from agentiq.api.chat.routes import router as chat_router
from agentiq.api.customer.routes import router as customer_router
from agentiq.api.opportunity.routes import router as opportunity_router
from agentiq.api.event.routes import router as event_router

app = FastAPI()

origins = [ORIGIN]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(customer_router)
app.include_router(opportunity_router)
app.include_router(event_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Agentiq"}


@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = form_data.username
    password = form_data.password
    authenticated = authenticate_user(username, password)

    if not authenticated:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
