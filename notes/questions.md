# Questions/Clarifications

## Cross Validation and Grid Search (Random Search)
- Q: As I understood it, cross validation doesn't give me the best model because it is using the same model with the same parameters and it is training "from scratch" every time. Is cross validation a way to evaluate the model variance based on different portions of the dataset being used for training/prediction?
- A:

- Q: Is Grid Search (or Random Search), unlike Cross Validation, a way to fine tune parameters?

## Stratified sampling

- Q: When do we use stratifid sampling?
- A: For classification problems, when the class is imbalanced. This is because we want to give the model a fair chance to learn correlations for the minority class
