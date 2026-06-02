import json
import os
from shared.interfaces import CustomGateDef

"""
    {
        "name": "MY_BELL_GATE",
        "num_qubits": 2,
        "instructions": [
            {"name": "H", "qubits": [0]},
            {"name": "CX", "qubits": [0, 1]}
        ]
    }
"""
MAIN_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(MAIN_DIR, 'data')
GATES_FILE = os.path.join(DATA_DIR, 'custom_gates.json')

def init_data_file():
    if not os.path.exists(GATES_FILE):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(GATES_FILE, 'w') as f:
            json.dump([], f)

def get_all_gates():
    init_data_file()
    with open(GATES_FILE, 'r') as f:
        return json.load(f)

def get_custom_gate(name: str) -> CustomGateDef:
    init_data_file()
    gates = get_all_gates()
    for gate in gates:
        if gate['name'] == name:
            return CustomGateDef.from_dict(gate)
    return None

def delete_custom_gate(name: str):
    init_data_file()
    gates = get_all_gates()
    gates = [g for g in gates if g['name'] != name]
    with open(GATES_FILE, 'w') as f:
        json.dump(gates, f, indent=4)

def save_custom_gate(gate: CustomGateDef):
    init_data_file()
    gates = get_all_gates()
    gates = [g for g in gates if g['name'] != gate.name]
    gates.append(gate.model_dump())
    with open(GATES_FILE, 'w') as f:
        json.dump(gates, f, indent=4)