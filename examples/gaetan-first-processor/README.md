# Gaetan First Orca Processor

This example validates a complete Orca execution chain:

window.py -> Orca Core -> processor.py -> algorithm execution

## What it does

- Registers a Python processor named `ml`
- Defines a time window named `Every30Second`
- Emits a window every 30 seconds
- Triggers the `LinearRegression` algorithm
- Returns a simple structured result

## Run

Terminal 1:

```bash
cd ~/Documents/myOrcaProcessor
source .venv/bin/activate
python processor.py
cat > examples/gaetan-first-processor/README.md <<'MD'
