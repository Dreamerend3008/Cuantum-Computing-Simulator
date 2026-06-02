from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

def qft(qc: QuantumCircuit, q: list[int]):
    qft_circuit = QFT(num_qubits=len(q), do_swaps=True).decompose()
    qc.compose(qft_circuit, q, inplace=True)

def iqft(qc: QuantumCircuit, q: list[int]):
    iqft_circuit = QFT(num_qubits=len(q), do_swaps=True, inverse=True).decompose()
    qc.compose(iqft_circuit, q, inplace=True)