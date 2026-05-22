from qiskit import QuantumCircuit

def c_amod15(a, power):
    """Controlled multiplication by a mod 15.
    Works for a in [2,4,7,8,11,13]."""
    if a not in [2, 4, 7, 8, 11, 13]:
        raise ValueError("'a' must be 2, 4, 7, 8, 11 or 13")
    
    U = QuantumCircuit(4)        
    for _ in range(power):
        if a in [2, 13]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
        if a in [7, 8]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
        if a in [4, 11]:
            U.swap(1, 3)
            U.swap(0, 2)
        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)
                
    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"
    c_U = U.control(1) # 1 control qubit
    return c_U

def mod_exp(qc: QuantumCircuit, q: list[int], p: list[float]):
    """
    Applies controlled modular exponentiation.
    p = [a, N] e.g., p = [7, 15]
    q = [control_qubits..., target_qubits...] where the last 4 qubits are the target.
    """
    if len(p) < 2:
        raise ValueError("Params 'p' must contain [a, N]")
    
    a = int(p[0])
    N = int(p[1])
    
    if N != 15:
        raise NotImplementedError("Currently only N=15 is supported (requires 4 target qubits).")
        
    num_controls = len(q) - 4
    if num_controls < 1:
        raise ValueError("Must provide at least 1 control qubit and exactly 4 target qubits (5+ total).")
        
    control_qubits = q[:num_controls]
    target_qubits = q[-4:]
    
    # In Shor's algorithm, we apply successive squares: a^(2^i) mod N
    for i, control_qubit in enumerate(control_qubits):
        power = 2**i
        gate = c_amod15(a, power)
        
        # Append the controlled gate. The first qubit is the control, the rest are target.
        qc.append(gate, [control_qubit] + target_qubits)
