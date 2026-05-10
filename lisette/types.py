from dataclasses import dataclass

class StopResponse(str): pass
class FullResponse(str): pass

@dataclass
class ToolResponse:
    content: list[str,str]

