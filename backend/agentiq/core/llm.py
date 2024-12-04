import cohere
from llm_easy_tools import get_tool_defs

from agentiq.logger import logger
from agentiq.core.tool import Tool
from agentiq.settings import API_KEY, MODEL


def generate(messages: list[dict], tools: list[Tool]):
    co = cohere.ClientV2(api_key=API_KEY)
    logger.info(messages)

    response = co.chat(
        model=MODEL, messages=messages, tools=get_tool_defs(tool.tool_function for tool in tools)
    )
    logger.info(response)
    return response
