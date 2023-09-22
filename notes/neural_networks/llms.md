# Large Language Models

Ref: https://lena-voita.github.io/nlp_course.html

RNN -> LSTM + Word Embeddings (Word2Vec) = Sec2Sec Encoder-Decoder -> Attention -> Transformer

## Encoder-Decoder LSTM

Also known as Sequence-to-Sequence (Sec2Sec)

- Input and output of variable length
- Uses RNN (LSTM or GRU) or Convolutional NN
- Each LSTM is unrolled for each input word embedding
- You can add multiple LSTM cells that share embedding in input
- You can add multiple layers of LSTM cells that take in input the output of the short-term memory (hidden state)

The encoder takes the input sequence and encodes it into a fixed-length vector (the context vector)
The decoder takes the fixed-length vector and transforms it in the output sequence

The innovation of this model is the fact that, although the input and output sequences can be of different size, the internal representation of the sequence is of fixed size.

Long-term memory => cell
Short-term memory => hidden state
Context vector => the last long and short memory outputs from bothh layers form the so-called Context Vector

- The Context Vector is used to initialise the LSTMs in the Decoder
- The input of the Decoder comes from the word embedding layer of the target vocabulary that starts with EOS
- The predicted word is then fed in input to the next unrolled LSTM, and this keeps happening until the NN predicts EOS.
- The original paper describes an embedding of dimension 1000 with 4 layers and 1000 LSTM cells
- Also, the output layer has 1000 inputs (from the 1000 LSTM cells) and an output of 80000 to match the size of the output vocabulary

One or more LSTM layers can be used to implement the encoder model. The output of this model is a fixed-size vector that represents the internal representation of the input sequence. The number of memory cells in this layer defines the length of this fixed-sized vector.

As with the Vanilla LSTM, a Dense layer is used as the output for the network. The same weights can be used to output each time step in the output sequence by wrapping the Dense layer in a TimeDistributed wrapper.

This architecture works best with with short sentences.

Example in Keras

```
model = Sequential()
model.add(LSTM(..., input_shape=(...)))
model.add(RepeatVector(...))
model.add(LSTM(..., return_sequences=True))
model.add(TimeDistributed(Dense(...)))
```

### Applications

- Machine Translation, e.g. English to French translation of phrases.
- Learning to Execute, e.g. calculate the outcome of small programs.
- Image Captioning, e.g. generating a text description for images.
- Conversational Modeling, e.g. generating answers to textual questions.
- Movement Classification, e.g. generating a sequence of commands from a sequence of gestures.

## Problem with vanilla Encoder-Decoder

LSTMs work very well if your problem has one output for every input, like time series forecasting or text translation. But LSTMs can be challenging to use when you have very long input sequences and only one or a handful of outputs.

This is often called sequence labeling, or sequence classification.

Some examples include:

- Classification of sentiment in documents containing thousands of words (natural language processing).
- Classification of an EEG trace of thousands of time steps (medicine).
- Classification of coding or non-coding genes for sequences of thousands of DNA base pairs (bioinformatics).

In a basic encoder-decoder, unrolling the LSTMs compresses the entire input sentence into a single context vector. This works ok with short sentences. But if we have paragraphs, entire pages of text or books to translate for example,

For longer phrases, words that are input early can be forgotten.

Basic RNNs run both long and short-term memories through a single path. LSTMs fix this problem by providing two separate paths for them.
Even with separate paths though, if we have a lot of data, both paths have to carry a lot of information and this means that words at the start of the sequence can still get lost, because of the compressed fixed-size internal representation of the input.

## Encoder-Decoder with Attention

The main idea of "Attention" is to add a new set of direct path from the encoder to the decoder, one per input value. By doing so, the decoder can directly access the input values, no matter the length of the sequence.

One of the main difficulties of LSTM sequence to sequence models is that they have to encode the entire input sequence into a fixed-length vector, which may lose some important information or context. To overcome this limitation, you can use attention mechanisms, which allow the model to dynamically focus on the relevant parts of the input sequence while decoding the output sequence. Attention mechanisms can improve the performance and accuracy of the model, especially for long and complex sequences.

**Definition**: Attention determines how similar the outputs from the encoder are at each step to the outputs from the Decoder, by calculating a similarity score between each output from the Encoder with each step of the Decoder.

Example:

Input sequence: Let's go
Output sequence: andiamo (1 LSTM cells)

In this example, we will have 2 LSTM units in sequence, the output of which will be used to calculate the similarity score for each step of the decoder, in this case only 1.

Let's say we had N steps in the decoder, for each step from 1 to N, we would calculate as many similarity score as there are outputs in the encoder, in this case 2.

**Similarity Score**: it is calculated using the Dot Product, which is the numerator of the full equation of the cosine similarity. The reason why the Dot Product is used instead of the Cosine Similarity, is because is computationally efficient (because there is less math to do), and the outcome doesn't change, because all the denominator does is to scale the score between -1 and 1.

The magnitude scaling it's only useful in case we need to compare the score between different models that use a different number of LSTM cells for example. In that case, the number would be comparable.

The dot product multiply each element pairwise and then sums each result. The resulting value is the similarity score.

