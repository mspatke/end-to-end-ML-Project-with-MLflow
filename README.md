# End-to-end-ML-Project-with-MLflow

## Workflows


1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update Configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Upadte  app.py


## Steps for Model Evaluation Stage
dagshub for tracking experiments:

MLFLOW_TRACKING_URI=https://dagshub.com/mspatke/End-to-end-ML-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=mspatke \
MLFLOW_TRACKING_PASSWORD=8518bb307abed9989560d016d935f9a3af3abb4a \
python script.py


1) Run this to export as env variable while running python script through terminal:

'''bash

export MLFLOW_TRACKING_URI=https://dagshub.com/mspatke/End-to-end-ML-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=mspatke

export MLFLOW_TRACKING_PASSWORD=8518bb307abed9989560d016d935f9a3af3abb4a

'''

2) If you are running code in jupyter notebook, then set below env variable in notebook

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/mspatke/End-to-end-ML-Project-with-MLflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "mspatke"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "8518bb307abed9989560d016d935f9a3af3abb4a"


