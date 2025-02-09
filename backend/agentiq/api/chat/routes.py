from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from agentiq.core.agent import Agent
from agentiq.core.tool import Tool
from agentiq.api.security import get_current_user
from agentiq.api.customer.service import get_customer_by_name, create_customer

from .models import Message

router = APIRouter(prefix="/chat", tags=["chat"])
agent = Agent(tools=[Tool(create_customer), Tool(get_customer_by_name)])


@router.post("/")
async def chat(message: Message, user: str = Depends(get_current_user)):
    """Chat endpoint that processes user messages through the AI agent."""
    try:
        return StreamingResponse(
            agent.run(message=message.content, session_id=message.session_id),
            media_type="application/json",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
