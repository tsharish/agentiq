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
            session_id = self.session_id
            self.memory[session_id] = [{"role": "user", "content": message}]
        elif session_id not in self.memory:
            raise ValueError(f"Session ID {session_id} does not exist.")
        else:
            self.memory[session_id].append({"role": "user", "content": message})

        response = generate(messages=self.memory[session_id], tools=self.tools)

        max_iterations = 10  # Safety check to prevent infinite loops
        while response.finish_reason != "COMPLETE" and max_iterations > 0:
            max_iterations -= 1

            if response.finish_reason == "TOOL_CALL":
                yield json.dumps({"session_id": session_id, "content": response.message.tool_plan})
                # Assuming only one tool call per response
                tool_call = response.message.tool_calls[0]
                tool = self.tool_map[tool_call.function.name]
                if not tool:
                    raise ValueError(f"Tool {tool_call.function.name} not found.")

                try:
                    tool_inputs = json.loads(tool_call.function.arguments)
                    tool_output = tool.run(**tool_inputs)
                except Exception as e:
                    tool_output = f"Tool execution error: {str(e)}"

                self.memory[session_id].extend(
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
                response = generate(messages=self.memory[session_id], tools=self.tools)

        self.memory[session_id].append(
            {"role": "assistant", "content": response.message.content[0].text}
        )

        yield json.dumps({"session_id": session_id, "content": response.message.content[0].text})
