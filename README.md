# Machine Learning Playground

This is a personal playground repository to practice machine learning, data science techniques and algorithms using the most popular Python libraries for the job. I also use this repo to collect and organise notes and learnings while studying and practicing.

The notebook exercises are written with [Jupyter](https://jupyter.org/). You can also use [Kaggle](https://www.kaggle.com) or [Google Colab](https://colab.research.google.com) to edit them on the cloud.

- [Notice](#notice)
- [Credits](#credits)
- [Python prerequisites](#python-prerequisites)
- [Getting started with PIP and Virtualenv](#getting-started-with-pip-and-virtualenv)
- [Getting started with Anaconda](#getting-started-with-anaconda)
- [Activate code formatting](#activate-code-formatting)
- [Dependencies](#dependencies)
- [Tech Radar](#tech-radar)
- [How to generate the requirements file](#how-to-generate-the-requirements-file)
- [How to upgrade the dependencies](#how-to-upgrade-the-dependencies)
  - [To try](#to-try)
- [Useful PIP commands](#useful-pip-commands)
- [References](#references)

## Notice

📚 The resources contained in this repository are notes written down while studying topics of Machine Learning and Data Science and exercises I write to practice. They reflect my understanding of the topic and as such, **they are not meant to be used as an authoritative source of information and/or reference documentation about the subject they refer to**.

🗒️ I take notes by summarising the concepts I read and/or watch. I also write stuff to conceptualise my own understanding of a broader topic or my thoughts about it. I even attempt to jot down ideas.

📦 I've built this repo mainly for me to have a place where to store my notes so that I can revise and practice. I made it public because it doesn't hurt to have other people reading them in the hope it could be useful in the process. With this in mind, there are plenty of other excellent resources out there, more complete and accurate than this, so again, here I am.

⚠️ Feel free to use these resources as you wish, according to the [LICENSE](./LICENSE), with the knowledge that inaccuracy may be likely. So, please use these resources with a pinch of salt, by knowing that they could contain mistakes. Please, always compare and integrate the concepts you read with other material you have access to, in order to make sure you are not inadvertently taking only my word for it.

⛔ Any mistake, blunder, typo, inaccuracy - if present - is there in good faith. No hard feelings. If you care enough about this work though, please report any of the above to me by [raising an issue](https://github.com/simonespa/machine-learning-playground/issues) so that I can fix it. Even better, you can also [raise a Pull Request](https://github.com/simonespa/machine-learning-playground/pulls) if you like to propose a fix yourself.

❤️ If you feel grateful about these resources and feel that this work may have helped you in any form or shape with your study, consider crediting this work as a way to say thank you 😊

## Credits

I started to be interested in topics gravitating the Artificial Intelligence world since my academic studies at the [Università della Calabria](https://www.unical.it), when I was then studying topics like Intelligent Systems, Answer-Set Programming and this thing called Data Mining at the [Department of Mathematics and Informatics](https://demacs.unical.it/)

I'm currently attending a Level 7 staff apprenticeship in AI and Data Science with [Cambridge Spark](https://www.cambridgespark.com/data-apprenticeships/level-7-ai-data-science) at the [BBC](https://www.bbc.co.uk/).

I'm also expanding these concepts and beyond by reading and watching further material available on the internet (papers, resources, video).

I'd like to give a shout out to [StatQuest](https://www.youtube.com/@statquest) with [Josh Starmer](https://www.linkedin.com/in/joshua-starmer-phd). It's an excellent YouTube channel with a vast and "clearly explained" catalogue of concepts spanning from Statistics to Data Science and Machine Learning. I can personally say that I'm now able to grasp concepts like Encoder-Decoder and Transformer architecture to give an example thanks to Josh. We don't know each other nor I get compensated to say this, so please, "checkout the quest" and subscribe, it's worth your time.

I also attended courses on [LinkedIn Learning](https://www.linkedin.com/learning), [Pluralsight](https://www.pluralsight.com) and [Coursera](https://www.coursera.org) as well as training courses provided by the BBC, spanning from introduction to ML to TensorFlow and Keras to data manipulation and visualisation with Pandas, Matplotlib and Seaborn.

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

## Dependencies

This is the list of the main DS libraries included in the `requirements.txt` file.

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
- [XGBoost](https://xgboost.readthedocs.io)

The full list of dependencies directly installed via PIP is the following:

```
pip install notebook jupyterlab ipywidgets jupyterlab-code-formatter voila numpy scipy sympy pandas pandas_profiling polars statsmodels matplotlib seaborn altair plotly scikit-learn tensorflow torch torchvision torchaudio xgboost awswrangler black isort
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

to lock the newly downloaded versions to the requirements file

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
