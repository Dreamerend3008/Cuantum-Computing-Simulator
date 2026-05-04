from qiskit import QuantumCircuit
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer.primitives import SamplerV2 as AerSampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

qc = QuantumCircuit(4)
qc.x(0)
qc.h(1)
qc.cx(0, 2)
qc.measure_all()

backend = GenericBackendV2(num_qubits=4)
pm = generate_preset_pass_manager(target=backend.target, optimization_level=1)
isa_qc = pm.run(qc)

sampler = AerSampler() # Wait, how does AerSampler take the backend? Let's check help
