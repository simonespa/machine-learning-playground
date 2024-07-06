# Words Embeddings

## Bag Of Words (BOW)

Each element of the array represent the frequency of the corresponding word in the document

This approach generates a fixed-lenght vector, but it doesn't encode any meaning.

## TF-IDF

Uses the Term Frequency and multiplies it by the Inverse Document Frequency. The term requency is as usual, how many time the word appears in a given document. The IDF instead, counts in how many documents that word appears. It's a weight that gives more importance to rare words (hence the inverse).

## Word Embedings

Embeddings are a vector representation which take context into consideration. These embedding are learned from the data, rather than representing statistical informations.

A neural network is usually trained for some kind of word prediction task.

## Word2Vec

Method developed by Google in 2013. It's a neural network architecture that it's implemented in two variants:
- Continuous Bag Of Word (CBOW)
- Skip-gram

It's a shallow Neural Network that has:
- Input Layer
- Projection Layer
- Output Layer

### CBOW

Predicts a word, given the context.

We define a window size, which defines the surrounding words (the context) of the surrounded word we want to predict.

Each word is One-Hot encoded.

### Skip-gram

Predicts the context, given a word.
