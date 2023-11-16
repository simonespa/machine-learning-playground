# Project

## Importance of contextual data

Recommendations are actions taken at a moment in space and time. The space and time signals are strong predictors in recommendations.

As shown by Netflix, using the discrete representation of time (hour of day, day of week, etc.), there was a significant improvement in ranking. By using the continuous representation of time (e.g. timestamp), the improvement was of several order of magnitude better than the discrete one. By using both, there was an extra significant improvement over the previous one.

## Problem framing

We could think of the recommendation ranking as a sequence problem.

Given in input the history of action of a user, predict the next action using a probabilistic model (e.g. RNN, Transformer).

An action is made by information about the user, location, device used, time.

Another approach could be using Deep reinforcment learning. It helps with long-term engagement, to avoid keeping the user stuck in a filter bubble.

## Nvidia Merlin

- Merlin: https://developer.nvidia.com/merlin

- Merlin on AWS: https://www.nvidia.com/en-us/on-demand/session/awsreinvent2020-aws1013/
- Article: https://www.nvidia.com/en-us/glossary/data-science/recommendation-system
- Repo: https://github.com/NVIDIA-Merlin/Merlin
- To Do: https://nvidia-merlin.github.io/Merlin/stable/examples/index.html
