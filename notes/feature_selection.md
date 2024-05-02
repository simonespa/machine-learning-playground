# Feature Selection

Notes from "Concrete Autoencoders: Differentiable Feature Selection and Reconstructionx" (Abubakar Abid, Muhammed Fatih Balin, James Zou)

Feature selection methods are mainly divided in 3 classes:
- Filter
- Wrapper
- Embedded

## Filter

Filter techniques use statistical tests (e.g. variance) to rank the importance of each feature in a dataset, in order to select features that individually maximise the chosen criteria (e.g. variance).

Filter methods generally do not consider interactions between features and do not provide a way to impute the remaining features; one must train a separate algorithm to do so.

## Wrapper

Wrapper methods select subsets of features that maximize an objective function optimized over the choice of input features using a black-box optimization method, such as sequential search or genetic algorithms (Kohavi & John, 1997; Goldberg & Holland, 1988). Since wrapper methods evaluate subsets of features, they are able to detect potential relationships between features, but usually at the expense of increased computation time.

## Embedded

Embedded methods also consider relationships between features but generally do so more efficiently as they incorporate feature selection into the learning phase of another algorithm. A well-known example is the Lasso (Tibshirani, 1996), which can be used to select features for regression by varying the strength of L1 regularization.
