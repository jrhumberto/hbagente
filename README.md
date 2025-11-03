# hbagente


## Links importantes
1. https://build.nvidia.com/nvidia/llama-3_3-nemotron-super-49b-v1_5
2. https://build.nvidia.com/nvidia/llama-3_3-nemotron-super-49b-v1_5/deploy
3. https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html
4. https://build.nvidia.com/nvidia/aiq/nim
5. https://developers.nvidia.com/
6. https://nvidia.com/on-demand/
7. https://youtube.com/@NVIDIALatinAmerica
8. https://github.com/NVIDIA-AI-Blueprints/aiq-research-assistant
9. https://docs.crewai.com/
10. https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant

## Comando

### Executar agente
````sh
PYTHONPATH=src python src/startup_data_reporter/main.py --startup_name="Neospace" --country="Brazil" 
````

### Criar agente crewai
````
crewai create crew demo
# Criará agents.yml, tasks.yml, crew.py e main.py
````

### PAsso a passo
````
1. uv init my-crew-project
2. cd my-crew-project
3. uv add crewai[tools]
````

### Arquivos crew
````
# agent.py
from crewai import Agent
assistant = Agent(
    role="Data Analyzer",
    goal="Extract insights from datasets",
    backstory="Expert in Python and stats",
    tools=[],
    llm=llm
)

# tasks.py
from crewai import Task
task = Task(
    description="Analyze Q4 sales data",
    agent=assistant,
    expected_output="Summary with trends"
)

# crew.py
from crewai import Crew
crew = Crew(
    agents=[assistant],
    tasks=[task],
    verbose=True
)
result = crew.kicloff()
print(result)
````



## …or create a new repository on the command line
````
echo "# hbagente" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jrhumberto/hbagente.git
git push -u origin main
````
## …or push an existing repository from the command line
````
git remote add origin https://github.com/jrhumberto/hbagente.git
git branch -M main
git push -u origin main
````
