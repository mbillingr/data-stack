import mlflow
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Local

from processing import config


@task
def say_hello():
    mlflow.set_tracking_uri("http://localhost:80")
    mlflow.set_experiment("/hello-world")
    with mlflow.start_run():
        mlflow.set_tag("MSG", "HELLO!")


with Flow(
    "hello-docker",
    storage=Local(path="/app/workflow/flow.py", stored_as_script=True),
    run_config=DockerRun(image="prefect_example:latest"),
) as flow:
    say_hello()


if __name__ == "__main__":
    flow.register("hello-world")
