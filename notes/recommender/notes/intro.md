# Recommenders

## Explicit feedbacks

Users are asked to provide a rating or to react to content with pre-designed interactions to provide their level of interest.
Although the information comes directly from the user, not everyone may provide informations, or the same person may not provide info to every single content. This makes the data sparse.

Considerations:
- Sparse data
- Rating inconsistencies (differencies in people)

## Implicit feedbacks

Feedback is inferred by user interactions with the content. For example, if the user watches a video until a certain % of its duration, we may consider this interaction as an intention (positive/negative)

Types of interactions are:
- click (any website with links)
- purchase (online retailers)
- consumption (video/audio streaming platform, article website)

Considerations:
- Data are not sparse, but may be unreliable

## Top-N recommender

Return a finite list of the top N best content to recommend to the user.

Steps:
- Candidate generation
- Candidate scoring (ranking)
- Filtering: can eliminate content already consumed, an editorially curated block list for offensive or inappropriate content, remove items below a certain score level. This is also where we apply the cutoff for the top N items.

This is called item-based collaborative filtering (used by Amazon in 2003)

First step is to generate candidates, then use similarities from the datastore with other content

## Item-based collaborative filtering
Uses item similarities
