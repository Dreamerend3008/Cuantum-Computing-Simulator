from simulation.qiskit_engine import run_shot_simulator, run_statevector_simulation
from core.qiskit_builder import build_circuit
from .circuit_service import build_circuit_from_dict
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
    
    q_circuit = build_circuit_from_dict(circuit_dict)
    
    # Decompose the circuit so Aer Simulator can understand high-level gates like QFT
    q_circuit = q_circuit.decompose()

    instructions = circuit_dict.get("instructions", [])

    runner_mode = circuit_dict.get("runner_mode", "")
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
        
        raw_counts = output["info"].get_counts()
        output["results"] = {k[::-1]: v for k, v in raw_counts.items()}
        
        # New: Get statevector behind the scenes for Bloch sphere visualization
        try:
            q_circuit_sv = q_circuit.copy()
            q_circuit_sv.remove_final_measurements()
            output["statevector_results"] = run_statevector_simulation(qc=q_circuit_sv)
        except Exception:
            output["statevector_results"] = None
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