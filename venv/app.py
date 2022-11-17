from fastapi import FastAPI, Depends
import psycopg2
import uvicorn
from psycopg2.extras import RealDictCursor

app = FastAPI()

def get_db():
    with psycopg2.connect(
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432,
        database="startml",
    ) as conn:
        return conn



@app.get('/user')
def get_all_uesrs(limit: int = 10, db=Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            f"""
            SELECT *
            FROM "user"
            LIMIT {limit}
            """
        )
        return cursor.fetchall()
