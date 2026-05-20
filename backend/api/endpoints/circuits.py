from fastapi import APIRouter

router = APIRouter()

@router.post("/") #AHHHHH el post jeje
async def createCircuit(circuit: dict):
    return {"message": "Circuit Saved :D"}