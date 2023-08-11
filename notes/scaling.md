# Scaling

It's a transformation technique applied to numerical variables. It scales values with different scale/range.

Models that use a weighted sum of input variables are affected by the scale: linear regression, logistic regression, artificial neural networks.
Also models that use the distance or dot products between predictors: K-nearest neighbors or support vector machines.

## Normalization

Normalization scales the feature values in a predefined interval. Usually [0, 1] or [-1, 1].

Also known as Scaling Normalization, scales the feature using minimum and maximum values. The range is often between [0, 1] or [-1, 1] and it is useful when the feature distribution is not Gaussian (a.k.a. NOrmal or bell-shaped). Outliers in your data will be impacted by normalization because it needs a wide range to function correctly.

## Standardization

Standardization scales the feature values by subtracging the mean and dividing by the standard deviation.

Also known as Z-score Normalization) scales the feature using the mean and the standard deviation. This is useful when the distribution is Gaussian.

Scales for normalization fall between [0,1] and [-1,1]. Standardization has no range restrictions. When the algorithms don't make any assumptions about the distribution of the data, Normalization is taken into account. When algorithms create predictions about the data distribution, standardization is applied.
