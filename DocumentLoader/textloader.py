from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs)
print(type(docs)) #list of documents, len of list 1 aayegi, docs[0]=metadata v deta h, doc[0].page_content or docs[0].metadata