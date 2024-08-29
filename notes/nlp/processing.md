# Processing

## Preprocessing

1. Tokenise: split by words
1. Capitalisation (Normalisation): the word case is normalised, i.e. transformed to lower case
1. Lemmatisation: generates lemmas for groups of words that belong to the same root. For example: "show", "shows", "showed", "showing" are grouped with the lemma "show".
1. Part-Of-Speech Tagging: tag the part of speech with nouns, verbs, adjectives. This is a tricky tasks, for example the word "show" can be both a noun and a verb, which is why this task is approached with Machine Learning techniques, such as tag prediction.

## Data Inspection

Inspect the context of a sentence around a keyword

```py
def context_search(keyword:str, dictionary:dict, span:int = 100, context_length:int = 10):
    keys = list(dictionary.keys())
    for key in keys[:span]:
        tokens = nlp(dictionary[key])
        for index, token in enumerate(tokens):
            if keyword.lower() == token.lower_:
                print(token.doc[index - context_length : index + context_length + 1])
```

Estimate the diversity of the vocabulary
  - Total number of tokens
  - Unique number of tokens
  - Lexical Richness: `LR = num_unique / total_num_words * 100`
- Frequency count and visualisation
  - Visualise a scatter plot of word ranks with the word frequency map
  - Visualise a histogram with percentage of word coverage
