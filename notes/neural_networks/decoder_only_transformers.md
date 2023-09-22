# Decoder-only transformers

A decoder-only transformer can take an input prompt and generate a response.

We need to transform all the words in the prompt into numbers using embeddings.

The decoder-only transformers have something called **Masked Self-Attention**. As well as the **Self-Attention** it helps associating words relationship within the sequence. The difference with this "masked" version is that for each word, the self-attention similarity is calculated with itself and all of the preceding words in the sequence (not tacking into account what appears next). Each word looks at itself and the words that came before it (but not after).

Because "masked self-attention" only allows access to to the words that come before it and not the ones that come after, it is sometimes called an **auto-regressive** method.

With GPT they stacked 12 Masked self-attention cells.
In the original GPT definition, instead of connecting the residual connection values to plug them into a fully connected NN, they re-used the embedding layer but in reverse, to help decode the numbers

The masked self-attention used in decoder-only transformers includes the token from the prompt and the output, while in encoder-Decoder transformers, the masked self-attention only includes the token within the output.
