from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


