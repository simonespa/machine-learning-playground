# Scikit Learn

## API

The API consists of 3 interfaces:

- Estimator: for building and fitting models
- Predictor: for making predictions
- Transformer: for converting data.

The API design has the following characteristics:

- Constructor parameters and parameter values determined by learning algorithms are stored and exposed as public attributes for inspection.
- Datasets are encoded as NumPy multidimensional arrays for dense data and as SciPy sparse matrices for sparse data.
- Parameters use sensible defaults to allow the algorithms to be run _as-is_ as baseline.
- Scikit-Learn is oriented towards batch learning but not for online learning. This is because it makes optimal use of NumPy and SciPy preventing the overhead of Python function calls or dynamic type checking.

## Estimators

Estimators form the core of the library.

This interface exposes the `fit` method to "fit" a model from the training data. It accepts two parameters, the first one is the matrix of features while the second one represents the column of labels for supervised learning.

```py
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

All classic learning altorithms implement this interface, plus the preprocessing routines (e.g. feature scaling), feature extraction techniques (e.g. vectorization of text documents) and stateless processing steps that do not require the fit method to perform useful work.

This method always return the estimator object it was called upon.

The parameters learned by the estimator are also exposed publicly as an attribute with a trailing underscore.

## Predictors

Extends the estimator by adding the `predict` method.

For supervised learning, it returns the predicted labels

```py
y_pred = model.predict(X_test)
```

Some unsupervised learning algorithms may also implement the Predictor interface (e.g. KMean s)

Predictors may implement methods that quantify the confidence of prediction. For linear models the `decision_function` method returns the distance of samples to the separating hyperplane. Some predictors also provide a `predict_proba` method which returns class probabilities.

Predictors must also provide a `score` function to assess their predictive performances.

For supervised learning, this method takes as input arrays `X_test` and `y_test` and typically computes the **coefficient of determination** between `y_test` and `predict(X_test)` in **regression**, or the **accuracy** in **classification**. The only requirement is that the score method returns a value that quantifies the quality of its predictions (the higher, the better).

An unsupervised estimator may also expose a `score` function to compute the likelihood of the given data under its model for example.

## Transformers

Some estimators implement this interface to modify or filter data before feeding it to the learning algorithm.

This interface exposes the `transform` method. It takes data in input and returns the transformed version of it.

Preprocessing, feature selection, feature extraction and dimensionality reduction algorithms are all provided as transformers within the library.

```py
scaler = StandardScaler()
scaler.fit(X_train)
X_train_transformed = scaler.transform(X_train)
```

This interface also provides `fit_transform(X_train)` method which is equivalent to the chained combination `fit(X_train).transform(X_train)`

## Meta-estimators

Estimators that take in input simpler estimators.

An example is the **ensemble method** which combines simpler models (e.g. decision trees).

The meta estimators define the same interface of the **Estimators**.

## Estimator composition

Composition mechanism allow to run transformations, fitting and prediction in parallel through `FeatureUnion` object or sequentially using the `Pipeline` object. They can also be combined to create a complex workflow.

The `Pipeline` is a sequence of `N` steps where the first `N - 1` steps are **transformers** and the last can be a **predictor** a **transformer** or both. The `Pipeline` exposes the same method of the last estimator in the chain.

The `FeatureUnion` combines multiple transformers into a single one, combining their outputs (i.e. union).

## Model selection

Is the process of finding the best combination of hyper parameters (within some hyper-parameter space) according to a user-defined criterion.

In `scikit-learn` there are two meta-estimators that implement this algorithm: `GridSearchCV` and `RandomizedSearchCV`. They both take in input an estimator and a set of hyper parameter settings to search through.

`GridSearchCV` exhaustively tests all combinations of hyper-parameters.

`RandomizedSearchCV` is a smarter algorithm that avoids the combinatorial explosion of grid search by sampling a fixed number of times from its parameter distributions.

Optionally, both of them take a **cross validation** scheme and a **score function** in input.

## Cross Validation

The cross validation method used by default is **k-fold**.

Other methods provided are: **stratified k-fold** and **leave-one-out**.

## Score Function

The score function used by default is the estimator’s **score** method.

Other score function provided include: **accuracy**, **AUC** and **F1 score** for classification, **R2 score** and **mean squared error** for regression.
