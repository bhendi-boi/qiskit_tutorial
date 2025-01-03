from qiskit.version import get_version_info as qiskit_version
from qiskit_ibm_runtime.version import get_version_info as ibm_runtime_version
from qiskit_aer.version import get_version_info as qiskit_aer_version


print("Qiskit version = ", qiskit_version())
print("Qiskit IBM runtim version = ", ibm_runtime_version())
print("Qiskit Aer version = ", qiskit_aer_version())
