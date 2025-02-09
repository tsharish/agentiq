from fastapi import Depends, APIRouter

from agentiq.api.security import get_current_user
from .models import Customer
from .data import customers

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get("/", response_model=list[Customer])
async def get_customers(user: str = Depends(get_current_user)):
    """Returns all customers"""
    return customers
