# Questions

## Feature scaling
- When to apply scaling?

## Data transformation
- Do we transform the train set only or the test set too?
- If we transform the train set only, when we do prediction should the data be transformed too?
- In `sickit-learn` transformers have the `fit`, `transform` and `fit_transform` methods. The example have the fit being called before transforming the dataset. Shouldn't we transform before fitting?

## Stratified sampling

- When do we use stratifid sampling?
- Should we stratify using a categorical attribute only or numerical are good too?
- Can we use any random attribute or only the ones that are strong predictors/important attributes?
- Can the label attribute for supervised learning be used for stratification?
- Should it be only one label or can it be more than one used for stratification?

## Dataset dimensions
- What's the right proportion between the number of columns and rows?
