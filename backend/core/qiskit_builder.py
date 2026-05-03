from qiskit import QuantumCircuit
from core.gate_mapper import apply_gate

def build_circuit(num_qubits: int, instructions: list[dict]) -> QuantumCircuit:
    """
    Builds a Qiskit QuantumCircuit from a list of generic instruction dictionaries.
    
    Expected format for instructions:
    [
        {"name": "H", "qubits": [0]},
        {"name": "CX", "qubits": [0, 1]}
    ]
    """
    qc = QuantumCircuit(num_qubits)
    for instr in instructions:
        name = instr.get("name")
        qubits = instr.get("qubits", [])
        params = instr.get("params", [])
        apply_gate(qc, name, qubits, params)
    qc = qc.reverse_bits()
    return qc
