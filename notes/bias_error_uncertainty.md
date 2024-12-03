## Bias

A systematic error (tendency) that skews the results of a measurement or of a prediction in favor of certain outcomes.
It can be concious or unconscious.

### Data bias

It occurs when data is incomplete, inaccurate, or misleading. It can happen during collection, processing, and/or analysis.

### Model bias

It occurs when systematic errors from erroneous assumptions in the model affect the predictions. These errors can arise from different sources, such as the selection of the training data, choice of features, or the intrinsic model assumptions. For example, a linear model will pickup the wrong signals from a non-linear dataset. Bias in the model arises when the algorithm has insufficient capabilities to learn the appropriate signals from the data.
Low model complexity or insufficient data can introduce bias which can then be reinforced and exacerbated.

### Type of bias

Algorithm, sampling, confirmation

## Error

Error is more is anything that is incorrect or deviate from the ground truth. It is not systematic like the bias. We can have errors while collecting data. For example, the device used to collect data is faulty and introduces random errors in the data. There is no systematic bias that is skewing the data, just some random incorrect values. The data can be outliers or completely corrupted, without meaning.

## Uncertainty

Measures the degree of confidence (or lack thereof) of a prediction. Sources of uncertainty can be:
- noisy data
- incomplete data

There are two types of uncertainty: epistemic and aleatoric

### Epistemic uncertainty

Is the model uncertainty due to the lack of training data. A small dataset or even a dataset with low-quality data can increase this type of uncertainty in the model. This uncertainty can be lowered by providing additional high-quality data.

### Aleatoric uncertainty

It refers to the inherent stochasticity of the observations. The collected data is an approximation of reality and not a perfect representation. The collection itself introduces randomness and noise. The noise of every observation accumulates and adds up to the aleatoric uncertainty.

This type of uncertainty cannot be reduced because it is not a property of the model, but an inherent property of the data distribution. This is also known as data uncertainty.

This uncertainty can be estimated by data augmentation during the testing phase.

## How to account for uncertainty in ML

Uncertainty caused by the difference between the approximation and the reality
Uncertainty caused by data quality limitations
Uncertainty caused by inherent limitations of the model

### Model fit uncertainty

Is caused by fitting deficit and is commonly measured by standard model evaluation approaches by splitting the training and test data.

This gives us the lower bound approximation of the remaining uncertainty.

### Data quality uncertainty

The confidence of a model decreases if the quality of the data in input during inference is lower thatn the quality of the training data.

To measure this uncertainty, we have to quantify the data quality of the cleaned data used for training and the data used for the model predictions.

Model evaluation that measure the effects of different data quality issues on the accuracy of the predictions.

### Scope Compliance uncertainty

ML models are trained to do a specific task. If that same model is used to do something different, the outcome becomes unreliable. For example, if autonomous vehicles are trained on right-hand drive country and then the model is deployed for left-hand driving, the model won't have the same confidence, hence the uncertainty needs to be quantified.

## Uncertainty quantification techniques
- Deep Bayesian neural networks
- Sparse Gaussian processes
- Monte Carlo dropout
- Deep Ensembles
- Deep Bayesian Active Learning

## Requirements

A ML model must produce:
- output
- level of confidence
- whether the level of confidence is calibrated
- whether the level of confidence is enough to act upon
