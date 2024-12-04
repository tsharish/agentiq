import json

from agentiq.core.llm import generate
from agentiq.core.tool import Tool


class Agent:
    def __init__(self, tools: list[Tool]) -> None:
        self.session_id = 0
        self.memory: dict[int, list[dict]] = {}
        self.tools = tools
        self.tool_map = {tool.name: tool for tool in self.tools}

    def run(self, message: str, session_id: int | None = None):
        if session_id is None:
            self.session_id += 1
            self.memory[self.session_id] = [{"role": "user", "content": message}]
        else:
            self.memory[self.session_id].append({"role": "user", "content": message})

        response = generate(messages=self.memory[self.session_id], tools=self.tools)

        while response.finish_reason != "COMPLETE":
            if response.finish_reason == "TOOL_CALL":
                yield response.message.tool_plan
                # Assuming only one tool call per response
                tool_call = response.message.tool_calls[0]
                tool = self.tool_map[tool_call.function.name]
                tool_inputs = json.loads(tool_call.function.arguments)
                tool_output = tool.run(**tool_inputs)
                self.memory[self.session_id].extend(
                    [
                        {
                            "role": "assistant",
                            "tool_calls": response.message.tool_calls,
                            "tool_plan": response.message.tool_plan,
                        },
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": [{"type": "text", "text": str(tool_output)}],
                        },
                    ]
                )
                response = generate(messages=self.memory[self.session_id], tools=self.tools)

        self.memory[self.session_id].append(
            {"role": "assistant", "content": response.message.content[0].text}
        )

        yield response.message.content[0].text
