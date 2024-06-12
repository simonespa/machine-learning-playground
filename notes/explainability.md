# Explainability

Feature importance tells us how important each feature is to the model prediction in general. On the contrary, it cannot tell us:
- the importance of each feature for a single prediction
- whether a given feature increased/decreased the prediction in regression
- whether a given feature changed the probability of the positive class in classification


## SHAP

https://towardsdatascience.com/introduction-to-shap-with-python-d27edc23c454
https://towardsdatascience.com/shap-for-categorical-features-7c63e6a554ea

## Limitation of SHAP
- Package: although it's model agnostic in theory, in practice it can work well with the most popular frameworks but it may not work with everything out there
- Featue Dependencies: when 2 or more features are correlated, SHAP is impacted. Especially with Kernel SHAP, because it uses permutations to make the calculation faster, the feature value of one observation takes into account the entire range for that feature, which may lead to unrealistic conclusions
- Causal Inference: it cannot be used for causal analysis. SHAP measures how important a feature is to a given model and not how important is in the real world. We should not make conclusions that are beyond the model.
- Human Error: when we read SHAP plots, we may find patterns that aren't there and come up with explaination that may
