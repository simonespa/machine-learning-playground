# Glossary

- Supervised vs Unsupervised learning
- Offline (batch) vs Online learning
- Instance-based vs Model-based learning
- Cost function vs Utility function (a.k.a fitness or goodness-of-fit)
- Collinearity, multicollinearity, correlation
- Feature selection
- Feature extraction
- Feature engineering
- Anomaly detection
- Hyper-parameters tuning
- Cross validation
- Curse of dimensionality
- Dimensionality reduction
- Accuracy
- Precision/Recall curve
- Receiver Operating Characteristic (ROC curve)
- Area Under the Curve (AUC)
- one-versus-all (OvA) strategy (a.k.a. one-versus-the-rest) for binary classifiers
- one-versus-one (OvO) strategy for binary classifiers
- Generalization error: the error rate of prediction on new cases. This value can be estimated.
- holdout validation (validation test)
- softmax
- logit
- relu
- Unsupervised Learning: KMeans, hierarchical clustering, DBSCAN, PCA, t-SNE
- Time Series Analysis
- Ensemble Methods: random forests, lightgbm and xgboost
- R square and p-value
- Bias/Variance tradeoff
  - Underfitting: high Bias, low Variance
  - Overfitting: low Bias, high Variance

## Bias-Variance tradeoff

The prediction error can be decomposed so that we can identify which amount is produced by the bias and which one by the variance. The tradeoff is the tension between these two amounts.

The **bias** is the "distance" between the prediction and the real value. In this cases the models oversimplify and a high degree of bias leads to underfitting. The bias is assumptions in the model that make the target function easier to approximate. This happens when the model is unable to capture relevant relations between features and the target variable. High bias means more assumptions about the target function.

The **variance** is an amount that describes the variability of model predictions. The model pays a lot of attention to training data, to a point where it memorizes them rather than learning from them. A model like this is inflexible and doesn't generalise, which leads to overfitting.

Variance is an amount that estimates how much the predicted value changes given a random input. Variance measures the inconsistency of different predictions using different training set. High variance means that the model has memorised the data, so it won't generalise well on a different dataset. This difference in prediction represents the variance. A high variance reflects overfitting.

High Bias: oversimplified model, underfitting
High Variance: overcomplicated model, overfitting

**Bias** refers to the difference between a model's predictions and the true values, while **variance** refers to the variability of a model's predictions

## ML Problems

### Supervised

- Fraud Detection
- Image Segmentation
- Medical Diagnosis
- Spam Detection

### Unsupervised

- Anomaly detection
- Network analysis
- Recommender systems
