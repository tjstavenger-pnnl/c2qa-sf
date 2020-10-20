# c2qa-sf

NQI C2QA project to simulate circuits using Strawberry Fields.

## Install

Use a Python virtual environment to install compatible version of Strawberry Fields.

```bash
git clone https://github.com/tjstavenger-pnnl/c2qa-sf.git
cd c2qa-sf
./install-dependencies.sh
```

## Activate Virtual Environment

Before using c2qa-sf, first install the depencies (as above) and then activate the Python virtual environment.

```bash
cd <path/to/c2qa-sf>
source venv/bin/activate
```

## Run the code

After activating the Python virtual environment, run the scripts. For example:

```bash
cd <path/to/c2qa-sf>
python3 -m c2qa.script.py
```
