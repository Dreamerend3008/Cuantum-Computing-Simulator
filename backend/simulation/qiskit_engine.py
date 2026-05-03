from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def run_statevector_simulation(qc: QuantumCircuit) -> np.ndarray:
    simulator = AerSimulator(method='statevector')
    
    # We need a copy because we are adding an instruction to save the state
    simulation_circuit = qc.copy()
    simulation_circuit.save_statevector()
    
    # Run the simulation
    job = simulator.run(simulation_circuit)
    result = job.result()
    
    # Return the statevector array
    return np.asarray(result.get_statevector())
