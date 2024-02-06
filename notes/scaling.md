# Scaling

It's a transformation technique applied to numerical variables. It scales values with different scale/range.

Models that use a weighted sum of input variables are affected by the scale: linear regression, logistic regression, artificial neural networks.
Also models that use the distance or dot products between predictors: K-nearest neighbors or support vector machines.

## Normalization

Normalization - a.k.a. scaling normalization or min-max scaling - scales the feature values in a predefined interval. Usually [0, 1] or [-1, 1].

ScikitLearn: [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

 This method is useful when the feature distribution is non Gaussian (a.k.a. NOrmal or bell-shaped). Outliers in your data will be impacted by normalization because it needs a wide range to function correctly.

Min-max scaling (many people call this normalization) is quite simple: values are
shifted and rescaled so that they end up ranging from 0 to 1. We do this by subtract‐
ing the min value and dividing by the max minus the min. Scikit-Learn provides a
transformer called MinMaxScaler for this. It has a feature_range hyperparameter
that lets you change the range if you don’t want 0–1 for some reason.

## Standardization

Also known as Z-score Normalization, standardization scales the feature values by subtracting the mean and dividing by the standard deviation.

ScikitLearn: [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

This method is useful when the distribution is Gaussian.

Standardization is quite different: first it subtracts the mean value (so standardized
values always have a zero mean), and then it divides by the variance so that the result‐
ing distribution has unit variance. Unlike min-max scaling, standardization does not
bound values to a specific range, which may be a problem for some algorithms (e.g.,
neural networks often expect an input value ranging from 0 to 1). However, standard‐
ization is much less affected by outliers. For example, suppose a district had a median
income equal to 100 (by mistake). Min-max scaling would then crush all the other
values from 0–15 down to 0–0.15, whereas standardization would not be much affec‐
ted. Scikit-Learn provides a transformer called StandardScaler for standardization.

## Comparison

- Normalization has an interval between [0,1] or [-1,1] while standardization has no range restrictions
- Normalization is used when the algorithm doesn't make any assumptions about the data distribution
- Standardization is used when the algorithm does predictions about the data distribution

## Resources
- https://towardsdatascience.com/scale-standardize-or-normalize-with-scikit-learn-6ccc7d176a02

## Notes

If the distribution of the quantity is normal, then it should be standardized, otherwise the data should be normalized. This applies if the range of quantity values is large (10s, 100s, etc.) or small (0.01, 0.0001).
