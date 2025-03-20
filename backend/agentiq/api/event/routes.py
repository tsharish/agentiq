from fastapi import Depends, APIRouter

from agentiq.api.security import get_current_user
from .service import get_events_by_date
from .models import Event

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/", response_model=list[Event])
async def list_events_by_date(date: str, user: str = Depends(get_current_user)):
    """Returns all events in a given date"""
    return get_events_by_date(date)
