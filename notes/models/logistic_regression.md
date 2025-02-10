# Logistic Regression

- Logistic Regression is a type of Generalised Linear Model
- To verify whether a variable is useful as a predictor or not, we can use the "Wald's test" (z-values)
- Logistic regression can use continuous and discrete measurement to classify
- It doesn't have the same concept of "residuals" like in Linear Regression. This means that it can't use least squares and it can't calculate the coefficient of determination (r-squared)
- The loss function used is called "maximum likelihood"
- The coefficients are calculated in terms of log odds using a linear model that spans on the y-axis from -Infinity to +Infinity
- Concept of t-tests are applied in Logistic Regression
- Everything we do with a linear model can be done with a logistic model, as long as we use log odds, which is $\frac{p}{1-p}$
- If we fit a linear function on the new log-odds function, and project the points on the line, the residuals are +/- Infinity, so we can't use least squares for the best fitting line. This is why we use maximum likelihood.

## Steps
- Choose a point and take the log(odds)
- We transform this value back to the original 0-1 logistic regression frame of reference where
$$p = \frac{e^{log(odds)}}{1 + e^{log(odds)}}$$
