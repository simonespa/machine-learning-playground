# Notes

- Shorter content mixed with long ones
- The recommender should decide:
  - which items are grouped together and their order
  - which groups are listed together and their order
  - how many items in a group and/or how many group in a page??? (to be validated)
  - should the groups of items be created dynamically by clustering recommended content under different categories, or should they be selected (still based on recommendation) from a large but predefined set? If the latter, should the preset be defined in type (e.g. because you liked ..., category-based, based on who is featured in it, based on mood, a combination of those) but dynamic in content??? (to be validated)



### Overrides

The human intervention is injected in the output itself and it could remove/add content, change the order of things, etc. This allows for correcting mistakes in the output due to many factors (unintended correlation between content that may damage the reputation or upset the user), or force certain content regardless of the recommendations for promotion (override the most prominent place in page to promote some content).

### Hints

The human intervention suggests certain content groups or specific items to the recommender system to take into consideration. This helps with the exploration of new content that otherwilse the algorithm would've not taken into consideration.

## Choice overload vs Choice deprivation

Choice overload happens when people are overwhelmed by the amount of choices to make compared to how many they really need or can cope with. On the other side of the medal we have choice deprivation. Deprivation happens when there are so few flavours that their likelihood of content consumption decreases.

 While choice deprivation is the opposite situation.

Users experience choice overload vs. choice deprivation in different ways, at different ratios at any given time, based on different factors that could be either latent or temporarily induced by external factors. The hypothesis is that this may have a detrimental effect and represent a friction factor that reduces the consumption rate of a given set of content.

The assumption here is that some times, users like or need to be directed towards what to consume and/or have the least amount of choices possible that keeps them from consuming the content. This assumption is not an intrinsic feature of a user, but rather a temporary mode of consumption guided by some external factor. To clarify, it's not a trait of a person who likes to be told what to consume, but rather a temporary state of mind.

This is the scenario where the user is exposed to a simplified version of the recommendation output, where there are few to no choices at any given time.

There may be different factors that may cause this behaviour, which we can speculate about:
- Is it be because a person is tired from the daily routine and they just want to relax by tacking the least amount of choices?
- Is it because of the excitement to discover new content in a "russian roulette" fashion in the case of no-choice scenario?
- Is it because of choice overload (more than desired or we can cope with) may cause a range of feelings that negatively impact the desire to consume the content? For example, a lot of choices can push a person towards a wide range of feelings: frustration of not knowing what to consume to total confusion, or regret of having chosen one content over another even though the current one is enjoyable, dissatisfaction of the current choice knowing there could be better out there, even choice paralysis where the user mindlessly scans almost the entire catalog without selecting anything in the end. Reference: https://www.taylorfrancis.com/chapters/edit/10.4324/9781315658353-50/cognitive-affective-consequences-information-choice-overload-elena-reutskaja-sheena-iyengar-barbara-fasolo-raffaella-misuraca

The no-choice scenario is a subset of the simplified version, where the user is presented with just one content at a time. If the user doesn't like the content, the next one can be selected so the user can decide whether to consume it or not. No choice doesn't mean no content. The user can still go through a list of items selected by the recommender, the absence of choices describes the fact that the recommender decides what to consume, the user decides whether or not they consume it or go for the next item.

Wbat on the surface appears as a "mindless", "no-bother", "take-it-easy" approach, it is in reality an implementation of a frictionless strategy that builds on top of the hypothesis of choice-overload may cause reduction in consumption rate in certain users in a certain amount of time.

This extreme "no-choice" case could be tested as an experimental feature that users can opt-in if they like. Gathering interaction and consumption informations will help validate or reject this hypothesis.

just few things. This only works for people who are inclined towards the undecisevness. Some people like to be told what to consume so they don't have to. This doesn't mean they may certainly like the content, but it helps with exploration.

### Sense of guilt with information overload

The performance of the chosen content seems/appears mediocre in comparison with the unknown. You have chosen something and you are wondering: "what if I did choose something else?"

## Explore new content
- Human intervention: hints and overrides
- Cew choice scenario. Imagine the situation where they can press a button and select the next thing to watch. They can either keep going, or select a new item and consume it. All these interaction will inform whether this person is likely to be inclined towards exploration of new content

## Keep the user engaged
- The content

## Notes

Understand whether a user is up for
- Shorter content, to consume more in a smaller amount of time
- Exploring new content, so that we can sometime expose to "risky unkowns" to experiment whether we can create a future long-lasting engagement
