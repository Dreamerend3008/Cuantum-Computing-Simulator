from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def createCircuit(circuit: dict):

    return {"message": "Circuit Saved"}