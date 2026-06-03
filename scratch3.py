from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

simulator = AerSimulator(method='statevector')
simulation_circuit = qc.copy()
simulation_circuit.save_statevector()
simulation_circuit = transpile(simulation_circuit, simulator)
job = simulator.run(simulation_circuit)
result = job.result()
values = np.asarray(result.get_statevector()).tolist()
print(values)
