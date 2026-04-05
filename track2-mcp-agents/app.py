from fastapi import FastAPI
from google.cloud import bigquery

app = FastAPI()
client = bigquery.Client()

@app.get("/data")
def get_data():
    query = "SELECT name FROM `project.dataset.table` LIMIT 5"
    results = client.query(query)
    return {"data": [row.name for row in results]}
