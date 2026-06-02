from qiskit import QuantumCircuit
from  .half_adder import half_adder

def old_full_adder(qc: QuantumCircuit, q: list[int]):
    
    half_adder(qc, [q[0], q[1], q[3], q[4]])
    half_adder(qc, [q[3], q[2], q[6], q[5]])
    
    qc.cx(q[4], q[7])
    qc.cx(q[5], q[7])

def full_adder(qc: QuantumCircuit, q: list[int]):
    # 4  bit quantum full adder
    qc.ccx(q[0], q[1], q[3])

    qc.cx(q[0], q[1])

    qc.ccx(q[1], q[2], q[3])

    qc.cx(q[1], q[2])

    qc.cx(q[0], q[1])