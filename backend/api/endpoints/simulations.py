from fastapi import APIRouter, HTTPException
from shared import SimulationResult, CircuitInput
from services.simulation_service import simulate_circuit
from qiskit.exceptions import QiskitError
import time

router = APIRouter()

@router.post("/")
def createSimulation(simulation: dict):
    return {"message": "Simulation saved"}

@router.post("/run")
def executeSimulation(ci: CircuitInput):
    """
        So, what i understand is that this is the standard form to connect our
        base logic (Harry's logic) with the api. this func is called when you
        run the simulation
    """
    try:
        data = ci.dict_builder() 
        result = simulate_circuit(data, time.time())

    except QiskitError as e:

        raise HTTPException(status_code=400, detail=f"Circuit not valid for simulator: {str(e)}") from e
    
    except (ValueError, TypeError, KeyError) as e:

        raise HTTPException(status_code=422, detail=f"Invalid simulation input: {str(e)}") from e

    if not result.get("success"):

        raise HTTPException(status_code=400, detail=result.get("error", "Simulation failed"))

    counts = result.get('output').get('results')

    if ci.runner_mode == "shot":
        counts = {k: v / ci.shots for k, v in counts.items() }
    else:
        counts = {k: v**2 for k, v in counts.items()}
        
    out = SimulationResult(probabilities = counts)

    return {"status": "success", "data": out}
