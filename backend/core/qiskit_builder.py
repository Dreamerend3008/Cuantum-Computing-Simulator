from qiskit import QuantumCircuit
from core.gate_mapper import apply_gate

def build_circuit(num_qubits: int, num_clbits: int ,instructions: list[dict]) -> QuantumCircuit:
    """
    [
        {"name": "H", "qubits": [0]},
        {"name": "CX", "qubits": [0, 1]}
    ]
    """
    if not num_clbits:
        num_clbits = 0
    qc = QuantumCircuit(num_qubits,num_clbits)
    for instr in instructions:
        name = instr.get("name")
        qubits = instr.get("qubits", [])
        
        if name.lower() == "measure":
            clbits = instr.get("clbits", qubits)
            qc.measure(qubits, clbits)
        elif name.lower() == "measure_all":
            qc.measure_all()
        else:
            params = instr.get("params", [])
            apply_gate(qc, name, qubits, params)
    

    qc = qc.reverse_bits()
    return qc
