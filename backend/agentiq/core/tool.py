from typing import Callable


class Tool:
    def __init__(self, tool_function: Callable) -> None:
        self.tool_function = tool_function

    @property
    def name(self):
        return self.tool_function.__name__

    def run(self, **kwargs):
        return self.tool_function(**kwargs)
