# Questions

## Cross Validation and Grid Search (Random Search)
- Q: As I understood it, cross validation doesn't give me the best model because it is using the same model with the same parameters and it is training "from scratch" every time. Is cross validation a way to evaluate the model variance based on different portions of the dataset being used for training/prediction?
- A:

- Q: Is Grid Search (or Random Search), unlike Cross Validation, a way to fine tune parameters?

## Imputation

- Q: Should I run the imputation on the entire dataset, or split it first in train/test, then fit the imputation on the training set only so that the mean calculated on the training data is used for both train and test?
- A:

## Data transformation

- Q: If we transform the train set only, when we do prediction should the data be transformed too?
- A:

## Stratified sampling

- Q: When do we use stratifid sampling?
- A: For classification problems, when the class is imbalanced. This is because we want to give the model a fair chance to learn correlations for the minority class
