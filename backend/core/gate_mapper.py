from qiskit import QuantumCircuit

def half_adder(qc: QuantumCircuit, q: list[int]):

    qc.cx(q[0], q[2])
    qc.cx(q[1], q[2])
    qc.ccx(q[0], q[1], q[3])


def full_adder(qc: QuantumCircuit, q: list[int]):
    
    # Paso 1: Primer Half Adder (Suma A y B)
    half_adder(qc, [q[0], q[1], q[3], q[4]])
    
    # Paso 2: Segundo Half Adder (Suma la 'Suma Parcial' S1 y Cin)
    half_adder(qc, [q[3], q[2], q[6], q[5]])
    
    # Paso 3: Acarreo Final (Cout = C1 XOR C2) Pero C1 y C2 no pueden ser 1 al mismo tiempo
    qc.cx(q[4], q[7])
    qc.cx(q[5], q[7])

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
    "FULL_ADD": lambda qc, q, p: full_adder(qc, q)
}

def apply_gate(qc: QuantumCircuit, gate_name: str, qubits: list[int], params: list[float] = None):
    if params is None:
        params = []
    
    if gate_name not in GATE_MAP:
        raise ValueError(f"Gate {gate_name} not supported.")
        
    GATE_MAP[gate_name](qc, qubits, params)
