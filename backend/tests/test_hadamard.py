from core.qiskit_builder import build_circuit
from simulation.qiskit_engine import run_statevector_simulation
import numpy as np

def test_hadamard_pipeline():
    instructions = [
        {"name": "H", "qubits": [0]}
    ]
    qc = build_circuit(num_qubits=1, instructions=instructions)
    statevector = run_statevector_simulation(qc)
    # 4. Check the results. H on |0> gives [1/√2, 1/√2]
    expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    print("Resulting Statevector:", statevector)
    print("Expected Statevector: ", expected)
    
if __name__ == "__main__":
    test_hadamard_pipeline()
