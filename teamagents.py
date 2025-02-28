from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

web_agents = Agent(
    name = 'Web Agents',
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True
)

finance_agents = Agent(
    name = 'finance Agent',
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, company_info = True)],
    instructions = ['use tables to represent'],
    show_tools_calls = True,
    markdown = True
)

agent_team = Agent(
    team = [web_agents, finance_agents],
    model = Groq(id = "llama-3.3-70b-versatile"),
    instructions = ['Always include sources', 'use tables to represent'],
    show_tools_calls = True,
    markdown = True
)

agent_team.print_response("summarize latest news from analyst recommendations and share latest news of HDFC Bank", stream = True)

