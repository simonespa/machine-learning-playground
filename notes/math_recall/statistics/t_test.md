# t-test

The t-test is the most common statistical test. It analyses whether there is a significant difference between the means of two groups.
For example, group 1 receives drug A, group 2 receives drug B, we want to know whether there is a difference in blood pressure between these two groups.

## Types of t-test

There are 3 types of t-tests:

- One sample t-test
- Independent samples t-test
- Paired samples t-test

## One sample t-test

We use it when we want to compare the mean value of a sample with a known reference mean of a population. For example, let's say a car manufacturer claims its EV model A has a range of 300 miles. We then collect a sample of cars for this model and run tests in different conditions. The mean value for this sample is 298 miles. This test will tell us whether 298 is significantly different from 300.

## Independent samples t-test

We use this when we want to compare the means of two independent groups or samples. We want to know whether there is a significant difference between these means. A typical example is when we want to compare the effects of two drugs: A and B. In this case, we randomly divide the observations in two groups. The first group receives drug A, the second drug B. With this t-test, we measure whether there is a significant difference of the mean on a given metric (e.g. pain reliefe, effectiveness, etc.).

## Paired samples t-test

We use this t-test to compare the means of two dependent groups. For example, how effective a diet is. To do this, we weight the people before the diet and after the diet. We can now look at the difference between before and after. The t-test will tell us whether there is a significant difference.

## Note

- The one sample t-test is like the Paired sample. If you treat the one sample and measure the same observations before and after, you are going to have a difference for each. You can now calculate the mean, and assess whether the calculated mean is significantly different from the reference mean which is zero.

## Assumptions for te t-test

- We need a suitable sample and in the case of the One sample t-test we also need a reference value.
- The variable must be metric (e.g. age, body weight, income, etc.)
- The metric variable must be normally distributed for all 3 test variants
- For the independent test, the variance must be equal (levene's test)

## Hypothesis for Ons sample t-test

Null hypothesis: the sample mean is equal to the reference value

## Hypothesis for Independent samples t-test

Null hypothesis: the mean values in both groups are the same

## Hypothesis for Paired samples t-test

Null hypothesis: the mean of the difference between the pairs is zero

## Why do we need a t-test?

We use it to make inferences on the population based on the alternative hypothesis.

## How is it calculated?

### One sample t-test

We first calculate the `t` value:

$t = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}}$ where the numerator is the difference between the sample mean and the reference mean and the denominator is the Standard Error, which is the standard deviation divided by the square root of the number of data points.

### Independent sample t-test

$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{\sigma^2_1}{n_1} + \frac{\sigma^2_2}{n_2}}}$

### Paired sample t-test

$t = \frac{\bar{x}_d - 0}{\frac{\sigma}{\sqrt{n}}}$

## What is the t value?

The `t` value is directly proportional with the difference of the means.

The bigger is the difference of the means, the bigger is the t value and viceversa.

The t value is also smaller when there is a bigger dispersion in the distribution, which is accounted for by the standard deviation at the denominator. This means that the more scattered the data the less meaningful a given mean difference is.

## Reject/Accept null hypothesis

The `t` value can be used in two ways:
- Read a critical t-value from the table
- Calculate a p-value

## p-value and significance level

The p-value is a measure of how likely is that the difference of the mean in the sample deviates from the one in the population.

The various critical t values are calculated into a table. If the t-value is greater than the critical t-value, we reject the null hypothesis.

The p-value is calculated by using the t-value and knowing the degrees of freedom.
