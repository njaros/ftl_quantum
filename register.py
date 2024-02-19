import os
from qiskit_ibm_provider import IBMProvider


def register():
    IBMProvider.save_account(token=os.environ["QISKIT_IBM_TOKEN"])


if __name__ == "__main__":
    register()
