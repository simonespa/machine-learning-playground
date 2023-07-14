- [Machine Learning Playground](#machine-learning-playground)
  - [Python prerequisites](#python-prerequisites)
  - [Getting started with PIP and Virtualenv](#getting-started-with-pip-and-virtualenv)
  - [Getting started with Anaconda](#getting-started-with-anaconda)
  - [Activate code formatting](#activate-code-formatting)
  - [Dependencies](#dependencies)
  - [Other Python libraries](#other-python-libraries)
  - [How to generate the requirements file](#how-to-generate-the-requirements-file)
  - [How to upgrade the dependencies](#how-to-upgrade-the-dependencies)
  - [Useful PIP commands](#useful-pip-commands)
  - [References](#references)

# Machine Learning Playground

A personal playground repository to practice machine learning and data science techniques and algorithms using the most popular Python libraries for the job. I also use this repo to collect notes and learnings while studying and practicing.

The notebook exercises are written with [Jupyter](https://jupyter.org/). You can also use [Kaggle](https://www.kaggle.com) or [Google Colab](https://colab.research.google.com) to edit them on the cloud.

## Python prerequisites

Make sure to have the latest stable version of `Python` 3.x and `pip` installed on your machine. Consider using [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python versions.

The desired Python version can now be set by running `pyenv install 3.n.m`, where `n` and `m` are the minor and patch version respectively. If you are not sure which version to install, you can check the available ones by running `pyenv install --list`.

## Getting started with PIP and Virtualenv

Install [Virtualenv](https://pypi.org/project/virtualenv/) in order to setup an isolated virtual environment to manage the Python project and dependencies (read this [installation](https://virtualenv.pypa.io/en/latest/installation.html) guide on how to).

You need to create a virtual environment with a clean installation of Python. The following command do so, by creating a folder called `.python` (which is automatically excluded from revision control) containing a vanilla installation of Python with just the initial depdendencies installed.

Create a virtual environment (only if you don't have an `.python` folder yet)

```sh
virtualenv .python
```

Enable the virtual environment

```sh
source .python/bin/activate
```

Check the python interpreter used is the one from the virtual environment

```sh
which python
```

Install the required dependencies

```sh
pip install -r requirements.txt
```

Start the development environment

```
jupyter notebook
```

or

```
jupyter lab
```

> NOTE: remember to deactivate the virtual environment by running the `deactivate` command once finished or if you switch project. If you don't do this and run `python` in another project through the same terminal session, you'll be running the same local version of Python with dependencies you may not want or need.

## Getting started with Anaconda

- Download and install [Anaconda](https://www.anaconda.com) on your machine
- Start the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/)
- Install and launch the Jupyter notebook or JupyterLab from the "home" tab

## Activate code formatting

Install and enable code formatting with [Black](https://pypi.org/project/black/) as a Jupyter extension

```
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter nbextension enable jupyter-black-master/jupyter-black
```

## Dependencies

This is the list of the main libraries included in the `requirements.txt` file.

- [Jupyter](https://jupyter.org)
- [JupyterLab](https://jupyter.org)
- [NumPy](https://numpy.org)
- [SciPy](https://scipy.org)
- [SymPy](https://www.sympy.org/en/index.html)
- [Pandas](https://pandas.pydata.org)
- [Pandas Profiling](https://pypi.org/project/pandas-profiling/)
- [Polars](https://www.pola.rs)
- [Statsmodels](https://www.statsmodels.org)
- [Matplotlib](https://matplotlib.org)
- [Seaborn](https://seaborn.pydata.org)
- [Altair](https://altair-viz.github.io)
- [Plotly](https://plotly.com/python)
- [Scikit-Learn](https://scikit-learn.org)
- [TensorFlow](https://www.tensorflow.org)
- [Keras](https://keras.io)
- [PyTorch](https://pytorch.org)

```
pip install notebook jupyterlab voila numpy scipy sympy pandas pandas_profiling polars statsmodels matplotlib seaborn altair plotly scikit-learn tensorflow torch torchvision torchaudio shap xgboost
```

## Tech Radar

Other interesting stuff worth investigating.

- [Caffe](https://caffe.berkeleyvision.org)
- [NLTK](https://www.nltk.org)
- [Theano](https://theano-pymc.readthedocs.io/en/latest)
- [Ggplot](https://ggplot2.tidyverse.org/index.html)
- [Dplyr](https://dplyr.tidyverse.org)
- [Tidyr](https://tidyr.tidyverse.org)
- [SpaCy](https://spacy.io)
- [Apache Spark](https://spark.apache.org)
- [mlflow](https://mlflow.org)

## How to generate the requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

## How to upgrade the dependencies

Replace all `==` symbols in the `requirements.txt` file with `>=`, then run

```
pip install -r requirements.txt --upgrade
```

once upgraded run

```
pip freeze > requirements.txt
```

### To try

```
pip install --upgrade --force-reinstall -r requirements.txt
```

or ignore installed packages and install the new ones:

```
pip install --ignore-installed -r requirements.txt
```

## Useful PIP commands

To list all the installed libraries in `site-packages`

```
pip list
```

To "show" the details of a specific library

```
pip show numpy
```

## References

- https://learnpython.org
- https://github.com/ageron/handson-ml
