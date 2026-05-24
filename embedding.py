import json
import numpy as np
from sentence_transformers import SentenceTransformer


# =========================================================
# LOAD MODEL
# =========================================================

# all-MiniLM-L6-v2 = 384 dimensions
# You asked for 1024 dimensions, so we pad vectors to 1024

model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================================================
# FUNCTION: CONVERT JSON RECORDS TO CHUNKS
# =========================================================

def json_to_chunks(json_data):
    """
    Converts each JSON object into a text chunk.
    """

    chunks = []

    for record in json_data:

        chunk = f"""
        MS Ticket Number: {record.get("MS ticket number", "")}
        Subscription Name: {record.get("subscription name", "")}
        Service: {record.get("Service", "")}
        Title: {record.get("title", "")}
        Severity: {record.get("Serverity", "")}
        Severity Raw: {record.get("severity_raw", "")}
        Created Date: {record.get("created_date", "")}
        Resolution Hours: {record.get("resolution_hours", "")}
        Resolution Days: {record.get("resolution_days", "")}
        Status: {record.get("status", "")}
        Issue Summary: {record.get("issue_summary", "")}
        Root Cause: {record.get("root_cause", "")}
        Resolution Summary: {record.get("resolution_summary", "")}
        Analysis: {record.get("analysis", "")}
        What Went Wrong: {record.get("what_went_wrong", "")}
        Best Practices: {record.get("best_practices", "")}
        """

        chunks.append(chunk.strip())

    return chunks


# =========================================================
# FUNCTION: CREATE 1024-D EMBEDDINGS
# =========================================================

def create_embeddings(chunks):
    """
    Converts text chunks into embeddings.
    Pads embeddings to 1024 dimensions.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    padded_embeddings = []

    for emb in embeddings:

        # Current dimension = 384
        current_dim = emb.shape[0]

        # Pad to 1024
        if current_dim < 1024:

            padded = np.pad(
                emb,
                (0, 1024 - current_dim),
                mode='constant'
            )

        else:
            padded = emb[:1024]

        padded_embeddings.append(padded)

    return np.array(padded_embeddings)


# def embedding_func(json_file):

#     # LOAD JSON FILE
#     with open(json_file, "r", encoding="utf-8") as f:
#         json_data = json.load(f)

#     # CREATE CHUNKS
#     chunks = json_to_chunks(json_data)

#     print(f"Total Chunks: {len(chunks)}")

#     # CREATE EMBEDDINGS
#     embeddings = create_embeddings(chunks)

#     print(f"Embedding Shape: {embeddings.shape}")

#     # SAMPLE OUTPUT
#     print("\nFirst Chunk:\n")
#     print(chunks[0])

#     print("\nFirst Embedding:\n")
#     print(embeddings[0])

#     print("\nEmbedding Dimension:")
#     print(len(embeddings[0]))


def embedding_func(json_file):

    # =========================================================
    # LOAD JSON FILE
    # =========================================================

    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # =========================================================
    # CREATE CHUNKS
    # =========================================================

    chunks = json_to_chunks(json_data)

    print(f"Total Chunks: {len(chunks)}")

    # =========================================================
    # SAVE CHUNKS
    # =========================================================

    chunk_dict = {}

    for i, chunk in enumerate(chunks, start=1):
        chunk_dict[f"chunk_{i}"] = chunk

    with open("chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunk_dict, f, indent=4, ensure_ascii=False)

    print("Chunks saved -> chunks.json")

    # =========================================================
    # CREATE EMBEDDINGS
    # =========================================================

    embeddings = create_embeddings(chunks)

    print(f"Embedding Shape: {embeddings.shape}")

    # =========================================================
    # SAVE EMBEDDINGS
    # =========================================================

    np.save("embeddings.npy", embeddings)

    print("Embeddings saved -> embeddings.npy")

    # =========================================================
    # OPTIONAL: SAVE EMBEDDINGS AS JSON
    # =========================================================

    embedding_json = {}

    for i, emb in enumerate(embeddings, start=1):
        embedding_json[f"chunk_{i}"] = emb.tolist()

    with open("embeddings.json", "w", encoding="utf-8") as f:
        json.dump(embedding_json, f)

    print("Embeddings JSON saved -> embeddings.json")

    # =========================================================
    # SAMPLE OUTPUT
    # =========================================================

    # print("\nFirst Chunk:\n")
    # print(chunks[0])

    # print("\nFirst Embedding:\n")
    # print(embeddings[0])

    # print("\nEmbedding Dimension:")
    # print(len(embeddings[0]))