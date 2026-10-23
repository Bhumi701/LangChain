from langchain_community.document_loaders import PyPDFLoader, PDFPlumberLoader

loader = PDFPlumberLoader('Unit-2 Notes.pdf')
docs = loader.load()
print(docs)
print(len(docs)) #per page

#pip install pypdf, pdfplumber

print(docs[0].page_content)
print(docs[1].metadata)