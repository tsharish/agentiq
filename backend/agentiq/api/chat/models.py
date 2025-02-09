from pydantic import BaseModel


class Message(BaseModel):
    content: str
    session_id: int | None = None
