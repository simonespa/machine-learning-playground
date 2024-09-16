# Machine Learning Playground

This is a personal playground repository to practice machine learning and data science techniques and algorithms using the most popular Python libraries for the job. I use this repo to collect and organise notes for a quick reference of things I learned during my studies.

The notebooks are written using [Jupyter](https://jupyter.org/) on my local machine. You can also use [Kaggle](https://www.kaggle.com) or [Google Colab](https://colab.research.google.com) to edit them on the cloud.

- [Notice](#notice)
- [Credits](#credits)
- [Python prerequisites](#python-prerequisites)
- [Getting started with PIP and Virtualenv](#getting-started-with-pip-and-virtualenv)
- [Getting started with Anaconda](#getting-started-with-anaconda)
- [Dependencies](#dependencies)
- [Tech Radar](#tech-radar)
- [How to generate the requirements file](#how-to-generate-the-requirements-file)
- [How to upgrade the dependencies](#how-to-upgrade-the-dependencies)
- [Useful PIP commands](#useful-pip-commands)
- [References](#references)

## Notice

📚 The resources contained in this repository are notes written down while studying topics of Machine Learning and Data Science and exercises I wrote to practice. They reflect my understanding of the topic and as such, **they are not meant to be used as an authoritative source of information and/or reference documentation about the subject they refer to**.

🗒️ I take notes by summarising the concepts I read and/or watch. I also put together pieces from different materials I consult about a specific topic. I write stuff to conceptualise my own understanding of a broader topic or my thoughts about it. I even attempt to jot down ideas.

📦 I've built this repository mainly for myself, to have a place where to collect my notes and to practice. I made it public because it doesn't hurt to give other people access to it, in the hope it could be useful in the process.

⚠️ Feel free to use these resources as you wish - according to the [LICENSE](./LICENSE) - with the knowledge that inaccuracy may be likely. So, please use these resources with a pinch of salt, by knowing that they could contain mistakes. Please, always compare and integrate the concepts you read from this repo with other material you have access to (there is plenty of other excellent resources out there, more complete and accurate than this), in order to make sure you are not inadvertently taking only my word for it.

⛔ Any mistake, blunder, typo, inaccuracy - if present - is there in good faith. No hard feelings. If you care enough about this work though, please report any of the above to me by [raising an issue](https://github.com/simonespa/machine-learning-playground/issues) so that I can fix it. Even better, you can also [raise a Pull Request](https://github.com/simonespa/machine-learning-playground/pulls) if you like to propose a fix yourself.

❤️ If you feel grateful about this collection and feel that this work may have helped you even so slightly in any form or shape with your study, consider crediting this repo as a way to say thank you 😊

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Machine Learning Playground</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/simonespa/machine-learning-playground" property="cc:attributionName" rel="cc:attributionURL">Simone Spaccarotella</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Credits

I started to be interested in topics gravitating the Artificial Intelligence world since my academic studies at the [Università della Calabria](https://www.unical.it), when I was then studying topics like Intelligent Systems, Answer-Set Programming and this thing called Data Mining at the [Department of Mathematics and Informatics](https://demacs.unical.it/)

I'm currently attending a Level 7 staff apprenticeship in AI and Data Science with [Cambridge Spark](https://www.cambridgespark.com/data-apprenticeships/level-7-ai-data-science) at the [BBC](https://www.bbc.co.uk/).

I'm also expanding these concepts and beyond by reading and watching further material available on the internet (papers, resources, video).

I'd like to give a shout out to [StatQuest](https://www.youtube.com/@statquest) with [Josh Starmer](https://www.linkedin.com/in/joshua-starmer-phd). It's an excellent YouTube channel with a vast and "clearly explained" catalogue of concepts spanning from Statistics to Data Science and Machine Learning. For example, I can personally say that I'm now able to grasp the main concepts behind Encoder-Decoder and Transformer architectures thanks to Josh. We don't know each other nor I get compensated to say this, so please, "checkout the quest" and subscribe, it's worth your time.

I also attended courses on [LinkedIn Learning](https://www.linkedin.com/learning), [Pluralsight](https://www.pluralsight.com) and [Coursera](https://www.coursera.org) as well as training courses provided by the BBC, spanning from introduction to ML to TensorFlow and Keras to data manipulation and visualisation with Pandas, Matplotlib and Seaborn.

## Python prerequisites

Make sure to have a suitable stable version of `Python` 3.x and `pip` installed on your machine. Consider using [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python versions.

The desired Python version can be set by running `pyenv install 3.n.m`, where `n` and `m` are the minor and patch version respectively. If you are not sure which version to install, you can check the available ones by running `pyenv install --list`.

> Please read [Python Version](#python-version) section to check what's the latest python version compatible with the installed packages.

## Getting started with PIP and Virtualenv

Install [Virtualenv](https://pypi.org/project/virtualenv/) in order to setup an isolated virtual environment to manage the Python project and dependencies (read this [installation](https://virtualenv.pypa.io/en/latest/installation.html) guide on how to).

You need to create a virtual environment with a clean installation of Python. The following command do so, by creating a folder called `ml-playground` (which is automatically excluded from revision control) containing a vanilla installation of Python with just the initial depdendencies installed.

Create a virtual environment (only if you don't have an `ml` folder yet)

```sh
virtualenv ml
```

Enable the virtual environment

```sh
source ml/bin/activate
```

Check the python interpreter used is the one from the virtual environment

```sh
which python
```

Install the required dependencies

```sh
pip install -r requirements.txt
```

Download the [English pipeline for Spacy](https://spacy.io/models/en#en_core_web_md)

```sh
python -m spacy download en_core_web_md
```

Start the development environment

```sh
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
- [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/stable)
- [NumPy](https://numpy.org)
- [SciPy](https://scipy.org)
- [SymPy](https://www.sympy.org/en/index.html)
- [Statsmodels](https://www.statsmodels.org)
- [Pandas](https://pandas.pydata.org)
- [Polars](https://www.pola.rs)
- [Dask](https://www.dask.org)
- [Dask ML](https://ml.dask.org)
- [Matplotlib](https://matplotlib.org)
- [Seaborn](https://seaborn.pydata.org)
- [Plotly](https://plotly.com/python)
- [Scikit-Learn](https://scikit-learn.org)
- [TensorFlow](https://www.tensorflow.org)
- [Keras](https://keras.io)
- [PyTorch](https://pytorch.org)
- [XGBoost](https://xgboost.readthedocs.io)
- [LightGBM](https://lightgbm.readthedocs.io/en/stable) and [LightGBM Python Package](https://github.com/microsoft/LightGBM/tree/master/python-package)
- [CatBoost](https://catboost.ai/)
- [Prophet](https://facebook.github.io/prophet/)
- [AWS Wrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/)
- [Sagemaker](https://sagemaker.readthedocs.io/en/stable/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- [Optuna](https://optuna.org)
- [Imbalanced Learn](https://imbalanced-learn.org/stable/)
- [SHAP](https://shap.readthedocs.io/en/latest/)
- [PyWhy](https://www.pywhy.org/)
- [SpaCy](https://spacy.io)
- [NLTK](https://www.nltk.org/)
- [Gensim](https://radimrehurek.com/gensim/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/index)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/en/index)
- [MLFlow](https://mlflow.org/)
- [AutoKeras](https://autokeras.com/)

The full list of dependencies directly installed via PIP is the following:

```
pip install flake8 black isort split-folders rdflib notebook jupyterlab ipywidgets voila numpy scipy sympy statsmodels pandas polars 'dask[complete]' distributed 'dask-ml[complete]' ydata-profiling sweetviz autoviz lux matplotlib seaborn plotly scikit-learn tensorflow tensorflow_datasets keras-tuner torch torchvision torchaudio xgboost lightgbm catboost prophet awswrangler sagemaker pyspark pyarrow optuna imbalanced-learn category_encoders shap lime anchor-exp dowhy econml causal-learn spacy gensim nltk lightfm transformers 'diffusers[torch]' mlflow autokeras
```

### Python Version

Read [Tensorflow Software Requirements](https://www.tensorflow.org/install/pip#software_requirements) to check the latest Python version compatibility

## Tech Radar

Technology worth investigating:

- [Apache Spark](https://spark.apache.org)
- [mlflow](https://mlflow.org)
- [Nvidia AI (RAPIDS)](https://developer.nvidia.com/rapids)
  - [GitHub](https://github.com/rapidsai)
  - [Rapids.ai](https://rapids.ai/)
  - [Triton Inference Server](https://github.com/triton-inference-server)
- [Nvidia Merlin](https://developer.nvidia.com/merlin)
  - [GitHub](https://github.com/NVIDIA-Merlin)

## How to generate the requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

## How to upgrade the dependencies

To upgrade the dependencies we first need to replace all `==` symbols in the `requirements.txt` file with `>=`, so that we unlock the version and allow PIP to download the latest. We then run the upgrade command, and finally freze the packages again with the `==` symbol to lock the latest versions.

Unlock the current versions

```sh
sed -i '' 's/[~=]=/>=/' requirements.txt
```

Upgrade to the latest versions

```sh
pip install --upgrade -r requirements.txt
```

Lock the latest versions

```sh
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

## References

- https://learnpython.org
- https://github.com/ageron/handson-ml3
