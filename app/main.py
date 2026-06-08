from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.session import create_tables
from app.api.routes import master_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is running...")
    await create_tables()
    yield
    print("Server has been stopped...")


app = FastAPI(lifespan=lifespan)


app.include_router(master_router)
