# Questions

* When to apply scaling?
* Do we transform the train set only or the test set too?
* If we transform the train set only, when we do prediction should the data be transformed too?
* In `sickit-learn` transformers have the `fit`, `transform` and `fit_transform` methods. The example have the fit being called before transforming the dataset. Shouldn't we transform before fitting?