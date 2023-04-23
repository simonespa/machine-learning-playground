- [Machine Learning Steps](#machine-learning-steps)
  * [Data Collection](#data-collection)
  * [Data Exploration](#data-exploration)
    + [Feature categorisation](#feature-categorisation)
    + [Data Visualisation](#data-visualisation)
      - [Comparison Visualisation](#comparison-visualisation)
      - [Relationship Visualisation](#relationship-visualisation)
      - [Distribution Visualisation](#distribution-visualisation)
      - [Composition Visualisation](#composition-visualisation)
  * [Data Preparation](#data-preparation)
    + [Cleaning Missing Data](#cleaning-missing-data)
    + [Handling Outliers](#handling-outliers)
    + [Handling Class Imbalance](#handling-class-imbalance)
    + [Feature Scaling](#feature-scaling)
      - [Z-score Normalization](#z-score-normalization)
      - [Min-Max Normalisation](#min-max-normalisation)
      - [Log transformation](#log-transformation)
    + [Dataset Size](#dataset-size)
    + [Sampling](#sampling)
    + [Curse of dimensionality](#curse-of-dimensionality)
    + [Dimensionality Reduction](#dimensionality-reduction)
      - [Feature Selection](#feature-selection)
      - [Feature Extraction](#feature-extraction)
  * [Modeling](#modeling)
  * [Evaluation](#evaluation)
    + [Regression Evaluation](#regression-evaluation)
    + [Classification Evaluation](#classification-evaluation)
  * [Production and Monitoring](#production-and-monitoring)

# Machine Learning Steps

## Data Collection

Identify and gather data we need. We need to consider the following aspects:

- Accuracy
- Relevance
- Size (some machine learning algorithms need small dataset, other the opposite)
- Variability
- Ethics (privacy, security, informed consent, bias)

## Data Exploration

Is the process of describing, visualising and analysing the data in order to better understand it. During this phase the structure of the data is explored.

- How many rows and columns are in the data (size of the input)
- What type of values
- Are there missing, incosintent or duplicate values into data
- Are there outliers

The **rows** of the dataset are known as **instances** or **examples**, while the **columns** are known as **features** or **variables**. In supervised learning, the label column is also known as **target variable**. The label is also described as a **dependent** or **output** variable, whereas the rest of the features are the **independent** or **input** variables.

### Feature categorisation

Features can be categorised as:

- **Categorical**: value are discrete (limited set of values).
- **Continuous**: integer or real number. Infinite number of possible values.

Categorical features can be:

- **Nominal**: labels with no ordinal relationship (e.g. names of cities, departments, etc.)
- **Ordinal**: labels that have an ordinal relationship among them (e.g. level of glucose in the blood, degree of difficulty, etc.)

> NOTE: not all numeric features are continuous.

Features can be **dense** or **sparse**. Sparse features can cause problems like **overfitting** and suboptimal results in learning models. Understanding why this happens is crucial when developing models. Multiple methods - including **dimensionality reduction** - are available to fix issues due to sparse features.

Features can also be categorised based on their dimensionality (unidimensional, multidimensional). The higher the dimensionality (cardinality) the more complex is the computation.

### Data Visualisation

#### Comparison Visualisation

It illustrates the difference between two or more items. The “box plot” can be used. This visualisations provides insights, such as:

- Significance (importance) of a feature
- Variation of the mean value across subgroups
- Existence of outliers

#### Relationship Visualisation

- Helps visualise the correlation between two or more continuous variables.
- Scatter plots and line charts are the most commonly used for this purpose.
- They show how 1 variable changes in response to a change in another.
- Provide insight into the significance and the presence of outliers wihin the value of that feature

#### Distribution Visualisation

- Illustrate the statistical distribution of the values of a feature
- Histogram is the most common used
- With Histogram we can visualise the most common (recurring) value of a feature
- Histogram visualise the spread (or skeweness) of the values
- Also visualise possible outliers

#### Composition Visualisation

- Show the component makeup of the data
- Stacked bar charts, grouped bar charts, and pie charts
- Stacked bar charts show how much a subgroup contribute to the whole
- Show relative or absolute change in the composition of a subgroup over time

## Data Preparation

This step prepares the dataset based on the chosen machine learning approach and algorithm.

It modifies and transforms the structure of the data in order to make it easier to work with.

It involves resolving data quality issue, such as:

- missing data
- duplicates
- noisy data
- outliers
- class imbalance
- dataset size

There are several techniques that aims at preparing the dataset for the modeling stage. Some of them focus on the data and its structure, some other on the dimensions of the dataset.

### Cleaning Missing Data

Data can be missing for many reason. It can happen for human error, lack of a reliable source, because the data is not available or can't be retrieved or simply because it doesn't exist.

There are different approaches to deal with missing data:

- Remove all instances with features that have a missing value
- Remove the features that have a lot of missing value (high percentage) only if from the data is clear that these features are not a strong predictor
- Replace the missing data with a neutral value (i.e. imputation). It could be zero, mean, median, mode, etc.
- Use a method known as “Imputation”. It’s a systematic approach to fill in missing data by using the most probable substitute value. There are several approaches. The **median imputation** for example substitutes the missing values with the median of the column.

IMPORTANT: Be careful when removing the samples with missing value. There may be a reason why that value is missing, and that reason may be an important indicator. In that case, removing the sample may introduce bias.

### Handling Outliers

OUtliers are significantly different values compared to the other observations (unusual values). This values are very far and isolated from the central tendency. Depending on the type of algorithm chosen, outliers may or may not affect the prediction. To deal with outliers we have to understand what these unusual data represent.

In case the feature is not a predictor, it could be removed or if it is important and the algorithm interprets the values geometrically, then we may need to scale the range to reduce the distance.

### Handling Class Imbalance

If the values of the dependent variable are categorical, we refer to them as **class labels** and the proportion of each class in the dataset is known as **class distribution**.

For most real-world problem, the class distribution is skewed (i.e. not uniform). For example, with loan risk detector, most people will likely be able to repay their loan than default on it. This phenomenon is known as **class imbalance**.

Because of this disproportion in the class distribution, the class imbalance issue could lead to serious misleading predictions, because the supervised machine learning algorithm didn’t have an equal shot at learning the patterns that correspond to each class label.

One approach to fix this problem is to undersample the majority class, this means that we randomly remove some instances of the majority class in an attempt to even the class distribution.

### Feature Scaling

Also known as data Normalisation or standardisation. The goal of this transformation is to ensure that the values of two or more features have the same interval. This normally involves scaling data to fall within a small or specified range. Normalisation is required by certain ML algorithms to reduce the complexity and make the result easier to interpret.

As a rule of thumb, we should always use feature scaling with algorithms that calculates distances between points.

Only continuous values need to be feature scaled.

Algorithms that DO require feature scaling

- Support Vector Machine (SVM)
- K-nearest neighbor (KNN)
- K-Means Clustering
- Linear Regression
- Logistic Regression
- Neural Networks

Algorithms that DO NOT require feature scaling (mostly non-linear ML algorithms):

- Decision tree
- Random Forest
- AdaBoost
- Naïve Bayes

#### Z-score Normalization

It transforms the data so that the feature has a mean of 0 (zero) and a standard deviation of 1. In most instances this works well, however some problems and/or certain ML algorithms requires that the data has a lower and upper bound such as 0 and 1. For that, we need min-max normalization.

#### Min-Max Normalisation

The values are transformed to a new scale with user-defined lower and upper bounds. Most often the values are 0 and 1.

This normalization tecnique together with the previous one are mostly suitable when there aren’t significant outliers in the data. If there are a lot of outliers we need to use Log Transformation.

#### Log transformation

It replaces the original values with the logarithm. The logarithm can be the natural, base 10 or base 2. It’s generally not critical which one we choose.

> PRO: the reason why the log transformation is used is because in case of significant outliers, this approach minimises the distance between the original outlier values and the rest of the data.
>
> CON: this transformation works only for positive values.

### Dataset Size

As we prepare our data, we sometimes have to reduce the size or complexity of our dataset. There are several ways of doing so. One approach is **Sampling**, which reduces the number of rows in our data. Another approach is **Dimensionality Reduction** which reduces the number of features (columns) - hence dimension or cardinality - in our dataset.

### Sampling

It’s the process of selecting a subset of the instances in the dataset as a champion for the whole. The original dataset is known as population while the subset is known as sample.

As always, there are different techniques for sampling:

Simple Random Sampling (without replacement): the instances selected from the population are no longer available to be picked up again, because are now part of the sample

Simple Random Sampling (with replacement): the instances selected from the population to create the sample are not removed. This means that we can select the same instance more than once to build up our sample. It may seem an odd way of sampling data, but it is indeed an important tecnique in ML known as bootstrapping. Bootstrapping is often used to evaluate and estimate the feature performance of a supervised ML model when we have very little data.

Stratified Random Sampling: it is like the simple random sampling approach, but ensures that the distribution of values of a particular feature within the sample, matches the distribution of values for the same feature in the overall population.

To do this, the instances are first divided in homogenous subgroups known as “strata”. Let’s say for example that we want to stratify based on gender. This means that we first need to group our population by it.

### Curse of dimensionality

It’s a phenomenon in ML that describes that the eventual reduction of the performance of a model as the dimensionality of the dataset increases. Specifically as we increase the number of features we eventually also have to increase the number of instances (rows) in the training data. if we don’t do this, the performance of our model will eventually degrade.

Most of the time it’s hard if not impossible or impractical to increase the number of instances, so the best course of action is to decrease the cardinality of the dataset to mitigate the impact of the “Curse of dimensionality”. We need to identify the optimal number of features to use.

### Dimensionality Reduction

It refers to techniques that reduce the number of features in a dataset. It’s important because it helps reducing time and storage required to process data by simplifying the

It reduces the number of dimensions of the feature space, hence the name "dimensionality reduction".

Dimensionality reduction is required to reduce the training time and memory consumption. It also helps with overfitting by simplifying the model. A model with too many degrees of freedom (a.k.a. many parameters) is likely to overfit the training dataset and therefore may not perform well on new data. Plus, a simpler dataset improves data visualisation.

Two important approachs are **Feature Selection** and **Feature Extraction**.

Worth mentioning also:

- Matrix Factorization
- Manifold Learning
- Autoencoder Methods

#### Feature Selection

Feature selection tecniques uses scoring or statistical methods to select which features to keep from the feature space.

This approach identify the minimal set of features that gives a performance reasonably close to that obtained by a model trained on all the features. The assumption is that some of the features could be redundant, irrelevant, or derivative and can be removed without having much of an impact on the performance of the model.

This approach is also know as **Variable Subset Selection**.

There are three types of feature selection techniques:

- Filter methods
- Wrapper methods
- Embedded methods

**Filter Methods**

Use scoring methods like correlation between the feature and the target variable, to select a subset of input features that are most predictive. Examples include Pearson’s correlation and Chi-Squared test.

**Wrapper Methods**

With wrapper methods, the feature selection process is based on a specific machine learning algorithm that fits and evaluate the model with different subsets of input features and selecting the subset the results in the best model performance.

Most commonly used techniques under wrapper methods are:

- Forward selection
- Backward elimination
- Bi-directional elimination (a.k.a stepwise selection)
- Recursive Feature Elimination

#### Feature Extraction

This approach uses a mathematical function to transform high-cardinality data into a lower one.

This approach result in a final set of features that are completely different from the original set. The new features are simply a projection of the original dataset.

This is why this approach is also known as **Feature Projection**.

It is a very efficient approach but it present one notable disadvantage: the resulting value of the projected new features are completely different and not easy to interpret.

## Modeling

Is the process of choosing and applying a machine learning algorithm that works well with the data we have.

In Supervised ML, the objective is to build a model that maps a given input (a set of independent variables) to a given output (dependent variable).

Depending on the nature of the dependent variable our problem can be either a Classification (for categorical labels) or a Regression problem (for continuous labels).

Some popular ML algorithm such as:

- Neural Networks (of any form of shape)
- K-Nearest Neighbors
- Decision Tree
- Naive Bayes
- Support Vector Machines

can be used to solve both regression and classification problems.

However, there exists a family of ML algorithms that are tailor-made for regression only, such as:

- Logistic regression
- Simple Linear Regression
- Multiple Linear Regression
- Poisson Regression
- Polynomial Regression

## Evaluation

Assess how well the model performs comparing the prediction with the real value in some way. There are several ways to do so.

The dataset used to test our model must be different from the one used to build it.

In Supervised Learning our goal is to predict labels, we assess the accuracy based on how well is capable to predict (i.e. measure of the error)

In Unsupervised Learning this is more of a subjective assessment. A good model is the one that provides results that makes sense to us.

Based on how well the model performs, we may need to iterate between the stages multiple times.

### Regression Evaluation

### Classification Evaluation

## Production and Monitoring

Once built a model and evaluated, we can now deploy it to production.

Exposing a model to production is not just a "place it there and let it run" operation. The model need to be monitored to make sure it keeps performing consistently. Also, the model must be updated overtime, because new information that were previously unknown can now affect future predictions.
