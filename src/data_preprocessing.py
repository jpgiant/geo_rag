import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

def preprocess_data():
    with open('data/wikipedia_indian_geography.json', 'r') as f:
        data=json.load(f)

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    chunks=[]
    for item in data:
        doc_chunks=text_splitter.split_text(item['content'])
        chunks.extend([(item['title'], chunk) for chunk in doc_chunks])
    return chunks

if __name__=="__main__":
    preprocessed_data=preprocess_data()
    print(f"Total Chunks: {len(preprocessed_data)}")
