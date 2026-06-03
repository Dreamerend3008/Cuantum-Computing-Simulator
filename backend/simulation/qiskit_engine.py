from simulation.noise_engine import get_noise_model
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np

def run_statevector_simulation(qc: QuantumCircuit) -> np.ndarray:
    num_qubits = qc.num_qubits
    
    simulator = AerSimulator(method='statevector')
    
    simulation_circuit = qc.copy()
    simulation_circuit.save_statevector()
    
    simulation_circuit = transpile(simulation_circuit, simulator)
    
    job = simulator.run(simulation_circuit)
    result = job.result()
    values = np.asarray(result.get_statevector()).tolist()

    limit = 2**num_qubits
    bits = [f"{i:0{num_qubits}b}"[::-1] for i in range(2**num_qubits)]

    return dict(zip(bits, values))
def run_shot_simulator(qc: QuantumCircuit, number_shots: int, n_model: str):
    noise_model = get_noise_model(n_model) if n_model else None
    # Pass noise_model to constructor so transpile() uses the correct basis gates
    simulator = AerSimulator(noise_model=noise_model) if noise_model else AerSimulator()
    qc_transpiled = transpile(qc, simulator)
    return simulator.run(qc_transpiled, shots=number_shots).result()

