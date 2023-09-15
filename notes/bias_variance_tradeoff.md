# Bias vs Variance tradeoff

The prediction error can be decomposed so that we can identify which amount is produced by the bias and which one by the variance. The tradeoff is the tension between these two amounts.

The **bias** is the "distance" between the prediction and the real value. In this cases the models oversimplify and a high degree of bias leads to underfitting. The bias is assumptions in the model that make the target function easier to approximate. This happens when the model is unable to capture relevant relations between features and the target variable. High bias means more assumptions about the target function.

The **variance** is an amount that describes the variability of model predictions. The model pays a lot of attention to training data, to a point where it memorizes them rather than learning from them. A model like this is inflexible and doesn't generalise, which leads to overfitting.

Variance is an amount that estimates how much the predicted value changes given a random input. Variance measures the inconsistency of different predictions using different training set. High variance means that the model has memorised the data, so it won't generalise well on a different dataset. This difference in prediction represents the variance. A high variance reflects overfitting.

High Bias: oversimplified model, underfitting
High Variance: overcomplicated model, overfitting

**Bias** refers to the difference between a model's predictions and the true values, while **variance** refers to the variability of a model's predictions
