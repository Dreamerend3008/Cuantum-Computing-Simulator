from qiskit import QuantumCircuit

def half_adder(qc: QuantumCircuit, q: list[int]):

    qc.cx(q[0], q[2])
    qc.cx(q[1], q[2])
    qc.ccx(q[0], q[1], q[3])