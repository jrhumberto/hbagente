from crewai import Crew, Process
from startup data_reporter.agents import startup_researcher, startup_verifier
from startup_data_reporter.tasks import gather_startup_data, generate_html_report

crew = Crew(
     agents=[startup_regearcher, startup_verifier],
     tasks=[gather_startup_data, generate_html_report],
     process=Process.sequential
)
