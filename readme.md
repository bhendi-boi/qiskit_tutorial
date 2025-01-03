# Qiskit Tutorial

## How to install Qiskit

- First, create a python virtual environment

```bash
    python -m venv venv_name
```

- Activate virtual environment

```bash
    venv_name/Scripts/Activate.ps1
```

- Install qiskit with visualisation features

```bash
    pip install qiskit[visualization]
```

- Install qiskit-ibm-runtime package

```bash
    pip install qiskit-ibm-runtime
```

- Install qiskit-aer package

```bash
    pip install qiskit-aer
```

- If you want to open your python notebooks using jupyter, install jupyter package as well.

```bash
    pip install jupyter
```

- If you are using a text editor like VSCode, install corresponding jupyter plugin. Here is the [link](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) for VSCode jupyter plugin.

## Check installation

- Run [test.py](test.py) file to check whether your installation is done perfectly.
- You should see output similar to this.

```bash
    Qiskit version =  1.3.1
    Qiskit IBM runtim version =  0.34.0
    Qiskit Aer version =  0.15.1
```

## Sample Notebooks

- After you are done with the installation, open you can open sample notebooks provided.
- [Create Quantum circuit in qiskit](create_qc.ipynb)
- [Simulate Quantum circuit in qiskit](simulate_qc.ipynb)
- [State Vectors in qiskit](state_vector.ipynb)
- [Run your ckts on IBM's QPUs](run_qc.ipynb)
