from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings


loader = TextLoader("docs.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap = 50)
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings()) #text ko embeddings mein kia fir store in FAISS vector database

retriever = vectorstore.as_retriever()

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "What are the key takeways from the documents?"
answer = qa_chain.run(query)

print("answer:", answer)