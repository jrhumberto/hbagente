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
28. Video **How to Integrate BrowserAct with n8n in 60 Seconds | Web Scraping Automation TutorialN**: https://youtu.be/2CfEBOfpRcM
29. Video **Extraia Dados de QUALQUER SITE Usando IA - 100% Grátis e Sem Programar (BrowserAct)**: https://youtu.be/XW5SzyC1zWM
30. Chonkie: https://github.com/chonkie-inc/chonkie
31. Resumo ou Curriculo: https://rxresu.me/auth/login
32. Formulário: opnform.com
33. Embedding_1: https://huggingface.co/BAAI/bge-m3
34. Embedding_2: https://platform.openai.com/docs/guides/embeddings - text-embedding-3-small
35. Embedding_3: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
36. OpenNotebook (alternativa ao notebooklm): https://github.com/lfnovo/open-notebook/blob/main/docs/getting-started/installation.md

## OCR
1. **Chandra OCR in 9min**: https://www.youtube.com/watch?v=MSsYL8EpfDw
2. https://huggingface.co/datalab-to/chandra
3. **HunyuanOCR - Free OCR That Just Destroyed Every Commercial API - Run Locally**: https://www.youtube.com/watch?v=TOsLdlDwIZs
4. https://huggingface.co/tencent/HunyuanOCR
5. 

## DOCLING
<img width="703" height="597" alt="image" src="https://github.com/user-attachments/assets/e1e2d042-7c7e-4c1e-9b8e-d93e05fad16b" />


## LLM Data Scrapers 🚀

A list of useful Open Source tools, LLM txt  and scrapers to gather data for LLMs:

| Name |  |
| :------| :------------|
| [gitingest](https://github.com/cyclotruc/gitingest) | Replace `hub` with `ingest` in any github url to get a prompt-friendly extract of a codebase |
| [gitforme.tech](https://gitforme.tech) | For any github url to get llm txt - https://github.com/herin7/gitforme |
| [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | Tools do MCP do Firecral em https://mcp.so/server/firecrawl-mcp-server  And a online llm txt: https://llmstxt.firecrawl.dev/ or in repository: https://github.com/firecrawl/create-llmstxt-py |
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
| [Browseract.com](https://www.browseract.com/) | Integração com N8n e templates em https://www.browseract.com/blog/browseract-integration-guide-for-n8n [28] [29]|


## Explicabilidade

| Biblioteca / Método | PDP (Global) | ALE (Global) | Decomp. Func. (Global) | Import. Permut. (Global) | ICE (Local) | LIME (Local) | Contrafactual (Local) | SHAP (Local) | Downloads/mês | Github Stars | Documentação |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Scikit-learn** | ✅ | | | ✅ | ✅ | | | | 42,378,287 | 56.5K | [Link](https://scikit-learn.org/stable/getting_started.html) |
| **treeinterpreter** | | | | | | | | | 81,137 | 729 | [Link](https://pypi.org/project/treeinterpreter/) |
| **ELI5** | | | | ✅ | | ✅ | | | 412,788 | 229 | [Link](https://eli5.readthedocs.io/en/latest/) |
| **Dalex** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 18,231 | 1.3K | [Link](https://dalex.drwhy.ai/) |
| **ALIBI explain** | ✅ | ✅ | | ✅ | ✅ | ✅ | ✅ | ✅ | 18,435 | 2.2K | [Link](https://docs.seldon.io/projects/alibi/en/latest/) |
| **interpretML** | ✅ | | | | | ✅ | | ✅ | 78,810 | 5.8K | [Link](https://interpret.ml/docs/index.html) |
| **OmniXAI** | ✅ | ✅ | | | | ✅ | ✅ | ✅ | 1,534 | 733 | [Link](https://opensource.salesforce.com/OmniXAI/latest/index.html) |
| **scikit-explain** | ✅ | ✅ | | ✅ | ✅ | ✅ | | ✅ | 529 | 17 | [Link](https://scikit-explain.readthedocs.io/en/latest/) |
| **pdpbox** | ✅ | | | | ✅ | | | | 23,067 | 787 | [Link](https://pdpbox.readthedocs.io/en/latest/) |
| **pyAle** | | ✅ | | | | | | | 1,940 | 46 | [Link](https://github.com/DanaJomar/PyALE) |
| **LIME** | | | | | | ✅ | | | 298,094 | 11K | [Link](https://lime.readthedocs.io/en/latest/) |
| **Shap or Shapley** | | | | | | | | ✅ | 6,848,557 | 20.6K | [Link](https://shap.readthedocs.io/en/latest/) |


| Biblioteca | LOCAL: Regressão (Lin/Log) | LOCAL: Árvores / RF | LOCAL: GBMs | GLOBAL: Regressão (Lin/Log) | GLOBAL: Árvores / RF | GLOBAL: GBMs |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scikit-learn** | ✅ | | | ✅ | ✅ | ✅ |
| **treeinterpreter**| | ✅ | | | | |
| **ELI5** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Dalex** | | | | | | |
| **ALIBI explain** | | | | | | |
| **interpretML** | ✅ | ✅ (Apenas Árvores) | | ✅ | ✅ (Apenas Árvores) | |
| **OmniXAI** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **scikit-explain** | | ✅ | | | | |
| **pdpbox** | | | | | | |
| **pyAle** | | | | | | |
| **LIME** | | | | | | |
| **Shap** | | | | | | |

>**Observação sobre Dalex e ALIBI**: Na tabela de modelos intrínsecos (verde/roxo), essas bibliotecas aparecem vazias na imagem original, pois elas geralmente focam em explicar modelos gerados por outras bibliotecas (model-agnostic) em vez de fornecerem seus próprios modelos intrínsecos.

![Figura original](https://github.com/user-attachments/assets/72864da8-6f6e-4f2a-967d-46be7c69579a)

    
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
