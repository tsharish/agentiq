from pydantic import BaseModel


class Customer(BaseModel):
    id: int
    name: str
    city: str | None = None
    state: str | None = None
    country: str | None = None
