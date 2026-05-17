from typing import Literal
from pydantic import BaseModel, Field
"""
Literal, de typing restringe los valores del string a una lista [val1, val2]
Mientras que Field() hacer verificaciones de pydantic sobre tipado
                ->ej: ge = 0 es greater or equal than 0.
"""

class CircuitInput(BaseModel):
    initial_state: str
    num_qubits: int = Field(ge = 1)
    instructions: list[dict]
    #Check quisquit_buider to understand instructions form
    shots: int = Field(ge = 1)
    num_clbits: int = Field(ge = 0)
    noise_model: Literal["depolarizing", "thermal_relaxation"] | None = None
    runner_mode: Literal["shot", "statevector"]

    #Return a JSON with the info of a circuit.     
    def dict_builder(self):
        initial_instructions = []
        for c, i in zip(self.initial_state, range(self.num_qubits)):
            if c == '1':
                initial_instructions.append({"name": "X", "qubits": [i]})
        
        instructions = list(self.instructions)
        if self.runner_mode == 'shot':
            instructions.append({"name": "MEASURE_ALL"})

        instructions = initial_instructions + instructions
        
        return {
            "name": "Testing",
            "num_qubits": self.num_qubits,
            "num_clbits": self.num_clbits,
            "instructions": instructions,
            "runner_mode": self.runner_mode,
            "noise_model": self.noise_model,
            "shots": self.shots
        }


#Output classes
class SimulationResult(BaseModel):
    measure: dict[str, int] 
    #There are the measurements of a experiment
    real_probabilities: dict[str, float]
    #There are the probabilities of a set of experiments

    state_vector: list[complex] | None = None
