# Linear Regression Assumptions

## Linearity
The relationship between the independent variable(s) and the dependent variable is linear. This means that the change in the dependent variable is proportional to the change in the independent variable(s).

## Independence
The residuals (the differences between observed and predicted values) are independent of each other. This means that the error terms should not show any correlation. This assumption is particularly important in time series data, where errors can be correlated over time.

## Homoscedasticity
The variance of the residuals should be constant across all levels of the independent variable(s). In other words, the spread of the residuals should not change as the value of the independent variable(s) changes. If the variance of errors changes (known as heteroscedasticity), it can lead to inefficient estimates and affect the validity of hypothesis tests.

## Normality of Residuals
The residuals should be approximately normally distributed, particularly for the purpose of conducting hypothesis tests about the regression coefficients. While this assumption is less critical for estimating coefficients, it is essential for making inferences about the model.

## No Perfect Multicollinearity
In multiple linear regression, independent variables should not be perfectly correlated with each other. Perfect multicollinearity means that one independent variable can be expressed as a linear combination of others, which complicates the estimation of coefficients and can lead to instability in the model.
