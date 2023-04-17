# Linear Regression

The linear regression model is the linear equation that multiplies the feature by a single scaler.
There are different methods to calculate an optimal set of scalar values, and these methods are: gradient descent, OLS, etc.

There are 3 types of gradient descent:

- Batch Gradient Descent
- Stochastic Gradient Descent
- Mini-batch Gradient Descent

## Training epoch of Gradient Descent

A training epoch in gradient descent includes the sum of the error and the updating of the model parameters.

## Batch Gradient Descent

Calculates the global error for each datapoint of the entire dataset, updating the model only after considering all the datapoints. This process is computationally efficient, but it could be prohibitive for massive datasets because it has to load and compute all the data in memory. This algorithm is stable and guaranteed to converge for convex cost functions.

## Stochastic Gradient Descent

This method runs an entire epoch for each datapoint. This means that the model parameters are updated on each data point, and this is what it gives it a lot of randomness. These frequent updates are not computationally efficient and can result in noisy gradients, but at the same time this characteristic could help the algorithm to escape local minima to reach the global one, because the path of the gradient reaches more places of the hyperplane, hence is more likely to escape a local minima. This is not guaranteed though, stochastic gradient descent can still get stuck.

## Mini-batch Gradient Descent

This is a hybrid approach that gets the best from the previous two Gradient Descent methods. It splits the dataset in smaller batches, and performs updates on each of those. This approach is balancing the benefit of both improving in efficiency compared to Stochastic GD with the use of batches, but also the benefit of having some randomness that may help escaping local minima if any.

1. Fit the data with a linear function, by setting the initial weights to a random value
2. Optimise the parameters using the Gradient Descent (or another optimisation algorithm)
3. Calculate the coefficient of determination R^2 (r-squared) - how well the model represents the data
4. Calculate a p-value for r-squared

It quantifies the relationship in the data using R squared. This value needs to be large.
It also determines the significance of this relationship using the p-value calculated with F. This value needs to be small.

In order for the regression to be meaningful, we need both values.

## R square and p-value

Reference: https://www.youtube.com/watch?v=7ArmBVF2dCs

### R squared

Also known as coefficient of determination.

The R-squared value is a measure of how well the model explains the variation of the data. It is an example of a goodness-of-fit statistic.

The R square tells how much variation is explained by the model. Its value is between 0 and 1. A value of 1 means that the model explains 100% of the variation.

For example, imagine the independent variable (X-axis) is the weight of something and the dependent variable (Y-axis) is the size of something. Let's say that the variance around the least squares function is less than the variance around the mean of sizes (the sum of the residuals is smaller). With R square we can say that some of the variation in "size" is explained by taking "weight" into account, and that "amount" is represented by R square.

Assuming the R square is N (or N%), we can say that there is a N% reduction in variance when we take the independent variable (X-axis) into account. Alternatively, we can say that the independent variable (X-axis) explains N% of the variation in the dependent variable (Y-axis).

R squared = The variation of the dependent variable (Y-axis) explained by the independent variable (X-axis) / The variation of the dependent variable (Y-axis) on its own

#### Edge cases

In a multivariate function, some parameters may not be of particular importance. This means that the least square will ignore them, by making the parameter equal to zero. This won't make the R square worse. For this reason, an adjusted R squared is calculated, which scales R squared by the number of variables.

On the other hand, these same variable may be random value that only by chance may reduce the sum of square around the fit function, hence improve the R square. It may seem that using these parameters will produce a better fit function, but actually they don't, it's just random noise.

The more statistically insignificant variables are used, the more opportunities there are for random events to reduce the sum of squares and as a consequence improve R square.

Consider this, if we have only two measurements, the fit function for these measurements is a function that links these two data points. This means that the sum of squares around the fit function will always be zero for any two data points. This means that the R squared value will always be 100%

We need a way to determine if the R squared value is statistically significant.

R-squared = (ss_mean - ss_fit) / ss_mean

### p-value

The p-value for a model determines the significance of the model compared with a null model. For a linear model, the null model is defined as the dependent variable being equal to its mean. So, the p-value for the model is answering the question, Does this model explain the values of the dependent variable significantly better than would just looking at the average value of the dependent variable?

The p-value explains the significance of the model.

The p-value for R squared comes from something called F

If the p-value is less than the significance level (usually 0.05) then your model fits the data well.

1. low R-square and low p-value (p-value <= 0.05)
   It means that your model doesn’t explain much of variation of the data but it is significant (better than not having a model)

2. low R-square and high p-value (p-value > 0.05)
   It means that your model doesn’t explain much of variation of the data and it is not significant (worst scenario)

3. high R-square and low p-value
   It means your model explains a lot of variation within the data and is significant (best scenario)

4. high R-square and high p-value
   It means that your model explains a lot of variation within the data but is not significant (model is worthless)

### F

F = ((ss_mean - ss_fit) / (p_fit - p_mean)) / (ss_fit / (n - p_fit))

The "p" values are called the "Degrees of fredom"
