import os
import pandas as pd
from pymongo import MongoClient

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_DB = os.getenv("MONGO_DB", "medical_data")
client = MongoClient("mongodb://admin:secret@mongo:27017/")
db = client[MONGO_DB]
collection = db["patients"]

file_path = "/data/healthcare_dataset-20250506.csv"
df = pd.read_csv(file_path, sep=";")

df.columns = [col.strip().replace(" ", "_") for col in df.columns]

documents = df.to_dict(orient="records")

collection.insert_many(documents)
print(f"{len(documents)} documents inséré.")