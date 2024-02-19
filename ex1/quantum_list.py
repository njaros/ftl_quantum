import logging
from qiskit_ibm_provider import IBMProvider
logging.getLogger('qiskit_ibm_provider').setLevel(logging.WARNING)


def quantum_list():
    provider = IBMProvider()
    backends = provider.backends()
    simulator_backend = provider.get_backend('ibmq_qasm_simulator')
    print(backends)
    print(simulator_backend)


if __name__ == "__main__":
    quantum_list()
