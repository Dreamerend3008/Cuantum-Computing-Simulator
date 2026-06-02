from qiskit import QuantumCircuit
import numpy as np

def initialize_state(qc: QuantumCircuit, state_vector: np.ndarray, qubits: list[int]):
    qc.initialize(state_vector, qubits)