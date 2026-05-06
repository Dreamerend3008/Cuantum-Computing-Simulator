from pydantic import BaseModel
from typing import Optional

#Claude me recomendó estas clases de encapsulamiento xd


#Input classes
class Gate(BaseModel):
    name: str
    qubit: int
    target: Optional[int] = None 
    #Just for the CNOT gate, when you have to put a 0 in control

class CircuitInput(BaseModel):
    num_qubits: int
    gates: list[Gate]
    shots: int 
    #How many experiments you will realize     


#Output classes
#Como toca tirar JSON, entonces usamos diccionarios
class SimulationResult(BaseModel):
    measurements: dict[str, int] 
    #Son las medidas del estilo "00": "400", o "número": "cantidad de caidas allí"
    probabilities: dict[str, float]
    #Lo mismo pero con probabilidades
    state_vector: list[complex] #wtffff hay un tipo primitivo complex
    circuit_diagram: 
    