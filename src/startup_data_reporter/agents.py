from crewai import Agent
from startup_data_reporter.tools.search_tool import search_tool
from startup_data_reporter.llm import get_nvidia_llm

llm = get_nvidia_llm()

startup_researcher = Agent(
    role='Startup Intelligence Researcher',
    goal='Discover startup info using reliable online sources',
    backstory='Expert researcher in startup analytics.',
    tools=[search_tool],
    verbose=True,
    memory=True,
    llm=llm
)

startup_verifier = Agent(
    role='Startup Data Verifier and Reporter',
    goal='Verify data and generate reports',
    backstory='Meticulous verifier of startup intelligence.',
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)  
