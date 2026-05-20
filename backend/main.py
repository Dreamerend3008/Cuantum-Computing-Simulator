#It control the start / end of the app.
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_router
import uvicorn

origenes = [
    "http://localhost:4321",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    #The code when starts the app
    print("Iniciando app...")
    yield
    #The code when finishes the app
    print("Finalizando app...")

#Defines an app with a context manager
app = FastAPI(lifespan = lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origenes,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Include the API router
app.include_router(api_router, prefix = "/api")

#This is the command that allows you launch the server with "python3 main.py".
#It allows do a better debugging of the code
if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload = True)
