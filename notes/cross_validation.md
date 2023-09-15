# Cross Validation

Cross validation tests the model's ability to predict unseen data. It helps reducing variance by highlighting overfitting and/or selection bias and gives an insight on how the model generalises.

The dataset is divided in K folds, where at each iteration the model is trained in K-1 folds and tested on the remaining one. Cross Validation will iterate the fit process K times.

The model is trained with the same hyperparameters at each iteration on "diferent" samples of the same training dataset. Given that the model doesn't change but the training data does, what Cross Validation gives is the variance of the model on unseen data. If the variance is hight, the model will likely underfit on real unseen data. If the predictive accuracy among the K trained models has a low variance, this means that it is stable on unseen data and will perform consistently on real unseen data.

Unlike Hyperparameter Search, this method 
