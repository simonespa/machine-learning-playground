# Gradient Boosting

It starts creating one node (a leaf), rather than a stump. This leaf represents an initial guess of the target value for all the samples. For continuous variables (regression), this initial value is the average. For labels it could be the mode. Then a tree is created. It won't be a stump, because unlike AdaBoost, the tree will be larger.

The tree is still constrained, like for example with a maximum number of leaf that can be set to up 8 or 32 (as used in practice).

Once the average is calculated, we calculate the residuals for each numeric target value, and then use all the features to create a constrained tree, to predict the residuals, rather than the actual target variable.

## Stopping criteria

The algorithm continues until it reaches the maximum number of trees set or the ensemble can't improve the fit anymore.
