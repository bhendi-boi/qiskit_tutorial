# Qiskit Tutorial

## Installation for this Tutorial

### Prerequsites

We recommend you do this before attending the session.

- Download [Python 3.x](https://www.python.org/downloads/) on your machine.
- Download this [github repo](https://github.com/bhendi-boi/qiskit_tutorial) by hitting the code button followed by download zip button.
  ![images/github_download.png](images/github_download.png)
- Unzip the folder and open it using a text editor or file explorer. We recommend you [download Visual Studio Code](https://code.visualstudio.com/download) and open this folder in VS Code.
  ![images/vscode_open_folder.png](images/vscode_open_folder.png)

- Finally, download Jupyter extension for VS Code.
  ![images/download_extension.png](images/download_extension.png)

### Installation

- Now we can download Qiskit and some addons
- Open the terminal in VS Code. You can also use the short hand `` Ctrl + Shift + `  ``.
  ![images/open_terminal.png](images/open_terminal.png)
- If it opens command prompt, change it to powershell.
  ![images/change_to_powershell_1.png](images/change_to_powershell_1.png)
  ![images/change_to_powershell_2.png](images/change_to_powershell_2.png)
- Once you have changed it to powershell, you will see `Powershell` instead of `cmd`.
- I have created a virtual environment beforehand. Activate it by running this command in the terminal.

```
    venv/Scripts/Activate.ps1
```

If you run into any issues here, refer to [this website](https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts).

![images/activate_venv.png](images/activate_venv.png)

- Run this command in the same powershell window to start downloading required packages.

```
    pip install -r requirements.txt
```

### Check installation

- Run [test.py](test.py) file to check whether your installation is done perfectly. Run this command in the same powershell window to start downloading required packages.

```
    python test.py
```

- You should see output similar to this.

```bash
    Qiskit version =  1.3.1
    Qiskit IBM runtim version =  0.34.0
    Qiskit Aer version =  0.15.1
```

If you get this output, you are ready for the session.

## Sample Notebooks

- After you are done with the installation, open you can open sample notebooks provided.
- [Create Quantum circuit in qiskit](create_qc.ipynb)
- [Simulate Quantum circuit in qiskit](simulate_qc.ipynb)
- [State Vectors in qiskit](state_vector.ipynb)
- [Run your ckts on IBM's QPUs](run_qc.ipynb)

## How to install Qiskit for new projects

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
