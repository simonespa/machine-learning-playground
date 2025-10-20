# PySpark

## Docker compose

Run the service with docker compose

```
docker compose up --build
```

## Docker interactive

You can run the container interactively, mounting the current directory with the container work directory

```
docker run --name jupyter-pyspark --rm -p 8080:8888 -v "$(pwd):/home/jovyan/work" quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='lallallero'
```

or you can choose to mount a Docker volume

```
docker run --name jupyter-pyspark --rm -p 8080:8888 -v jupyter-pyspark:/home/jovyan quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='lallallero'
```

## Run jupyter

Then open http://localhost:8080/lab?token=b4847fad9ad1693c7912616e1714ac5d4051c18f

## Reference
- https://docs.docker.com/guides/jupyter/
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
- https://github.com/jupyter/docker-stacks/blob/main/images/pyspark-notebook/Dockerfile
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html
