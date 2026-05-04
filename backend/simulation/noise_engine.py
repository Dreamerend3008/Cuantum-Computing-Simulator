from qiskit_aer.noise import NoiseModel, depolarizing_error,thermal_relaxation_error

single_qubit_gates = ['h', 'x', 'y', 'z', 's', 't', 'rx', 'ry', 'rz']
double_qubit_gates = ['cx', 'cz', 'swap', 'ecr']

def get_noise_model(n_model_str: str) -> NoiseModel:
    noise_model = NoiseModel()
    if n_model_str == 'depolarizing':
        error_1q = depolarizing_error(0.01, 1)
        error_2q = depolarizing_error(0.01, 2)
        noise_model.add_all_qubit_quantum_error(error_1q, single_qubit_gates)
        noise_model.add_all_qubit_quantum_error(error_2q, double_qubit_gates)
        return noise_model
    elif n_model_str == 'thermal_relaxation':
        T1 = 50e-6
        T2 = 70e-6  
        error_single = thermal_relaxation_error(T1, T2, 100e-9)
        
        # 2-qubit gates need a 2-qubit error, so we tensor two 1-qubit errors together
        error_double_1q = thermal_relaxation_error(T1, T2, 300e-9)
        error_double = error_double_1q.tensor(error_double_1q)
        
        noise_model.add_all_qubit_quantum_error(error_single, single_qubit_gates)
        noise_model.add_all_qubit_quantum_error(error_double, double_qubit_gates)
        
        # 'swap' is 2-qubit, 'cxx' (Toffoli) is 3-qubit
        error_600ns_1q = thermal_relaxation_error(T1, T2, 600e-9)
        #noise_model.add_all_qubit_quantum_error(error_600ns_1q.tensor(error_600ns_1q), ['swap'])
        noise_model.add_all_qubit_quantum_error(error_600ns_1q.tensor(error_600ns_1q).tensor(error_600ns_1q), ['cxx'])
        return noise_model
    return noise_model        