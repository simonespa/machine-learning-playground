# Statistics

## Population vs Sample

The population is a group of observations that share one ore more features and represent the entirety of all observation that can possibly have those shared features. For example, all people living in Italy, is the population of all observations that share the features of being people and living in the same country.

The sample, is a subset of the population.

## Descriptive

Descriptive statistics is about measuring descriptive informations such as central tendency (mean, median, mode) and dispersion (std deviation, variance, range, etc.). This measurement can only be applied to samples.

## Inferential

When we want to draw conclusion on the population, we need to use inferential statistics.

- Hypothesis
- Drawing a sample out of the population
- Hypothesis testing
- p-value calculation
- Significance
- Errors

First, come up with an hypothesis, than draw a representative sample from the population, run hypothesis testing with the aim to reject/accept the null hypothesis, calculate the p-value and choose a significance threshold. Also consider Type 1 errors (the null hypothesis is true, but we reject it) and Type 2 errors (the null hypothesis is false and we accept it)

## How to choose the right hypothesis test?

It depends on the level of measurement of the data

## Level of measurement

There are 4 level of measurement:
- Nominal: B, D, A, C
- Ordinal: A < B < C < D
- Interval: 1.4 1.6 1.8 2 2.2
- Ratio: 0 0.5 1 1.5 2

In practice, Interval and Ratio are often used to perform the same analysis, therefore, the two measurement are combined together and called Metric (i.e. Metric level).

The level of measurement tells us how the data can be collected, analysed and interpreted.

Different level of measurement support different statistical analysis, tests and visualisation.

## Nominal variables

It's the most basic level of measurement. This data can be categorised but it cannot be ranked in a meaningful way. Examples are gender, type of animals, etc.

## Ordinal variables

Ordinal data can be categorised and ranked.

The difference between ranks doesn't have any mathematical meaning. The interval between them (distance between the data points) is not necessarily equal.

Examples are all sort of rankigs (e.g. first, second, third, etc.), satisfaction rate, etc.

## Metric variables

Metric variables are the highest level of measurement.

Are like ordinal variable, but the difference between them have a mathematical meaning and the interval are equally spaced.

Examples are income, weight, age, utility consumption, etc.

Metric variables can be subdivided in Interval and Ratio.

### Ratio variables

In a car race, if the fastest car takes 2 minutes to finish one lap, and the slowest takes 3 minutes, we can compare them from a starting point which is the True Zero. The measurement of all the cars starts from zero, so we can compare measurements and calculate ratios, like the last car is N times slower than the first car.

### Interval variables

Let's say we didn't measure the start time of the race, we don't know how long it took for the first car to arrive but we know that the last car arrived after 1 minute, so we can measure their interval and say that the last car was 1 minute slower, but we cannot say anything about the last runner being N times slow, because we don't have the absolute value, which is the true zero.       
