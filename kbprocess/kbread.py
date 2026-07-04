"""
Qdrant Collection Downloader (Read Only)

This script:
- Connects to Qdrant using a READ-ONLY API key
- Downloads all points from a collection
- Saves them into a local JSON file

It DOES NOT modify the database.
"""

import json
from qdrant_client import QdrantClient

# ==========================================================
# CONFIGURATION
# ==========================================================

QDRANT_URL = "https://2077ebcf-6d9d-4d4c-abd5-391d999fdcaa.us-east4-0.gcp.cloud.qdrant.io:6333"

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJyIiwiZXhwIjoxNzg4MDAyODE3LCJzdWJqZWN0IjoiYXBpLWtleTplNGFhNzNhNS04YjAyLTRkZjEtYjQzNC02ODc1MTk2NmZmM2MifQ.W2G4l4XUM-PaPkJH-WcDpv9ZwfRRtqvBYrqf-YTb24w"

COLLECTION_NAME = "education_knowledge_base"

OUTPUT_FILE = "education_knowledge_base.json"

BATCH_SIZE = 100

# ==========================================================
# CONNECT
# ==========================================================

print("Connecting to Qdrant...")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=API_KEY,
)

print("Connected successfully.\n")

# ==========================================================
# DOWNLOAD
# ==========================================================

all_points = []
offset = None
total = 0

print("Downloading collection...\n")

while True:

    points, offset = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=BATCH_SIZE,
        offset=offset,
        with_payload=True,
        with_vectors=False,   # Change to True if you also want embeddings
    )

    if not points:
        break

    for p in points:

        all_points.append({
            "id": p.id,
            "payload": p.payload
        })

    total += len(points)

    print(f"Downloaded: {total} points")

    if offset is None:
        break

# ==========================================================
# SAVE
# ==========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_points, f, indent=2, ensure_ascii=False)

print("\n----------------------------------")
print(f"Finished!")
print(f"Total Points : {total}")
print(f"Saved File   : {OUTPUT_FILE}")
print("----------------------------------")