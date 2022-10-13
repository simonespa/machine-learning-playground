from sklearn.base import BaseEstimator, TransformerMixin

class Mean(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    # calculate the mean for each feature
    return self

  def transform(self, X):
    # fill the null values with the feature mean
    return X
