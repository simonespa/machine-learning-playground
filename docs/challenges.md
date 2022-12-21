# Challenges

## Bad Data

- Insufficient Quantity of Training Data
  - The Unreasonable Effectiveness of Data
  - Data matters
  - Sampling noise
- Nonrepresentative Training Data
  - Sampling bias
  - Nonresponsive bias
  - data mismatch between test and production (the data used for test comes from a dataset which is not representative of the real-life live data)
- Poor-Quality Data
  - Training data is full of errors and noise
  - Missing data
    - Discard the attribute
    - Discard the instances with missing data
    - Fill in the missing values
    - Train one model with the feature and one model without it
  - Outliers
    - Discart the attribute
    - Discard the instances with outliers
    - Fix the error manually with the help of a domain expert
- Irrelevant Features
  - Feature engineering
    - Feature selection: selecting the most useful features
    - Feature extraction: combining (merge) existing features to produce a more useful one (dimensionality reduction algorithms)
    - Creating new features by gathering new data

## Bad Algorithms

- Overfitting the Training Data
  - Cause
    - Overgeneralization
    - Noisy data
    - Small sample
    - Model too complex relative to the amount of noise in the training data
  - Fix
    - Reduce the number of attributes in the training data
    - Simpler model
    - Bigger sample
    - Reduce the noise in the data
    - Regularization: constrains the model to make it simpler (e.g. by controlling the degree of fredom of a linear model)
- Underfitting the Training Data
  - Fix
    - Use a more powerful model
    - Feeding better features to the learning algorithm
    - Reducing the constraints on the model
