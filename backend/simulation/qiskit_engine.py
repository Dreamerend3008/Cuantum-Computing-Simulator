from simulation.noise_engine import get_noise_model
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def run_statevector_simulation(qc: QuantumCircuit) -> np.ndarray:

    simulator = AerSimulator(method='statevector')
    
    simulation_circuit = qc.copy()
    simulation_circuit.save_statevector()
    
    job = simulator.run(simulation_circuit)
    result = job.result()
    return np.asarray(result.get_statevector())


def run_shot_simulator(qc: QuantumCircuit, number_shots: int, n_model: str) -> np.ndarray:
    simulator = AerSimulator()
    if not n_model:
        return simulator.run(qc,shots=number_shots).result()
    else:
        return simulator.run(
            qc,
            shots=number_shots, 
            noise_model=get_noise_model(n_model)
        ).result()

