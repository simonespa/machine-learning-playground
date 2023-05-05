j# Notes

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

## Feature scaling

### Min-max (a.k.a normalization)

Min-max scaling (many people call this normalization) is quite simple: values are
shifted and rescaled so that they end up ranging from 0 to 1. We do this by subtract‐
ing the min value and dividing by the max minus the min. Scikit-Learn provides a
transformer called MinMaxScaler for this. It has a feature_range hyperparameter
that lets you change the range if you don’t want 0–1 for some reason.

### Standardization

Standardization is quite different: first it subtracts the mean value (so standardized
values always have a zero mean), and then it divides by the variance so that the result‐
ing distribution has unit variance. Unlike min-max scaling, standardization does not
bound values to a specific range, which may be a problem for some algorithms (e.g.,
neural networks often expect an input value ranging from 0 to 1). However, standard‐
ization is much less affected by outliers. For example, suppose a district had a median
income equal to 100 (by mistake). Min-max scaling would then crush all the other
values from 0–15 down to 0–0.15, whereas standardization would not be much affec‐
ted. Scikit-Learn provides a transformer called StandardScaler for standardization.

## Multiclass Classification

Multiclass Classifiers (a.k.a. Multinomial Classifiers) can distinguish between more than two classes.

## Multicollinearity

Decision trees and boosted trees algorithms are immune to multicollinearity by nature. When they decide to split, the tree will choose only one of the perfectly correlated features.

Logistic Regression or Linear Regression are not immune to Multicollinearity problems and you should fix it before training the model.

Fix: you can either remove the feature or use dimension reduction algorightm such as Principle Component Analysis (PCA).

## Concepts

- Scikit-Learn "predict_proba()" vs "decision_function()"
- `decision_function()` method returns a score for each instance, and then make predictions based on those scores using any threshold you want

Scikit-Learn classifiers have either `decision_function()` or `predict_proba()` method. The `predict_proba()` method returns an array containing a row per instance and a column per class, each containing the probability that the given instance belongs to the given class.

## Algorithms

Random Forest classifiers or naive Bayes classifiers are capable of handling multiple classes directly.
Support Vector Machine classifiers or Linear classifiers are strictly binary classifiers.
You can also use multiple binary classifiers to perform multiclass classification

## Confirmation Bias

Confirmation bias is the tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or values.

Specific effects:

- attitude polarization (when a disagreement becomes more extreme even though the different parties are exposed to the same evidence)
- belief perseverance (when beliefs persist after the evidence for them is shown to be false)
- the irrational primacy effect (a greater reliance on information encountered early in a series)
- illusory correlation (when people falsely perceive an association between two events or situations).

People may show confirmation bias because they are pragmatically assessing the costs of being wrong, rather than investigating in a neutral, scientific way.

## Inference methods

Deductive reasoning, or deduction, is making an inference based on widely accepted facts or premises. If a beverage is defined as "drinkable through a straw," one could use deduction to determine soup to be a beverage. Inductive reasoning, or induction, is making an inference based on an observation, often of a sample. You can induce that the soup is tasty if you observe all of your friends consuming it. Abductive reasoning, or abduction, is making a probable conclusion from what you know. If you see an abandoned bowl of hot soup on the table, you can use abduction to conclude the owner of the soup is likely returning soon.

## Holdout validation and Testing

1. Train multiple models with various hyperparameters on the reduced training set (i.e., the full training set minus the validation set)
2. Select the model/hyperparameters that performs best on the validation set for each different algorithm
3. Train the best model for each algorithm on the full training set (including the validation set) and this gives you the final models
4. Lastly, evaluate the final models on the test set to get an estimate of the generalization error and choose the one that performs best

## Correlation Coefficient

The correlation coefficient only measures linear correlations but misses nonlinear relationships.

## Partial Derivatives
