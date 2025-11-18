# hbagente

## Estrutura
* src/startup_data_reporter e src/article_summarizer são projetos baseados em palestra no SERPRO
* src/project -> retirado do pasta project de [11] e [12] - Ver também [13]
* src/my_mcp -> retirado do pasta my_mcp de [11] e [12] - Ver também [13]
* src/leann_with_ollama -> retirado do video [16]
* src/demo_leann -> retirada da documentação oficial [17] - Ver tambén video [18]
* src/docstoteles -> retirado de [20] - Ver também video [21]


## Referências
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
11. https://github.com/caio-moliveira/mcp-agents/tree/main
12. Video **Criando seu Agente AI com Python, CrewAI e FastMCP**: https://youtu.be/Lviw0siXbL4
13. Video **Agentes de IA com MCP: Integração prática com CrewAI**: https://youtu.be/-tf_egWmCsM
14. LEANN - https://github.com/yichuan-w/LEANN
15. CLI Agentes - https://github.com/moazbuilds/CodeMachine-CLI
16. Video **Leaan with Ollama**: https://www.youtube.com/watch?v=7XqcuxrR4uM
17. Demo com Leann: https://github.com/yichuan-w/LEANN/blob/main/demo.ipynb
18. Video **Smallest RAG Vector DB** - LEANN - https://www.youtube.com/watch?v=WzWqQp2WegY
19. Video **Transforme qualquer site em uma API com esta IA (Scraping de Dados com Firecrawl)**: https://youtu.be/gIT2bTTso0E
20. Docstoteles - TRANSFORMEI qualquer documentação em um assistente de IA  (Web Scraping + RAG)  - GROK, Firecrawl: https://github.com/asimov-academy/video-docstoteles-material
21. Video **TRANSFORMEI qualquer documentação em um assistente de IA  (Web Scraping + RAG)**: https://youtu.be/emcxlgN8sQ0 
22. LLm Data Scrapers: [github.com/patrickloebel/llm-data-scrapers](https://github.com/patrickloebel/llm-data-scrapers)
23. Grafico de redes: https://github.com/deepgraph/deepgraph
24. RAG - https://elisaterumi.substack.com/p/como-construir-seu-proprio-rag-local
25. Awesome Data Centric - https://github.com/Renumics/awesome-open-data-centric-ai
26. Code to UML: https://github.com/WiseCat-Git/code-to-uml-generator/
27. Video **Jina Reader API: Build better AI Agents and RAG systems with Reader**: https://www.youtube.com/watch?v=GllAqZE6uws


## LLM Data Scrapers 🚀

A list of useful Open Source tools, LLM txt  and scrapers to gather data for LLMs:

| Name |  |
| :------| :------------|
| [gitingest](https://github.com/cyclotruc/gitingest) | Replace `hub` with `ingest` in any github url to get a prompt-friendly extract of a codebase |
| [gitforme.tech](https://gitforme.tech) | For any github url to get llm txt - https://github.com/herin7/gitforme |
| [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | And a online llm txt: https://llmstxt.firecrawl.dev/ or in repository: https://github.com/firecrawl/create-llmstxt-py |
| [deepgraph.co](https://deepgraph.co) | Transforma qualquer github em um chat e gráfico de redes como `https://deepgraph.co/<user>/<repo>`   Exemplo: https://deepgraph.co/deepgraph/deepgraph [23]  |
| [repomix](https://github.com/yamadashy/repomix) |  Packs your entire repository into a single, AI-friendly file | 
| [llm-scraper](https://github.com/mishushakov/llm-scraper) | Turn any webpage into structured data using LLMs | 
| [crawl4ai](https://github.com/unclecode/crawl4ai) |  LLM friendly web crawler & scraper | 
| [trafilatura](https://github.com/adbar/trafilatura) |  Python & Command-line tool to gather text and metadata on the web | 
| [RepoToTextForLLMs](https://github.com/Doriandarko/RepoToTextForLLMs) |  Simple Python script to fetch repo content | 
| [marker](https://github.com/VikParuchuri/marker) |  Convert PDF to markdown or JSON quickly | 
| [reader](https://github.com/jina-ai/reader) | Convert any URL to an LLM-friendly input with a simple prefix `https://r.jina.ai/<SITE>`   Exemplo: https://r.jina.ai/https://elisaterumi.substack.com/p/como-construir-seu-proprio-rag-local [24] | 
| [files-to-prompt](https://github.com/simonw/files-to-prompt) | Concatenate a directory full of files into a single prompt for use with LLMs | 
| [docling](https://github.com/DS4SD/docling) | Simplifies document processing and parsing of diverse formats | 
| [firecrawl](https://github.com/mendableai/firecrawl) |  API to turn websites into LLM-ready markdown or structured data, can be self-hosted (with limitations) | 
| [llmstxt-generator](https://github.com/mendableai/llmstxt-generator) | API to generate `llms.txt`files  from websites for LLM training and inference | 
| [llm-datasets](https://github.com/mlabonne/llm-datasets) | Curated list of datasets and tools specifically for post-training [22] |
| [llm-datasets](https://github.com/mlabonne/llm-datasets) | Curated list of datasets and tools specifically for post-training [22] |




    
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
