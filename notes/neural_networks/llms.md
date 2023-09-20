# Large Language Models

RNN -> LSTM + Word Embeddings (Word2Vec) = Sec2Sec Encoder-Decoder -> Attention -> Transformer

## Sec2Sec Encoder-Decoder with LSTM

- Input and output of variable length
- Uses RNN (LSTM or GRU) or Convolutional NN
- Each LSTM is unrolled for each input word embedding
- You can add multiple LSTM cells that share embedding in input
- You can add multiple layers of LSTM cells that take in input the output of the short-term memory (hidden state)

Long-term memory => cell
Short-term memory => hidden state
Context vector => the last long and short memory outputs from bothh layers form the so-called Context Vector

- The Context Vector is used to initialise the LSTMs in the Decoder
- The input of the Decoder comes from the word embedding layer of the target vocabulary that starts with EOS
- The predicted word is then fed in input to the next unrolled LSTM, and this keeps happening until the NN predicts EOS.
- The original paper describes an embedding of dimension 1000 with 4 layers and 1000 LSTM cells
- Also, the output layer has 1000 inputs (from the 1000 LSTM cells) and an output of 80000 to match the size of the output vocabulary
- During training, the deco

This architecture works best with with short sentences.

## Encoder-Decoder with Attention

In a basic encoder-decoder, unrolling the LSTMs compresses the entire input sentence into a single context vector. This works ok with short sentences. But if we have paragraphs, entire pages of text or books to translate for example,

For longer phrases, words that are input early can be forgotten.
