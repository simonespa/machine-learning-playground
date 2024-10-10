## Scale Invariant

Tree-based ML models are scale invariant. They don't care whether features are expressed in KM, percentage, $, etc. The decision boundary at each node is defined by a constraint like "feature X >= some_value". This means that it doesn't matter which scale this feature is measured, as long as the value satisfies that constraint.

## Scale Sensitive

Models that use the Euclidean space to calculate distances, are scale sensitive. They require all numerical features to have the same scale, to contribute equally. Otherwise the model could favour one feature over another, or the make the learning unstable.

### Distance based

- K-Nearest Neighbours (KNN) and K-Means use the Euclidean space to measure the distance between datapoints. They require all features to contribute equally.
- Linear Discriminant Analysis (LDA), Principal Component Analysis (PCA) etc. are also distance-based techniques. Tey use the Euclidean space to find the direction/eigenvector/principal component that maximises the variance.

### Gradient Descent based

Models based on Gradient Descent optimisation like linear & logistic regression, SVM, Neural Networks etc. require all features to be on the same scale because otherwise some weights could update much faster than others, making the training fase unstable.
