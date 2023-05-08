# Transformations

## Normalization vs Standardization

**Normalization** (also known as Scaling Normalization) scales the feature using minimum and maximum values. The range is often between [0, 1] or [-1, 1] and it is useful when the feature distribution is not Gaussian (a.k.a. NOrmal or bell-shaped). Outliers in your data will be impacted by normalization because it needs a wide range to function correctly.

**Standardization** (also known as Z-score Normalization) scales the feature using the mean and the standard deviation. This is useful when the distribution is Gaussian.

Scales for normalization fall between [0,1] and [-1,1]. Standardization has no range restrictions. When the algorithms don't make any assumptions about the distribution of the data, Normalization is taken into account. When algorithms create predictions about the data distribution, standardization is applied.
