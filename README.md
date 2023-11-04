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


dagshub for tracking experiments:

MLFLOW_TRACKING_URI=https://dagshub.com/mspatke/End-to-end-ML-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=mspatke \
MLFLOW_TRACKING_PASSWORD=8518bb307abed9989560d016d935f9a3af3abb4a \
python script.py


Eun this to export as env variable:

'''bash

export MLFLOW_TRACKING_URI=https://dagshub.com/mspatke/End-to-end-ML-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=mspatke

export MLFLOW_TRACKING_PASSWORD=8518bb307abed9989560d016d935f9a3af3abb4a

'''