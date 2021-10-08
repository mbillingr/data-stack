Tech Stack for Data Analysis and Machine Learning
=================================================

Overview
--------

The tech stack is centered around data processing with Python (numpy, scipy, pandas, ...).
We will use the following tools:
- `Dask`: out of memory and parallel processing of numpy arrays and pandas dataframes.
- `Prefect`: defining and orchestrating data processing pipelines.
- `MLflow`: tracking, model registry/deployment
- `Docker`: container management


Installation
------------

### Python environment

Install dask, numpy, scipy, pandas, etc. in a fresh Python environment.

TODO: ensure same environment local and in Dask workers


### Prefect

Install `prefect` in the local Python environment, according to it's [
installation instructions](https://docs.prefect.io/core/getting_started/install.html).

Start a prefect server locally with 
```
$> prefect server start --use-volume
```

Start a local agent in its own terminal window
```
prefect agent local start
```



### MLflow

Start a local mlflow tracking server
```
$> start.bat
```

This setup was inspired by https://towardsdatascience.com/deploy-mlflow-with-docker-compose-8059f16b6039.