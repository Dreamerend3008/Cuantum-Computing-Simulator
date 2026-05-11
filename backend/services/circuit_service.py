from qiskit import QuantumCircuit
from core.qiskit_builder import build_circuit

def build_circuit_from_dict(circuit_dict: dict) -> QuantumCircuit:
    num_qubits = circuit_dict.get("num_qubits", 0)
    num_clbits = circuit_dict.get("num_clbits", 0)
    instructions = circuit_dict.get("instructions", [])
    return build_circuit(num_qubits, num_clbits, instructions)