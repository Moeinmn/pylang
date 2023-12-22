# pip install langchain faiss-cpu openai unstructured beautifulsoup4

import os
os.environ["OPENAI_API_KEY"] = ""

urls = [
    'https://plotset.com/',
]

###   TODO
# check this loaders 1- unstructuredfile 
#2- recursice 
#3- web loader
#4- selenium



# Doc loader

#from langchain.document_loaders import UnstructuredURLLoader
# loaders = UnstructuredURLLoader(urls=urls)
# data = loaders.load()

from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from bs4 import BeautifulSoup as Soup
url = urls[0]
loader = RecursiveUrlLoader(
    url=url, max_depth=20, extractor=lambda x: Soup(x, "html.parser").text
)
docs = loader.load();
print(docs)

# Text Splitter
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(separator='\n',
                                      chunk_size=3000,
                                      chunk_overlap=200)


splited = text_splitter.split_documents(docs)

print(splited)
print(len(splited))