# Performance Measures

## Regression

Performance measures for regression problems represent the so called **cost function**.

A typical performance measure for regression problems is the **Root Mean Square Error (RMSE)**. It gives an idea of how much error the system typically makes in its predictions, with a higher weight for large errors.

$$RMSE(X,h) = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (h(x^{(i)}) - y^{(i)})^2}$$

Even though the **RMSE** is generally the preferred performance measure for regression tasks, in some contexts you may prefer to use the Mean Absolute Error (also called the Average Absolute Deviation) for data with many outliers.

$$MAE(X,h) = \frac{1}{m} \sum_{i=1}^{m} \lvert h(x^{(i)}) - y^{(i)} \rvert$$

Both the RMSE and the MAE are ways to measure the distance between two vectors: the vector of predictions and the vector of target values. Various distance measures, or norms, are possible.

Computing the root of a sum of squares **(RMSE)** corresponds to the Euclidean norm. It is the notion of distance you are familiar with. It is also called the $l_2$ norm.

Computing the sum of absolutes **(MAE)** corresponds to the $l_1$ norm. It is sometimes called the Manhattan norm because it measures the distance between two points in a city if you can only travel along orthogonal city blocks.

The higher the norm index, the more it focuses on large values and neglects small ones. This is why the RMSE is more sensitive to outliers than the MAE. But when outliers are exponentially rare (like in a bell-shaped curve), the RMSE performs very well and is generally preferred.

To recap:
- Root Mean Square Error (RMSE) - preferred in general when there are no or few outliers like in a bell-shaped curve
- Mean Absolute Error (MAE) - preferred when there are many outliers (it's less susceptible)

Ref: https://builtin.com/machine-learning/cost-function

## Logistic regression

We can use a modified cost function and as a consequence gradient descend.

More sophisticated and faster ways to optimize the θ parameters of the hypothesis function are:

- Conjugate gradient
- BFGS
- L-BFGS

## Classification

$$accuracy = \frac{correct}{len(pred)}$$

The "accuracy" is generally not the preferred performance measure for classifiers, especially when you are dealing with skewed datasets (i.e. datasets with class imbalance).

### Confusion matrix

A better way to measure the performance of a classification prediction is to look at a confusion matrix (a.k.a. "error matrix"). It's a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix). Each row of the matrix represents the instances in an actual class while each column represents the instances in a predicted class, or vice versa.

The confusion matrix gives you a lot of information, but sometimes you may prefer a more concise metric.

### Precision and Recall

An interesting one to look at is the accuracy of the positive predictions. This measure is called the "precision" of the classifier

$$precision = \frac{TP}{TP + FP}$$

A trivial way to have perfect precision is to make one single positive prediction and ensure it is correct (precision = 1/1 = 100%). This would not be very useful since the classifier would ignore all but one positive instance. So precision is typically used along with another metric named **recall**, also called **sensitivity** or **true positive rate (TPR)**. this is the ratio of positive instances that are correctly detected by the classifier.

$$recall = \frac{TP}{TP + FN}$$

![Confusion Matrix](confusion-matrix.png)

Recap:

- Precision:
- Recall: true positive rate

### F1 score

It is often convenient to combine precision and recall into a single metric called the F1 score, in particular if you need a simple way to compare two classifiers. The F1 score is the harmonic mean of precision and recall (Equation 3-3). Whereas the regular mean treats all values equally, the harmonic mean gives much more weight to low values. As a result, the classifier will only get a high F1 score if both recall and precision are high.

$$F_1 = \frac{2}{\frac{1}{precision} + \frac{1}{recall}} = 2 \cdot \frac{precision \cdot recall}{precision + recall} = \frac{TP}{TP + \frac{FN + FP}{2}}$$

The F1 score favors classifiers that have similar precision and recall. This is not always what you want: in some contexts you mostly care about precision, and in other contexts you really care about recall. For example, if you trained a classifier to detect videos that are safe for kids, you would probably prefer a classifier that rejects many good videos (low recall) but keeps only safe ones (high precision), rather than a classifier that has a much higher recall but lets a few really bad videos show up in your product (in such cases, you may even want to add a human pipeline to check the classifier’s video selection). On the other hand, suppose you train a classifier to detect shoplifters on surveillance images: it is probably fine if your classifier has only 30% precision as long as it has 99% recall (sure, the security guards will get a few false alerts, but almost all shoplifters will get caught).

Unfortunately, you can’t have it both ways: increasing precision reduces recall, and vice versa. This is called the precision/recall tradeoff.

### How to choose

Since the ROC curve is so similar to the precision/recall (or PR) curve, you may wonder how to decide which one to use. As a rule of thumb, you should prefer the PR curve whenever the positive class is rare or when you care more about the false positives than the false negatives, and the ROC curve otherwise. For example, looking at the previous ROC curve (and the ROC AUC score), you may think that the classifier is really good. But this is mostly because there are few positives (5s) compared to the negatives (non-5s). In contrast, the PR curve makes it clear that the classifier has room for improvement (the curve could be closer to the topright corner).


- Accuracy
- ROC AUC
- PR AUC
- F1 score
- PR curve
