from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv("incidents.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Remove duplicate header rows
df = df[df["incident_id"] != "incident_id"]

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------------------------------------------
# CREATE SEARCHABLE TEXT
# ---------------------------------------------------

texts = (
    df["title"].astype(str)
    + " "
    + df["description"].astype(str)
).tolist()

# ---------------------------------------------------
# CREATE EMBEDDINGS
# ---------------------------------------------------

embeddings = model.encode(
    texts,
    convert_to_numpy=True
)

embeddings = embeddings.astype(
    "float32"
)

# ---------------------------------------------------
# CREATE FAISS INDEX
# ---------------------------------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

# ---------------------------------------------------
# SEARCH FUNCTION
# ---------------------------------------------------

def search_similar_incidents(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = query_embedding.astype(
        "float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx, distance in zip(
        indices[0],
        distances[0]
    ):

        similarity_score = round(
            (1 / (1 + distance)) * 100,
            2
        )

        # Ignore weak matches
        if similarity_score < 55:
            continue

        results.append({

            "incident_id":
            df.iloc[idx]["incident_id"],

            "title":
            df.iloc[idx]["title"],

            "description":
            df.iloc[idx]["description"],

            "resolution":
            df.iloc[idx]["resolution"],

            "severity":
            df.iloc[idx]["severity"],

            "similarity":
            similarity_score
        })

    return results