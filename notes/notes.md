# Notes

## Steps

1. Understand the problem. What's the current solution and what's business objective?
2. Decide whether this is something worth employing ML or a less sofisticated automation job.
3. If positive, choose the right approach by answering few questions

- Is it supervised, unsupervised or reinforcement learning?
- Is it a classification or regression task?
- Is it a batch, online or incremental learning?

4. Select a performance measure for the chosen approach

- Check if the class is imbalanced if is a classification problem
- Decide what to include in the GridSearch

* Dataset split ratio
* Whether to use stratified or not
* Missing data imputation strategy
* Feature engineering
* Categorical encoding
* Hyperparameters

## Data preparation

- Deal with missing data
  - Remove the instances with missing data
  - Remove the columns that have missing data
  - Fill the missing data with a value (zero, the mean, etc.)
- Categorical feature encoding
- Feature selection (choose the best predictors)
  - train faster
  - reduce model complexity (easier to interpret)
  - improves prediction accuracy
  - reduces overfitting
- Feature engineering (create new features, combine existing one)
- Feature scaling
- With classification problems, find the correlation of the class with other features.

## Feature selection

Via "univariate selection". Statistical tests (e.g. chi-squared test) that select independent features that have the strongest relationship with the target feature.

Via "feature importance" that gives a score for each feature of the dataset. The higher the score the more important or relevant is the feature to in respect of the target one. This is built-in with the tree-based classifiers such as Random Forest and Extra Tree.

Via "Correlation Matrix Heatmap. This shows how features are related to each other and as a consequence with the target one.

High correlation between two features means that they convey the same information. One of them must be removed. If the correlation is with the target feature, that's good, the feature is a strong predictor.

## Multiclass Classification

Multiclass Classifiers (a.k.a. Multinomial Classifiers) can distinguish between more than two classes.

## Multicollinearity

Decision trees and boosted trees algorithms are immune to multicollinearity by nature. When they decide to split, the tree will choose only one of the perfectly correlated features.

Logistic Regression or Linear Regression are not immune to Multicollinearity problems and you should fix it before training the model.

Fix: you can either remove the feature or use dimension reduction algorightm such as Principle Component Analysis (PCA).

## Algorithms

Random Forest classifiers or naive Bayes classifiers are capable of handling multiple classes directly.
Support Vector Machine classifiers or Linear classifiers are strictly binary classifiers.
You can also use multiple binary classifiers to perform multiclass classification

## Holdout validation and Testing

1. Train multiple models with various hyperparameters on the reduced training set (i.e., the full training set minus the validation set)
2. Select the model/hyperparameters that performs best on the validation set for each different algorithm
3. Train the best model for each algorithm on the full training set (including the validation set) and this gives you the final models
4. Lastly, evaluate the final models on the test set to get an estimate of the generalization error and choose the one that performs best

## Correlation Coefficient

The correlation coefficient only measures linear correlations but misses nonlinear relationships.
