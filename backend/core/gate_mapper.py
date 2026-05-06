from qiskit import QuantumCircuit
from .custom_circuits.half_adder import half_adder
from .custom_circuits.full_adder import full_adder, old_full_adder

GATE_MAP = {
    "H": lambda qc, q, p: qc.h(q[0]),
    "X": lambda qc, q, p: qc.x(q[0]),
    "Y": lambda qc, q, p: qc.y(q[0]),
    "Z": lambda qc, q, p: qc.z(q[0]),
    "S": lambda qc, q, p: qc.s(q[0]),
    "T": lambda qc, q, p: qc.t(q[0]),
    "RX": lambda qc, q, p: qc.rx(p[0], q[0]),
    "RY": lambda qc, q, p: qc.ry(p[0], q[0]),
    "RZ": lambda qc, q, p: qc.rz(p[0], q[0]),
    "CX": lambda qc, q, p: qc.cx(q[0], q[1]),
    "SWAP": lambda qc, q, p: qc.swap(q[0], q[1]),
    "CXX": lambda qc, q, p: qc.ccx(q[0], q[1], q[2]), # Toffoli gate
    "HALF_ADD": lambda qc, q, p: half_adder(qc, q),
    "FULL_ADD": lambda qc, q, p: full_adder(qc, q),
    "OLD_FULL_ADD": lambda qc, q, p: old_full_adder(qc, q)
}

def apply_gate(qc: QuantumCircuit, gate_name: str, qubits: list[int], params: list[float] = None):
    if params is None:
        params = []
    
    if gate_name not in GATE_MAP:
        raise ValueError(f"Gate {gate_name} not supported.")
        
    GATE_MAP[gate_name](qc, qubits, params)
