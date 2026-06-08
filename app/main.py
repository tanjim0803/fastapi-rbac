from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.session import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is running...")
    await create_tables()
    yield
    print("Server has been stopped...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}
