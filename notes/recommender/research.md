# Introduction

In a recommender setting, there are mainly two opposite scenarios: the user is willing to search for the right content among many personalised choices or not in a mood to search and scroll but happy for the recommender to come up with something. There are actually other scenarios, but they are all the combinations in between.

This has to do with the "Choice overload vs Choice deprivation".

# Type of rails

## Hero

This is the most prominent promotion of content. It's the top-most visible and it could take the enntire area. It only promote one item.
This item could be:

- fully personalised from the entire catalogue
- an editorial promotion
- personalised content from an editorially curated list
- personalised (either from the entire catalogue or from an editorially curated list) with editorial intervention through Hinting.

## Continue Watching for X

A rail that lists the content in progress.

## My List (My programmes, etc.)

A list of items being added to a personal list of favourites. This list allows the user to express an explicit preference. This information can be used as a signal for content recommendations.

## Trending/Popular/Top 10

This is a popularity rail from:

- the entire catalogue
- an editorially curated list

## Trending/Popular/Top 10 in X (your region)

As for the Trending rail, plus it's further filtered by region of watch.

## Because you watched X

Returns similar content to the one being used as the seed.

- Uses content similarity to rank the items
- Sources from the entire catalogue or a curated list

## Because you liked X

Same as "Because you watched" but it consider the "liked" action

## Category/Genre/Format/Tags rail

This rail shows content sharing the same category/genre/format/tag and rank them based on some personalisation approach:

- Based on collaborative filtering and what other users have watched?
- Sources from the entire catalogue or a curated list

## New releases

Should show new content being made available (movie, entire series, part of a series, etc.)

## Top Searches

Contains a ranked list of top content being searched within the app. Parameters for this rail is:

- The span of time to consider the top search from
- Whether to include all searches or searches from similar users (using user similarity)

## Platform Original

Original content from the provider (e.g. BBC, Netflix, etc.)

# Configuration

There should be a set of rail types the Recommender can generate its output from. The type, the number of rails of the same type, and the order in page should be decided by the Recommender by default.

## Guardrails

Editorial should have ultimate control over the output of the Recommender System presented to each single user at scale, for peace of mind, regulation compliance or to correct it when considered wrong, inappropriate, offensive, discriminative, partisan, damaging to reputation, harmful, etc.

Guardrails are rules applied on the input of the Recoomender System or on its output. They can be of two types: overrides or hints.

A rule is a triplet <X, Y, Z> composed by an action X on content Y for audience Z.

There are two types of rules: input and output. The input rules are **hints** to the Recommender that modify the weight of the recommendation in favour or against but it's ultimately the Recommender System to have the final say. The output rules are **overrides** and they are meant to modify the actual output of the Recommender to give ultimate control and peace of mind to editorial

## Content

The content could be:
- A rail type
- A specific instance of a rail type
- A specific content

## Audience

The audience can be:
- Everyone
- A subgroup filtered by some criteria (e.g. age group, etc.)

## Actions

Actions can be groupd as hints and overrides.

The hints are promote and demote, while the overrides are

**Promote** tells the Recommender to increase the importance of a certain content.

Editorial should be able to control the Recommender System in two ways. They should be able to influence the input by assigning weights to content for specified  and controlling the output
- They can intervene over the input by means of hints. They can ask the RecSys to promote, demote
-



Editorial should be able to: override, boost, demote and hide content by specifying the target (the what) and the audience (the who).

More than one action can be enabled at the same time, as long as they don't overlap.

E.g.
- override the position of X for all users (sort of editorially curated promotion for everyone)
- override the position of X for a certain age group (targeted promotion)
- boost X for everyone. The algorithm will give more weight to this content but it's up to the Recommender to rank it based on other factors. This is can be considered as a hint for the recommender or a soft override.

## Override

The override action should allow editorial to:
- override the absolute position of a rail to a specified index for all users or a sou
- override

- The type of rails should be selected by the RecSys by default
- The rails should be ranked by the RecSys by default
- The content of the personalised rails should be ranked by the RecSys by default

## Rail position

It can be overriden or boosted for all users or just for some groups of users.

The override can be achieved by specifing an index. The rail will then appear on that position.
The boosting can be achieved by selecting the "boost" flag. The rail type will have a boosted weight, but it's then up to the algorithm to decide where to place it based on ranking.

## Number of rail of the same type

Certain rails may be capped if needed to give some control to editorial on how many of them the algorithm will rank.

# Parameterisation

Editorial should be able control set a desired threshold for certain important parameters:

- Coverage
- Diversity
- Novelty
- Churn
- Responsiveness
