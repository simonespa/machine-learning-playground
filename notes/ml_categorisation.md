# Machine Learning Categorisation

Machine learning models, techniques and approaches can be classified according to different categorisation characteristics.

## Type of tasks

- Predictive: the model is trained on the data to predict an outcome
- Descriptive: the model spots patterns, correlation, structure in the data, and it also visualise it with transformations
- Prescriptive: the model recommends actions, optimisations

## Training approachs

- Supervised
  - Regression
  - Classification
- Reinforcement Learning
- Unsupervised
- Semi-supervised
- Self-supervised

Supervised is used for predictive tasks: classification and regression.

Unsupervised is used for descriptive tasks: clustering, visualisation, feature reduction

Semi-supervised combines both **supervised** and **unsupervised techniques**. It's used for predictive tasks when labelling data is expensive, difficult, almost impossible or even requires domain expertise which may not be available. The dataset is partially labelled, but not fully.

Self-supervised methods like autoencoders are truly unsupervised. They don't need an external ground truth, but they derive the ground truth from the underlying structure (latent features) of the input data. They still use a cost function during training.

References:

- https://www.ibm.com/topics/semi-supervised-learning
- https://towardsdatascience.com/supervised-semi-supervised-unsupervised-and-self-supervised-learning-7fa79aa9247c

## Type of prediction

- Regression
- Classification

Type of classifications: https://machinelearningmastery.com/types-of-classification-in-machine-learning/

## Type of classifications

- Binary
- Multi-Class
- Multi-Label
- Imbalanced

Reference: https://machinelearningmastery.com/types-of-classification-in-machine-learning/

## Classification approach

- Generative
- Discriminative

## Prediction approach

- Deterministic
- Probabilistic (a.k.a. stochastic)

Deterministic models produce a single prediction for a given input without providing any information about the uncertainty of it.

Probabilistic or stochastic models are trained to optimize a probabilistic objective function. These models provide a probabilistic characterization of the uncertainty in their predictions.
