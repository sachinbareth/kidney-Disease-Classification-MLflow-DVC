'''
# kidney-Disease-Classification-MLflow-DVC


## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?

### STEPS:
clone the repository

```bash
https://github.com/sachinbareth/kidney-Disease-Classification-MLflow-DVC
```

### STEP 01- Create a conda environment after the repository

```bash
conda create -n cnncls python=3.8 -y
```
```bash
conda activate cnncls
```
### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```





```bash
# Finally run the following command
python app.py
```
Now,

```bash
open up you local host and port
```
# MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

'''
### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/sachinbareth/kidney-Disease-Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=sachinbareth \
MLFLOW_TRACKING_PASSWORD=5ed04e79885a1204e0f15fc08d9027377a1d667e \
python script.py

Run this to export as env variables:

```bash


export MLFLOW_TRACKING_URI=https://dagshub.com/sachinbareth/kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=sachinbareth 

export MLFLOW_TRACKING_PASSWORD=5ed04e79885a1204e0f15fc08d9027377a1d667e
```





```bash
# Finally run the following command
python app.py
```
Now,
```bash
open up you local host and port
```
### MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)



##### cmd
-mlflow ui
### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/sachinbareth/kidney-Disease-Classification-MLflow-DVC.mlflow
MLFLOW_TRACKING_USERNAME=sachinbareth
MLFLOW_TRACKING_PASSWORD=5ed04e79885a1204e0f15fc08d9027377a1d667e
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/sachinbareth/kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=sachinbareth 

export MLFLOW_TRACKING_PASSWORD=5ed04e79885a1204e0f15fc08d9027377a1d667e
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag