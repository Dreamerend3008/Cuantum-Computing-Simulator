from qiskit import QuantumCircuit
from .custom_circuits.half_adder import half_adder
from .custom_circuits.full_adder import full_adder, old_full_adder
from .custom_circuits.qft import qft, iqft
from .custom_circuits.mod_exp import mod_exp
from services.custom_gate_service import get_custom_gate

import math

def safe_initialize(qc, q, p):
    # Treat user input as quantum amplitudes (as requested, reverting back)
    norm = math.sqrt(sum(abs(x)**2 for x in p))
    if norm > 0:
        p_norm = [x / norm for x in p]
    else:
        p_norm = [1.0] + [0.0] * (len(p) - 1)
    qc.initialize(p_norm, q)

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
    "OLD_FULL_ADD": lambda qc, q, p: old_full_adder(qc, q),
    "QFT": lambda qc, q, p: qft(qc, q),
    "IQFT": lambda qc, q, p: iqft(qc, q),
    "MOD_EXP": lambda qc, q, p: mod_exp(qc, q, p),
    "INITIALIZE": lambda qc, q, p: safe_initialize(qc, q, p)
}

def apply_gate(qc: QuantumCircuit, gate_name: str, qubits: list[int], params: list[float] = None):
    if params is None:
        params = []
    
    if gate_name in GATE_MAP:
        GATE_MAP[gate_name](qc, qubits, params)
        return

    custom_gate = get_custom_gate(gate_name)
    if custom_gate:
        if len(qubits) != custom_gate.num_qubits:
            raise ValueError(f"Gate {gate_name} requires {custom_gate.num_qubits} qubits, but got {len(qubits)}")
        for instr in custom_gate.instructions:            
            sub_name = instr.get('name')
            mapped_qubits = [qubits[i] for i in instr.get('qubits', [])]
            sub_params = instr.get('params', [])

            apply_gate(qc, sub_name, mapped_qubits, sub_params)
        return
    raise ValueError(f"Unknown gate: {gate_name}")