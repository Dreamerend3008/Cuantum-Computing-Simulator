from fastapi import APIRouter
from shared import CustomGateDef
from services.custom_gate_service import save_custom_gate, get_custom_gate, delete_custom_gate, get_all_gates

router = APIRouter()


@router.post("/create_custom_gate")
def create_custom_gate(cg: CustomGateDef):
    # no creo que hagan falta verificaciones de formato, debido a que las 
    # instrucciones son de compuertas que soportamos en el sistema y el formato 
    # se manda directamente desde el front asi que no deberian haber errores de formato.
    #bro además las verificaciones de formato las hace Pydantic según cómo haces la clase   
    save_custom_gate(cg)
    return {"status": "success"}

@router.post("/delete_gate/{name}")
def deleteCustomGate(name: str):
    delete_custom_gate(name)
    return {"status" : "success"}

@router.get("/get_all_gates")
def getAllCustomGates() -> dict:
    return {"data" : get_all_gates()}

@router.get("/get_gate/{name}")
def getCustomGate(name : str):
    return {"data" : get_custom_gate(name)}