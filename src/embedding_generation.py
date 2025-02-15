from langchain.embeddings import HuggingFaceEmbeddings

def generate_embeddings(chunks):
    embeddings=HuggingFaceEmbeddings()
    return [embeddings.embed_query(chunk[1]) for chunk in chunks]

if __name__=="__main__":
    from data_preprocessing import preprocess_data
    chunks=preprocess_data()
    embeddings=generate_embeddings(chunks)
    print(f"Generated {len(embeddings)} embeddings")