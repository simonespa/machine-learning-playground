# Generative vs Discriminative Learning

This is another way to categorise the type of ML algorithms.

Both type of algorithms can be used for classification and they both can be supervised, but the way they separate the negative class from the positive class is very different.

## Generative
A generative approach typically tries to build a model of the positives and negatives. It tries to characterise the entire population of the positives and negatives.

It will try to come up with a distribution of the positives and negatives.

A generative model will look at a boundary in space that informs how liley for an entity to be part of that class.

- Probabilistic model
- works with labelled and unlabelled data

### Models Examples
- Naive Bayes

## discriminative

These type of models focus more on the decision boundary rather than characterising the entire population for each class.

A discriminative approach doesn't care about datapoints far away from the boundary, they are not important for the model. What the model cares about is finding a boundary that separates the positives from the negatives.

This type of classifier is more powerful because it can ignore most of the data and focus to the ones close to the boundary. It cannot be used with unlabelled data.

- Probabilistic model
- Works with labelled data only

### Models examples
- Logistic regression
- KNN
