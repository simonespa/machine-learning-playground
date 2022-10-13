- [Machine Learning Playground](#machine-learning-playground)
  * [Getting started with Virtualenv](#getting-started-with-virtualenv)
  * [Getting started with Anaconda](#getting-started-with-anaconda)
  * [Dependencies](#dependencies)
  * [Other Python libraries](#other-python-libraries)
  * [How to generate the requirements file](#how-to-generate-the-requirements-file)
  * [Useful PIP commands](#useful-pip-commands)

# Machine Learning Playground

A playground repository to practice machine learning and data science techniques and algorithms using the most popular Python libraries for the job.

The notebook exercises are written with [Jupyter](https://jupyter.org/). You can also use [Kaggle](https://www.kaggle.com) or [Google Colab](https://colab.research.google.com) to edit them on the cloud.

## Getting started with Virtualenv

Make sure to have the latest Python 3.x installed on your machine. Consider using [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python versions.

This section will guide you through the setup of an isolated Python environment for this project.

Install [Virtualenv](https://pypi.org/project/virtualenv/) (read the [installation](https://virtualenv.pypa.io/en/latest/installation.html) documentation)

Create a new virtual environment

```
virtualenv .env
```

Enable the virtual environment

```
source .env/bin/activate
```

or

```
. .env/bin/activate
```

Confirm you’re using the virtual environment by checking the location of your Python interpreter

```
which python
```

Install the dependencies

```
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

Once you finish with this project, you can disable the virtual environment

```
deactivate
```

## Getting started with Anaconda

* Download and install [Anaconda](https://www.anaconda.com) on your machine
* Start the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/)
* Install and launch the Jupyter notebook or JupyterLab from the "home" tab

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

## How to upgrade the dependencies

Replace all `==` symbols in the `requirements.txt` file with `>=`, then run

```
pip install -r requirements.txt --upgrade
```

once upgraded run

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
pip show numpy
```