We start calculating the similarity score of each word from the encoder with the first step of the decoder. The resulting values will go through a Softmax activation function which will determine what percentage of each encoded input word we should use when decoding. To do so we scale the output of each LSTM from the encoder by multiplying with the related SoftMax utput that represent the percentage. Finally, we add the scaled values together which combines the separate encoding for the input words relative to their similarity with the first step in the decoder. The output it's a vector with a dimension equal to the number of LSTM cells on each layer. These represent the so-called **Attention Values**.

The final step is to plug the attention values, together with the output of the LSTM in the first step of the Decoder into a Fully Connected Feed Forward Neural Network. Each input nodes is fully connected with the next layer of nodes which then run the value through a SoftMax activation function to select the next word in output.

### TLDR

- We use Similarity score and SoftMax to determine what percentage of each encoded input word should be used to help predict the next output word.

## Transformers

Word Embedding + Positional Encoding

**Positional encoding** uses sine/cosine functions with varying period. The y value of each function is used to sum to the word embedding value corresponding position. Each function corresponds to a word embedding position, spaced points on the X axis of each function is used to positional encode each word embedding from the input. By doing so, the input sequence can be as long as possible, the function will always have an X value to encode the embeding.

**Self Attention** calculate how similar each word is to all of the words in the input sequence, including itself. Example: The dork barked at the moon, it was shiny. Does shiny refer to the "dog" or the "moon"? Self-attention will work this relationship out.

If the pronoun "it" is commonly associated with the subject "dog" rather than the object "moon", the similarity score for "dog" would have a bigger impact on how the word "it" is encoded.

**Query, Key, Value** calculation.

For each positional encoding array, we calculate new set of arrays with the same dimension of the positional encoding one. For each of them we calculate the **Query** and the **Key** by multiplying the encoding values by weights and summing them together.

Now, we calculate a similarity score between each query and all of the keys (including the one that describes the word itself) using the Dot Product, passing the final value through the SoftMax function. Among these values, the bigger one will have much more influence on the encoding of the word than the rest. To do so, we create another vector of values with the same dimension of query and key for each word, using the same mechanism of weights multiplication. We then multiply them by the output of the SoftMax function to scale the values and sum them together to calculate the final vector of values called the **Self-Attention values**.

Now we do this same thinkg for the second word, the third and so on. The good news is that we don't have to re-calculate the query, key and values, because we already calculated them.

To recap:
- Calculate the similarity score between the **query** and all the **keys**
- Run the similarity scores through **SoftMax**
- Scale the **values** by the SoftMax output and add them together to calculate the **self-attention values**

- **Positional encoding** keeps track of each word position
- **Self-Attention** keeps track of the relationship among words

Note 1: this model architecture re-use the same set of weights among queries, as well as keys and values.
Note 2: query, keys and values for each word can be calculated in parallel

The self-attention values for each word contain encoded input from all of the words in the sequence, which helps giving context to the encoded word.

**Multi-head attention**: it's created by stacking multiple self-attention cells (each with its own set of weights) in order to correctly encode how words are related in more structured text such as paragraphs and chapters.

Last thing to do is to get the **position encoded values** and add them with the **self-attention values**. This bypasses are called **Residual Connections** and make it easier to train complex neural networks by allowing the

The main elements of the encoder part of the transformer are:
- Word embedding: to encode words into numbers
- Positional encoding: to encode the position of the words within the sentence
- Self-attention: to encode the relationship among the words (both for the input and output sequence)
- Encoder-Decoder attention: to keep track of relationship between the input and the output sequences, to make sure important words in the input are not lost in translation
- Residual connections: to allow each sub-unit to focus on solving just one part of the problem. It allow the network to train in parallel.

**Encoder-Decoder Attention**: it's a mechanism to keep track of the relationship between the input words and the output. This mechanism allows the decoder to keep track of the significant words in the input.

In order to do so, we use the "Residual Connection" values of the EOS token in the Decoder to create a set of value that represent the "Query". Then we create the keys for each word in the encoder. From here it's the same mechanism, we calculate the similariity between the query and the keys by using the dot product. We then run the output to SoftMax to calculate the percentage. Once we have the percentage, we calculate the set of "Value" for each word in the input, and we scale them by the percentage generated by SoftMax, then we add the pairs of scaled values together which represent the **Encoder-Decoder attention values**.

Also in this case, we add another set of **Residual Connection values**. This allows the Encoder-Decoder Attention to focus on the relationship between the output words and the input without having to preserve the Self-Attention or word and position encoding.

The residual connection values are then plugged directly in a fully connected NN with 1 input layer directly connected to the output layer. The values are multiplied by weights, all scaled input are then added together, summed to a bias and passed through a SoftMax activation function which returns the predicted word that should come next.

### Training and Attention

During inference, the Attention is used taking into account all the words before and after the one being considered. During training instead, a transformer uses **Masked Self-Attention** in the **Decoder**.

For example, during training in the decoder, we know the output should be "Andiamo <EOS>". This means that we don't have to decode the initial <EOS> before we decode "Andiamo" like we do when we generate new output.

Since we know we are going to decode "Andiamo" we run the computation in parallel with the <EOS> token. This allow for parallelism and a faster training time.

To recap, during training, an Encoder-Decoder transformer uses masked self-attention for the tokens in the known output. This allows the transformer to learn how to generate the output without looking ahead.
