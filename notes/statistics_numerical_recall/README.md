# Statistics and numerical recall

## Mean, median and mode

- The mean is the average of a data set.
- The median is the middle of the set of numbers.
- The mode is the most common number in a data set.

## Standard Deviation

The standard deviation is generally denoted σ (the Greek letter sigma), and it is the square root of the variance, which is the average of the squared deviation from the mean. When a feature has a bell-shaped normal distribution (also called a Gaussian distribution), which is very common, the “68-95-99.7” rule applies: about 68% of the values fall within 1σ of the mean, 95% within 2σ, and 99.7% within 3σ.

## Percentiles

A percentile indicates **the value below which a given percentage of observations in a group falls**.

For example, given the following table:

| Stats | Age |
| ----- | --- |
| 25%   | 18  |
| 50%   | 29  |
| 75%   | 37  |

you can read its data as follows: 25% of the population have an age lower than 18, while 50% are lower than 29 and 75% are lower than 37. These are often called the 25th percentile (or 1st quartile), the 50th percentile (or 2nd quartile or median), and the 75th percentile (or 3rd quartile).

## Skewed distributions

A left-skewed distribution has a long left tail. Left-skewed distributions are also called negatively-skewed distributions. That’s because there is a long tail in the negative direction on the number line. The mean is also to the left of the peak.

A right-skewed distribution has a long right tail. Right-skewed distributions are also called positive-skew distributions. That’s because there is a long tail in the positive direction on the number line. The mean is also to the right of the peak.

<img src="left-right-skewed-distributions.png" width="50%" alt="Skewed distributions">

In a normal distribution, the mean and the median are the same number while the mean and median in a skewed distribution become different numbers.

A left-skewed, negative distribution will have the mean to the left of the median.

<img src="left-skewed-distribution.png" width="50%" alt="Left-skewed distribution">

A right-skewed distribution will have the mean to the right of the median.

<img src="right-skewed-distribution.png" width="50%" alt="Right-skewed distribution">

## Skewness

Is a measure of the distribution of values around the mean.

The tail is longer on one side and in most cases, the mean is to the left of the median for left-skewed distribution or to the right for right-skewed ones. This isn’t a reliable test for skewness though, as some distributions (i.e. many multimodal distributions) violate this rule. You should think of this as a rule of thumb.

## Linear equation

A linear equation is described by $y = \theta_0 + \theta_1X_1$. This equation has only one variable and it is called _"univariate linear equation"_.

A _"multivariate linear equation"_ on the other hand will have more than one variables: $y = \theta_0 + \theta_1X_1 + \theta_2X_2 + ... + \theta_nX_n$

In a univariate linear equation, $\theta_0$ represent the `y-intercept` and $\theta_1$ is the `gradient` (a.k.a. `slope` of the function).

## Variance

The variance of something is equal to the ratio between the sum of squares of these things over the number of these things, which is equal to the average sum of squares.

The variance describes the variation or the residuals around

## Variance vs Standard Deviation

