# Create virtual environment
# venv = name of virtual environment, you can have a different name too.
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1 > python3 -m venv .venv

# Install setup tools
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1> pip3 install setuptools

# Activate the virutal environment
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1 > source .venv/bin/activate


# Install MLFlow
# This will create the MLFlow  files inside the 'mlops/.venv' directory = 'mlops/.venv/mlfow'
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1 > pip3 install mlflow

# Start the MLFlow user interface
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1 > mlflow ui


# Open the MLFlow user interface
# Default port is 5000
Browser > http://localhost:5000
OR
mlflow ui --port 7002



# Run the example
Terminal > /Users/ankur/backup/delta/sn/datascience/workspace/mlops/mlops1 > python3 experiment.py

# Check the run on the browser
Browser > http://localhost:7002

