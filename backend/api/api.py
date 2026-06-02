#Is the router manager
from fastapi import APIRouter
from api.endpoints import circuits, simulations

#Here I pick up all of the endpoints defined in the route
api_router = APIRouter()
api_router.include_router(circuits.router, prefix = "/circuits", tags = ["circuits"])
api_router.include_router(simulations.router, prefix = "/simulations", tags = ["simulations"])
