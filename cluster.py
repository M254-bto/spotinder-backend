from fastapi import FastAPI
import pickle



app = FastAPI()


@app.get('/')
async def read_cluster():
    return {"Data": "Cluster"}