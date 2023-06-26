# Concepts

- Ref: https://www.causalens.com/why-causal-ai/

 - "LIME or SHAP cannot guarantee the model will always act sensibly as they are trying to explain based on observed inputs. SHAP and Lime are only explaining the past and not trying to anticipate what the model may do in the future."
 - They tell us what features are associated with the prediction but not necessarily what features drive the outcome.
- Every ML model hallucinates. This problem arises when you try to extrapolate beyond the training data.
- Causal AI provides a priori explainability. This means you know globally what the model is doing and sensible outcomes are guaranteed.

## Simpson's paradox

## Interventions

## Counterfactuals

## Conditional Independence Test

It is used to find the causal graph automatically, using just the dataset.

Variable dependency can be detected by groups (tiers) where you don't know a group of them is related to another group, but you know there is a relationship. You can also define a direct relationship between two variables when you know exactly the relationship between them.

## Causal Discovery

### Causal Feature Selection
- FSNOD
- Multivariate Granger Causality
- PCMCI
- PCMCI AR
- PCMCI Ensemble
- PCMCI One
- PCMCI Zero
- VAR LINGAM
- VAR NOTEARS

### Full graph discovery

- A*
- A* Global
- A* Local
- FCI
- FCI Exogenous
- FCI Probabilistic Tiers
- FCI Tiers

### Constraints-based methods
It uses Conditiona Independence testing with p-values. In some cases it can identify latent confounders. Examples include PC and FCI.

### Score-based methods

It is based on evaluating a potential causal graph using a score function (e.g. BIC). Score functions mostly include likelihood terms, but some also incorporate CI tests. Examples include GES and A*.

### Continuous optimization methods

Basd on functional learning (e.g. treating the graph structure as a continuous variable). At the moment, these approaches are not robust (e.g. NOTEARS). Examples include NOTEARS and GOLEM
