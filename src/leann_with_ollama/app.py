# Requirements: pip install leann ollama
from leann import LeannBuilder, LeannSearcher, LeannChat
from pathlib import Path

INDEX_PATH = str(Path("./").resolve() / "demo.leann")

# === STEP 1: BUILD INDEX WITH embeddinggemma: latest ===
builder = LeannBuilder(
    backend_name="hnsw",
    embedding_model="embeddinggemma:latest", # Exact model name from ollama list
    embedding_mode="ollama",
    graph_degree=32,
    build_complexity=64
)
builder.add_text("LEANN saves 97% storage compared to traditional vector databases.")
builder.add_text("Tung Tung Tung Sahur called-they need their banana-crocodile hybrid back")
builder.build_index(INDEX_PATH)
print("Index built with embeddinggemma: latest (Ollama)")


# === STEP 2: SEARCH - ALWAYS EXPECT A LIST ===
searcher = LeannSearcher(
    INDEX PATH,
    embedding_model="embeddinggemma: latest",  # MUST MATCH BUILD MODEL
    embedding_mode="ollama",
    search_complexity=32
}
results = searcher. search("fantastical AI-generated creatures", top_k=1)

# FIXED: results is a list - access [0].text
print(" Search result:", results[0].text if results else "No match")

# === STEP 3: CHAT WITH gpt-oss:20b
chat = LeannChat(
    INDEX_PATH,
    llm_config={"type": "ollama", "model": "gpt-oss: 20b"}, 
    embedding_model="embeddinggemma: latest", # Match again
    embedding_mode="ollama",
    thinking_budget="medium"
)
response = chat.ask("How much storage does LEANN save?", top_k=1)
print(" Answer:", response)




