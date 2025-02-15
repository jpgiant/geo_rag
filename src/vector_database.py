from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(chunks):
    embeddings=HuggingFaceEmbeddings()
    vector_store=Chroma.from_texts([chunk[1] for chunk in chunks],embeddings)
    return vector_store

if __name__=="__main__":
    from data_preprocessing import preprocess_data
    chunks=preprocess_data()
    vector_store=create_vector_store(chunks)
    print("Vector Store Created!")