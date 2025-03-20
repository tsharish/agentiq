from pydantic import BaseModel


class Event(BaseModel):
    name: str
    date: str
    start_time: str
    end_time: str
