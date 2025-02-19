from enum import Enum
from pydantic import BaseModel, NonNegativeFloat


class Stage(str, Enum):
    open = "Open"
    closed_won = "Closed Won"
    closed_lost = "Closed Lost"


class Opportunity(BaseModel):
    id: int
    name: str
    customer_id: int
    customer_name: str
    amount: NonNegativeFloat
    stage: Stage = Stage.open
