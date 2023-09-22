# Retentive Network

Paper: https://arxiv.org/pdf/2307.08621.pdf

It propose the **retention mechanism** for sequence modelling. This mechanism supports three computation paradigms: parallel, recurrent, chunkwise recurrent.

**Parallel**

It allows for training parallelism

**Recurrent**

It enables low-cost O(1) inference. It improves decoding throughput, latency and GPU memory

**Chunkwise recurrent**

Simplify efficient modelling of long sequences with linear complexity. Each chunk is encoded in parallel, while recurrently summarizing the chunks.

This paper says that Transformers are unfriendly to deployment because it makes the linearly complex O(N) during inference. By growing the sequence length, the GPU memory grows together with the latency, reducing the inference time.

## Improvements

There are 3 main paths in the research world to improve inference performance by retaining the benefit of training parallelism like Transformers.

**Linearized attention**: it approximates the standard attention scores with kernels so that autoregressive inference can be rewritten in a recurrent form.

**Return to recurrent models**: for efficient inference: it sacrifice the the training parallelism though. As a mitigation, element-wise operators are used for acceleration

**Replace attention with something else**: such as S4, presented by the "Efficiently modeling long sequences with structured state spaces" paper and its variants.

All of the above can't break the so-called **Impossible Triangle**, so no clear winner in comparison with the Transformers.

RetNet in contrast, break the impossible triangle, by achieving low-cost inference, efficient long-sequence modelling, Transformer-comparable performance, and parallel model training.

This paper introduced the so-called **Multi-Scale retention mechanism** to replace the **Multi-Head Attention**

## Comparisons

In comparison with **attention**, the **retention** mechanism removes **SoftMax** and enables recurrent formulation which benefits inference.
