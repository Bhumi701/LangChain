import langchain

print(langchain.__version__)

import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))