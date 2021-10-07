from prefect import task, Flow
import mlflow


@task
def say_hello():
    mlflow.set_tracking_uri("http://localhost:80")
    mlflow.set_experiment("/hello-world")
    with mlflow.start_run():
        mlflow.set_tag('MSG', 'HELLO!')


with Flow("say-hello") as flow:
    say_hello()


if __name__ == '__main__':
    flow.register("hello-world")
