from simulation.qiskit_engine import run_shot_simulator, run_statevector_simulation
from core.qiskit_builder import build_circuit
import numpy as np
import time

example_dict = {
    "name": "GHZ Circuit",
    "num_qubits": 4,
    "num_clbits": 4,
    "instructions": [
                    {"name": "H", "qubits": [0]},
                    {"name": "CX", "qubits": [0,1]},
                    {"name": "CX", "qubits": [0,2]},
                    {"name": "CX", "qubits": [0,3]},
                    {"name": "MEASURE_ALL"}
                    ],
    "runner_mode": "shot", # "shot" or "statevector"
    "noise_model": 'depolarizing', # 'depolarizing', 'thermal_relaxation'
    "shots": 1024,
}

def simulate_circuit(circuit_dict: dict, start_time: float) -> dict:

    runner_mode = circuit_dict.get("runner_mode", "")
    num_qubits = circuit_dict.get("num_qubits", 0)
    num_clbits = circuit_dict.get("num_clbits", 0)
    instructions = circuit_dict.get("instructions", [])

    q_circuit = build_circuit(num_qubits, num_clbits, instructions)

    output = {}
    if runner_mode == "shot":

        # Measurement is needed to use shot simulator
        if not any(instr.get("name") == "MEASURE_ALL" or instr.get("name") == "MEASURE" for instr in instructions):
            return  {
                        "output": None,
                        "success": False,
                        "error": "Shot simulation cannot be run without measurement instructions."
                    }
        

        shots = circuit_dict.get("shots", 1024)
        noise_model = circuit_dict.get("noise_model", None)

        output["info"] = run_shot_simulator(qc=q_circuit, number_shots=shots, n_model=noise_model)
        
        output["results"] = output["info"].get_counts()
    elif runner_mode == "statevector":
        # Measurment breaks the logic expected for a staetvector simulator
        if any(instr.get("name") == "MEASURE_ALL" or instr.get("name") == "MEASURE" for instr in instructions):
            return  {
                        "output": None,
                        "success": False,
                        "error": "Statevector simulation cannot be run with measurement instructions."
                    }
        
        output["results"] = run_statevector_simulation(qc=q_circuit)
    else:
        return  {
                    "output": None,
                    "success": False,
                    "error": f"Invalid runner mode: {runner_mode}"
                }
    return  {
                "output": output,
                "success": True,
                "execution_time": time.time() - start_time,
                "time": time.time() - start_time
            }


# Example usage
if __name__ == "__main__":
    start_time = time.time()
    simulation_result = simulate_circuit(example_dict, start_time)
    if simulation_result["success"]:
        print("Simulation successful. Results:")
        print(simulation_result.get("output", {}).get("results", {}))
    else:
        print("Simulation failed with error:")
        print(simulation_result.get("error", "Unknown error"))