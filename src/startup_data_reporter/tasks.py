from crewai import Task
from startup_data_reporter.agents import startup_researcher, startup_verifier

gather_startup_data = Task(
    description=(
        "You are an AI researcher gathering public data about a startup named '{startup_name}' in '{country}'.\n\n"
        "Return your findings as ** structured plain text ** , including:\n"
        "- Name\n"
        "- Brief Description (1-2 sentences on what the startup does)\n"
        "- Founding Date\n"
        "- Founders with LinkedIn URLs (if found)\n"
        "- Total Funding (USD)\n"
        "- Number of Employees\n"
        "- Headquarters Location\n"
        "- Sources section grouped by field (with URLs)\n\n"
        "Be clear and structured, for example:\n"
        "Name: ExampleAI\n"
        "Description: ExampleAI builds privacy-focused AI chips for autonomous vehicles.\n"
        "Founding Date: 2021\n"
        "Founders: \n"
        "- Jane Doe (https://linkedin.com/in/janedoe)\n"
        "Funding (USD): $50M\n"
        "Employees: 120\n"
        "Headquarters: Berlin, Germany\n\n"
        "Sources: \n"
        "Description:\n"
        "- https://example.com/article1\n"
        "Founding Date: \n"
        "- https://example.com/article2"
    ),
    expected_output="Structured plain text with all fields and a 'Sources' section, clearly labeled.",
    agent=startup_researcher
)

generate_html_report = Task(
    description=(
        "You are a startup intelligence analyst receiving structured text describing a startup. \n\n"
        "Parse the text and generate a clean Markdown report with the following sections:\n\n"
        "## Startup Overview\n"
        "- Name\n"
        "- Description\n"
        "- Founding Date\n"
        "- Funding\n"
        "- Employees\n"
        "- Headquarters\n\n"
        "## Founders\n"
        "List each founder and their LinkedIn URL if available. \n\n"
        "## Sources\n"
        "Group source links by field name. Use proper Markdown formatting for headings and links. \n\n"
        "Only return the final Markdown. No explanations."
    ),
    expected_output="A professional Markdown report of the startup.",
    agent=startup_verifier
)
