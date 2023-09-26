# Bayes Theorem

## References
- https://www.youtube.com/watch?v=R13BD8qKeTg
- https://www.youtube.com/watch?v=HZGCoVF3YvM
- https://www.youtube.com/watch?v=O2L2Uv9pdDA

It is mainly used to quantify belief.

Evidence should not determine beliefs, but update them.

How you update your beliefs, based on evidence.

- The ratio (the width) is described by the prior. This could be your own knowledge of the ratio based on bias and stereotypes, or a more accurate information coming from a statistical sampling of the population (e.g. librarian and farmer that fits a certain description)
- Questions about the personalities/stereotypes shift the relevant likelihood (the height)

## The formula

$P(H|E) = \frac{P(H) * P(E|H)}{P(E)} = \frac{P(H) * P(E|H)}{P(H) * P(E|H) + P(¬H) * P(E|¬H)} $

where

- $P(E|H)$ is the probability of observing the evidence given the hypothesis is true. It is a.k.a. **likelihood** because it is the proportion of a certain group that fits the description.
- $P(H)$ is the prior probability of a hypothesis being true (before any evidence). It is a.k.a. **prior** because it represents the probability of the hypothesis before taking in consideration any evidence. This value could come from any ratio taking in consideration the general population.
- $P(E)$ is the total probability of seeing the evidence.
- $P(H|E)$ is the probability a hypothesis holds given some evidence observed is true. It is a.k.a. **posterior**. It is your belief about the hypothesis after seeing the evidence.

When we see the "|" (vertical bar) it means we are talking about some proportion of a limited part of the total space of possibilities.

## The usage

- It can be used to analyse the extent of which new data affect the model (either validate or invalidate).
- In ML can be used to model a machine belief

## How to proceede with the librarian/farmer example

Read the evidence, according to the description you estimate a percentage which holds true for each category. Let's say 40% of librarian and 10% of farmers fits the description.

This means that you have $\frac{4}{4 + 20} ≈ 16.7%$ of librarian that fits the description given the evidence.

Even if we think that a librarian is 4 times more likely than a farmer to fit the description, the probability of this description fitting for a librarian is still a very low percentage.

## Multimonial Naive Bayes classifier

When we talk about Naive Bayes in ML we refer to the multinomial classifier. There is also another version of this algorithm called Gaussian Naive Bayes which uses the normal distributions of each feature to then apply the Naive Bayes theorem.

When the probability is about a discrete variable, it is also called likelihood.

The Naive Bayes classifier has a problem when a word is not found in the training set. In that case, the probability of that word given a particular class would be zero. By having zero in the multiplication, in doesn't matter whether the instance clearly belongs to a specific class, zero would set the total score to zero. To overcome thisproblem, a parameter "alpha" equal to 1 (or any other number really) is added to all the frequencies. This will remove any likelihood equal to zero in the calculation.

Naive Bayes has high bias because it ignores the ordering of the words, but since in practice it performs really well, it has low variance.
