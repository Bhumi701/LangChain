from langchain_community.document_loaders import CSVLoader 
loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))

print(docs[0])





#   """
#   (venv) (base) PS C:\Users\Bhumi Bhardwaj\OneDrive\Desktop\langchain-models\DocumentLoader> python csvloader.py
# C:\Users\Bhumi Bhardwaj\OneDrive\Desktop\langchain-models\DocumentLoader\csvloader.py:1: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.
#   from langchain_community.document_loaders import CSVLoader
# 400
# page_content='User ID: 15624510
# Gender: Male
# Age: 19
# EstimatedSalary: 19000
# Purchased: 0' metadata={'source': 'Social_Network_Ads.csv', 'row': 0}
#   """