* [Getting Started](#getting-started)
  + [Setup the virtual environment](#setup-the-virtual-environment)
  + [Install the dependencies](#install-the-dependencies)
* [How to generate the requirements file](#how-to-generate-the-requirements-file)
* [How to run an example](#how-to-run-an-example)
* [Useful PIP commands](#useful-pip-commands)
* [Python Libraries](#python-libraries)

# Machine Learning Playground

A playground repository to practice machine learning and data science techniques and algorithms using the most popular Python libraries for the job.

The notebook exercises are written with [Jupyter](https://jupyter.org/). You can also use [Kaggle](https://www.kaggle.com) or [Google Colab](https://colab.research.google.com) to edit them on the cloud.

## Getting started with Virtualenv

Make sure to have the latest Python 3.x installed on your machine. Consider using [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python versions.

This section will guide you through the setup of an isolated Python environment for this project.

* Install [Virtualenv](https://pypi.org/project/virtualenv/) (read the [installation](https://virtualenv.pypa.io/en/latest/installation.html) documentation)
* Create a new virtual environment by running `virtualenv .env`
* Enable your virtual environment by running `source .env/bin/activate` (or `. .env/bin/activate`).
* Confirm you’re using the virtual environment by checking the location of your Python interpreter `which python`
* Install the dependencies `pip install -r requirements.txt`
* Start the development environment by running `jupyter notebook`
* Once you finish with this project, you can disable the virtual environment by running `deactivate`

## Getting started with Anaconda

* Download and install [Anaconda](https://www.anaconda.com)
* Launch the Jupyter notebook or JupyterLab from the main console

## Dependencies

This is the list of libraries included in the `requirements.txt` file.

* [Jupyter](https://jupyter.org)
* [JupyterLab](https://jupyter.org)
* [NumPy](https://numpy.org)
* [Pandas](https://pandas.pydata.org)
* [SciPy](https://scipy.org)
* [Matplotlib](https://matplotlib.org)
* [Seaborn](https://seaborn.pydata.org)
* [Scikit-Learn](https://scikit-learn.org)
* [TensorFlow](https://www.tensorflow.org)
* [PyTorch](https://pytorch.org)
* [Keras](https://keras.io)

```
notebook jupyterlab numpy pandas scipy matplotlib seaborn scikit-learn tensorflow torch torchvision torchaudio
```
## Other Python libraries

This is a list of other useful Python libraries not included in this project.

* [Caffe](https://caffe.berkeleyvision.org)
* [Theano](https://theano-pymc.readthedocs.io/en/latest)
* [Ggplot](https://ggplot2.tidyverse.org/index.html)
* [Dplyr](https://dplyr.tidyverse.org/)
* [Tidyr](https://tidyr.tidyverse.org/)

## How to generate the requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

## Useful PIP commands

To list all the installed libraries in `site-packages`

```
pip list
```

To "show" the details of a specific library

```
pip show requests
```
