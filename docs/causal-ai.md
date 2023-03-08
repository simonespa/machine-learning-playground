# Causal AI talk

Andre Franca from causaLens
References:
- https://www.causalens.com/
- https://www.causalaiconference.com/#agenda

observational distribution vs interventional (interventions) distribution

## Interventions

recommending an item to buy constitute as an intervention

example of the rucksack and laptop recommendation

statistical association. Some events are associated and meaningful. For example, the tide related with the time of day

phisical processes generates data
physical processes imply statistical association
statistical association causal learning physical processes

There could be a chicken-egg situation with correlation

Causal AI tries to understand what are the physical association of the system.

A/B testing allows us to intervene in the system

## counterfactuals

when it comes to causality, everything have to be counterfactual

## Notebook example

There is an intervention "exposed" (users have been exposed to a banner) and the outcome called "yes" (people who clicked the banner)


## Biases in causal inference

The platform OS version could be a bias because

## Conditional independence


If you witness shark attack and ice cream selling a lot, they are statistical associated, but what is the statistical association that may be confounding the relationship?

## Partial correlation

It is used to remove the influence of the 3rd variable from the correlation. W is the confounder and must be removed. When we scatter plot we realis they are independent.

I can use the "p value" to check given 2 variables apparently correlated with a confounder, this test allows us to remove the impact of the confounders and measure the real correlation.

Use the Pearson correlation test

## confounder

is any variable that introduces a spurious correlation between 2 other variables.




## Backdoor paths

everything is a backdoor path, and we should test for every thing, except for colliders.

## colliders

the variables that we should not control for. If we control for these variables, we would introduce false correlations.

If the are colliders in the data, we should be careful not to use them as control.

How do we do this?

## Non linear / categorical data

hot encode everything

contingency table

entropy and mutual information (which uses the contingency table).

## Causal discovery test

## conditional association

## covariates

## causal discovery experiments

We can do "tiering" which is basically a way to organise the variable in a causal hierarchy of dependencies. For example, the device informs which browser I do have. If I have an iPhone I will definitely have Safari, but not other browsers

Testing X vs Y conditional on W (Perason value equal to )

Recap

how causal discovery works
figuring out the uncoditional dependency
identify the colliders and confounders
oriented graphs


at the end we have a causal model, to figure out the relationship between variables



Answer to my question:

we can define an oracle:

tiering of the variables

latent variable problem. What is a latent variable? When we run marketing budget, the marketing team is setting the budget based on things beyond our control. How can we control these things? We can use instrumental variables

## Instrumental variables

# etherogeneous treatment effect






if there is a distribution shift in the data, then we should realy have this causal test

for purely predictive models (with direct drivers) it is actually going to improve the performance of the model for generalised use case outside the training data.


bunch of customers, some of them churn, some not. Although


simpson paraox


if we want to predict only how many customer are going to churn, then we are ok with strong predictors


but if we are trying to understand what is causing churn and how to stop it, then in that case we need to use the test, because we need to know the real t
