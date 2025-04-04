from fastapi import Depends, APIRouter

from agentiq.api.security import get_current_user
from agentiq.api.customer.data import customers
from .models import Opportunity
from .data import opportunities

router = APIRouter(prefix="/opportunities", tags=["opportunities"])


@router.get("/", response_model=list[Opportunity])
async def get_opportunities(user: str = Depends(get_current_user)):
    """Returns all opportunities"""
    for opportunity in opportunities:
        customer_name = next(
            (
                customer["name"]
                for customer in customers
                if customer["id"] == opportunity["customer_id"]
            ),
            None,
        )
        opportunity["customer_name"] = customer_name
    return opportunities
