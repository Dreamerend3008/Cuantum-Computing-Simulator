from fastapi import APIRouter, HTTPException
from shared.interfaces import CustomGateDef
from services.custom_gate_service import (
    get_all_gates, 
    get_custom_gate, 
    save_custom_gate, 
    delete_custom_gate
)

router = APIRouter()

@router.post("/") #AHHHHH el post jeje
async def createCircuit(circuit: dict):
    return {"message": "Circuit Saved :D"}

@router.get("/custom-gates")
async def list_custom_gates():
    return get_all_gates()

@router.post("/custom-gates")
async def create_custom_gate(gate: CustomGateDef):
    try:
        save_custom_gate(gate)
        return {"message": "Custom gate saved successfully", "gate": gate.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/custom-gates/{name}")
async def remove_custom_gate(name: str):
    try:
        delete_custom_gate(name)
        return {"message": f"Custom gate {name} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))