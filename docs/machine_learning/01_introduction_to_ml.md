# Introduction to Machine Learning

Machine Learning is a sub-field of Artificial Intelligence, while Deep Learning is a sub-field of ML.

- The main objective of Machine Learning is to make predictions and answer the “What’s next?” question.
- Data Science includes: Machine Learning, Data Mining, Optimisation
- In the field of “Business Analytics”, Machine Learning is also known as “Predictive Analytics” whereas Data Mining is also known as “Descriptive Analytics” and Optimisation is also known as “Prescriptive Analytics”

- **Descriptive Analytics**: tracks and analyses existing data in order to identify new patterns
- **Predictive Analytics**: analyses past trends to predict the likelyhood of future outcomes
- **Prescriptive Analytics**: recommends actions based on prior performances

## Machine Learning Approaches

Machine learning is often categorized by the methodology used during the training stage. There are three fundamental approaches according to this distinction:

- supervised learning
- unsupervised learning
- reinforcement learning

Another approach often described is **semi-supervised**, which is a mix of both supervised and unsupervised.

### Supervised Learning

It's the process of building a predictive model. Predictive models are used to assign labels to unlabeled data based on patterns learned from previously labeled historical data.

Supervised machine learning models are generally used to predict outcomes for unseen data. This could be predicting fluctuations in house prices or understanding the sentiment of a message.

This approach uses labelled data to train the model. The label in a dataset is a specific feature associated with historical data that we want to predict. The model learn patterns in previously labeled data.

Before using the model for prediction, we need to build it (train it) with past information.

Independent variables are the information in input, the dependent variable is the labeled output.

Once the model is trained, it must be tested to evaluate the percentage of Predictive Accuracy (i.e. the quality of the prediction).

Deep Learning is an example of supervised learning approach.

Applications

- Image recognition
- Text prediction
- Spam filtering
- Loan outcomes

#### Example: Loan Outcomes

Suppose we want to predict the loan risk of individual customers based on the information provided on their loan application, in order to know whether the customer will or will not default with the risk of not returning the money back.

Information we have:

- Descriptive information of past loans (amount, purpose, income, etc.)
- The outcome of the past loans.

### Unsupervised Learning

It's the process of building a descriptive model. Descriptive models are used to summarise and group unlabeled data in new and interesting ways.

With this approach, models discover emerging patterns (i.e. hidden structures in data) and group them together.

Evaluate the input data and identify any hidden pattern or relationship that exists in the data

Unsupervised machine learning is mainly used to:

- Cluster datasets on similarities between features or segment data (customer segmentation, market-basket analysis)
- Understand relationship between different data point such as automated music recommendations
- Perform initial data analysis

#### Example: Customer Segmentation

Suppose we want to group our customers on how similar they are in order to better target them with our product.

- Historical information about their behaviour
- Demographic information

### Reinforcement Learning

It's a reward-based learning and it works on the principle of feedback.

Attempts to tackle 2 distinct objectives:

- Finding previously unkown solutions to a problem (i.e. a machine that learn to play a game like chess)
- Finding online solutions to problems that arise due to unforseen circumstances. Example, a machine that recalculate an alternative route due to a change in the plan.

It’s the science of learning to make decisions from interaction or the process of learning through feedback. This approach is very similar to early child learning (trial and error).

There are two primary entities:

- the **agent**: takes actions in the environment
- the **environment**: gives feedback to the agent

The agent figures out the best way to accomplish a task through a series of cycles in which the agent takes an action and receives immediate positive or negative feedback on the action from the environment. After a number of cycles, the agent eventually learns the optimal sequence of actions to take in order to accomplish the task at hand. Reinforcement learning is commonly used for:

- Gaming
- Trading
- Robotics
- Autonomous driving

The feedback provided by the environment comes in two forms:

- **State**: describe the impact of the agent’s previous actions on the environment and the possible actions the agent can take
- **Reward**: each action is associated with a numerical reward that the agent will get if the action is taken

The objective of the agent is to maximise the sum of rewards over the long term.

#### Exploitation vs Exploration tradeoff

- **Exploitation**: the agent chose the action that maximises reward
- **Exploration**: the agent chose the action with little to no consideration of the associated reward

An agent that focuses only on Exploitation, will only solve problems has previously encountered
An agent that focuses only on Exploration, will not learn from prior experience.
A balanced approach is needed for an effective reinforcement learning.
