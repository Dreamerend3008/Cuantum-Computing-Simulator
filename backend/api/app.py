from fastapi import FastAPI
from pydantic import BaseModel

class MainApp:
    __api:FastAPI

    #This only reveal the property of "api", dont let modify the atribute outside
    #Ouuuuu yea
    @property
    def api(self) -> FastAPI:
        return self.__api

    def __init__(self):
        self.__api = FastAPI()
        self.__register_routes()
    
    
    def __register_routes(self):
        @self.__api.get("/") #Its like "when you recieve /"
        def Test():
            return {"message": "Hola mundo"}

        