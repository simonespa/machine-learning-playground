# Adaptive Boosting

Adaptive Boosting (a.k.a. AdaBoost) is a boosting approach which weights the data exponentially.

Unlike with RandomForest - where the generated trees are different with different depth - in AdaBoost the generated trees contain the root and two leaves, and these trees are called Stumps.

A stump is a weak learner, as it can only consider one variable at a time.

Unlike RandomForest, each stump (tree) can have a different weight (more/less say) in the final decision.

The models are piped in sequence, and the order is important.

Each sample gets a weight. Initially, the weight is 1 over the total number of samples.

After initialised the weights, we choose which feature is the best at classifying. To do so, we calculate the Gini Index on each of the features and pick the lowest one.

Once the classifier has been picked, we need to calculate how much say will have within the ensamble.

The total error for a **stump** is the sum of the weights associated with the incorrectly classified samples.

## Stopping criteria

Until it reaches the maximum number of trees.
