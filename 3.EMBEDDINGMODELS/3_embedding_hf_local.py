from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

documents = [
  "What is the capital of France?",
  "What is the capital of Germany?",  
  "What is the capital of Italy?",
  "What is the capital of Spain?",
  "What is the capital of Portugal?"
]

#text = "What is the capital of France?"
#vector = embedding.embed_query(text)
vector = embedding.embed_documents(documents)

print(str(vector))