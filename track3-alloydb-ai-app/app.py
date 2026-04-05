from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    host="ALLOYDB_HOST",
    database="postgres",
    user="postgres",
    password="PASSWORD"
)

@app.get("/tasks")
def get_tasks():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    return {"tasks": rows}
