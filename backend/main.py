#It control the start / end of the app.
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import api_router
import uvicorn

#This is the command that allows you launch the server with "python3 main.py".
#It allows do a better debugging of the code
if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload = True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    #The code when starts the app
    print("Iniciando app...")
    yield
    #The code when finishes the app
    print("Finalizando app...")

#Defines an app with a context manager
app = FastAPI(lifespan = lifespan)
#Include the API router
app.include_router(api_router, prefix = "/api")
