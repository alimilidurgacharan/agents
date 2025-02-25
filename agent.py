from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.run.response import RunEvent, RunResponse

agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [ArxivToolkit()],
    desrption = "You are a researcher writing an article on a topic",
    instruction = [
    "For a given topic, search given top five papers",
    "Then read each paper and extract the article text",
    "Analyze and prepare 5-7 bullet points based on the information.",
    ],
    markdown = True,
    show_tool_calls = True
)

def as_stream(response):
    for chunk in response:
        if isinstance(chunk, RunResponse) and isinstance(chunk.content, str):
            if chunk.event == RunEvent.run_response:
                yield chunk.content
