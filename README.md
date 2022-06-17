- [Getting Started](#getting-started)
  * [Setup the virtual environment](#setup-the-virtual-environment)
  * [Install the dependencies](#install-the-dependencies)
  * [How to generate the requirements file](#how-to-generate-the-requirements-file)
  * [How to run an example](#how-to-run-an-example)
  * [Useful PIP commands](#useful-pip-commands)
- [Machine Learning](#machine-learning)

# Machine Learning Playground

A playground repository to practice machine learning, data modelling and data visualisation.

## Getting Started

I'm currently using [pyenv](https://github.com/pyenv/pyenv) to manage the Python version on my terminal.

This section will guide you through the setup of a Python virtual environment for this specific project.

The use of a virtual environment allows you to isolate the project and its dependencies from the main Python installation.

### Setup the virtual environment

Create a virtual environment with `virtualenv`

```
virtualenv .env
```

and activate it

```
source .env/bin/activate
```

or

```
. env/bin/activate
```

You can confirm you’re using the virtual environment by checking the location of your Python interpreter

```
which python
```

If you want to switch to another project or generally speaking leave your current virtual environment, run

```
deactivate
```

### Install the dependencies

Install the required dependencies

```
pip install -r requirements.txt
```

### How to generate the requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

### How to run an example

Let's say there is an `example.py` module within the `exercises` folder that defines a `hello` function.

Open the Python interpreter

```
python
```

import the function you want to run from its module

```py
from exercises.example import hello
```

execute the function

```py
hello()
```

Modules don't have any "main" execution. If you were to run a file directly, you would need to add the following to it

```py
if __name__ == '__main__':
  hello()
```

and then run

```
python exercises/example.py
```

### Useful PIP commands

To list all the installed libraries in `site-packages`

```
pip list
```

To "show" the details of a specific library

```
pip show requests
```

## Machine Learning

Libraries to practice with:
* NumPy
* SciPy
* scikit-learn
* pandas
* TensorFlow
* PyTorch
* Matplotlib
* Seaborn
* Dplyr
* Tidyr
* Ggplot

Machine learning algorithms to practice:
* Linear Regression
* Logistic Regression
* SVM
* KNN
* Decision Trees
* K Means Clustering
