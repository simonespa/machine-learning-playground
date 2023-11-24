# Autoencoders

It is a neural network architecture capable of discovering structure from the data at a lower dimension.

Autoencoder is a version of Encoder-Decoder architecture with an input, an output and a hiden layer. The Autoencoder learns the encoding (latent representation) of the input on a lower dimension and then tries to reconstruct it with minimal loss, to be as similar to the input as possible.

The Autoencoder is categorised as a self-supervised learning technique rather than unsupervised, because it uses the input as ground truth for training. Not all of the Autoencoder types use the input as the ground truth as we'll see.

The aim of an autoencoder is to minimise the so-called "reconstruction loss". The lower is the loss, the better the input reconstruction is.

## References

- https://www.jeremyjordan.me/autoencoders/
- https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73

## Types of Autoencoders

- Undercomplete
- Sparse
- Denoising
- Contractive
- Variational
- Disentangled Variational

## Undercomplete

It is the simplest form of autoencoders. It's an unsupervised method to learn the latent space which is a compressed version of the input. The output of this network is the same as the input. A "reconstruction error" is the loss function used to quantify how much information has been lost from the input during the reconstruction of the latent space.

It uses the same image for input and ground truth.

This form of compression can be seen as a dimensionality reduction technique. Unlike PCA, autoencoders learn non-linear relationships. An autoencoder with linear activation function only can be reduced to the same level of PCA.

This sort of "dimensionality reduction" is called **manifold learning** because the encoder learns non-linear manifolds.

Being an Encoder-Decoder architecture, one can use LSTMs or CNNs.

## Sparse

The difference with the undercomplete autoencoders is that this network doesn't have a bottleneck in the hidden layer. Instead, it uses a regularisation tecnique to penalise the activation of the nodes at each hiden layer. The sparsity function calculates a penalty which is directly proportional to the number of neurons being activated. This penalty acts as a regularization term.

By penalising the activation, the network does its best to minimise the number of nodes used to encode the input. This means that the latent encoding of a set of feature can have different sizes.

## Denoising

This is the first type of Autoencoder that doesn't use the input as the ground truth. A noisy version of the input is fed into the network. The noise is added via an automatic alteration. The denoiser will learn the representation and try to reconstruct the image without noise. The original input is kept as the ground truth to evaluate the network.

The autoencoder maps the input to a lower-dimensional manifold, were the filtering operation is simpler. This type of autoencoder learns the lower-dimensional encoding of the input thanks to the non-linar dimensionality reduction. The loss function in this case is either L2 or L1.

## Contractive

This type of autoencoder generates similar latent encoding for similar inputs. This means that for small changes in the input, the encoded latent state remains almost similar with very few changes. This is achieved by requiring a small derivative of the activation functions of the hidden layer.

It is similar to what the denoiser which is insensitive to the noise in the input. In this case, the minimal changes are seen as noise perturbations.

The penalty here is for large derivatives of the hidden layers activations

## Variational

The theoretical basis of this architecture are: probabilistic model and variational inference.

A variational autoencoder is an autoencoder whose training is regularised to avoid overfitting and ensure that the latent space has good properties that enable generative process.

Instead of mapping the input to a fixed lower-dimensional vector, it maps it onto a distribution. So, ather than having in the bottleneck one single fixed-size vector in the representing the latent input, a Variational Autoencoder will have 2 fixed-size vectors representing the mean and the standard deviation of the distribution. From these two vector, the autoencoder is able to generate a sample of the distribution which is fed in the so-called **sampled latent vector** which is then the input of the decoder.

<img src="./variational-autoencoder-bottleneck.png">

As for the other types of Autoencoders, this network is trained to minimise the reconstruction loss. In order to introduce some regularisation of the latent space - which is the property that will allow the Autoencoder to generate new unseen content - the input is encoded as a distribution over the latent space rather than as a single point.

This type of autoencoder express the latent attributes learned in a probabilistic fashion. The reason for this is because the latent space is not continuous, which makes it harder to be interpolated.

By representing the latent space with distribution, we create a continuous latent space.

The primary use of variational autoencoders can be seen in generative AI.

1. the input is encoded as distribution over the latent space
2. a point from the latent space is sampled from that distribution
3. the sampled point is decoded and the reconstruction error can be computed
4. the reconstruction error is backpropagated through the network

NOTE: In practice, the encoded distributions generated by the encoder are enforced to be close to a standard normal distribution, so that the encoder can be trained to return the mean and the covariance matrix that describe these Gaussians.

IMPORTANT: The encoding of the input as distributions instead of simple points is not sufficient to ensure continuity and completeness. Without a well defined regularisation term, the model can learn to "ignore" the fact that distributions are returned and behave almost like classic autoencoders (leading to overfitting), in order to minimise its reconstruction error.

To avoid these side effects, we have to regularise both the **covariance matrix** and the **mean of the distributions** returned by the encoder.

Naturally, there is a tradeoff between the regularisation term and the reconstruction loss. This is because, by regularising the Autoencoder, we are inevitably increasing the reconstruction loss.

The loss function is composed of two terms: the reconstruction loss and the KL divergence which makes sure that the distribution generated by the encoder is not to far from a normal Gaussian distribution. This means that this term ensures that the generated distribution is as close as possible to a distribution with the mean close to zero and the standard deviation close to one.

### Reparameterisation Trick

The bottleneck of the autoencoder contains a latent vector that takes a sample from a distribution, and this is a problem for Backpropagation because you cannot apply the gradient descent on a stochastic node.

The trick is to deconstruct the sampled latent vector - let's call it $z$ - in order to separate the terms you want to optimise with Backpropagation from the stochastic term that cannot be removed.

<img src="./sample-vector-deconstruction.png">

The $\mu$ an $\sigma$ are the parameters that the network learns, while $\epsilon$ is the normal Gaussian distribution. And this is ok, because we still want to have a stochastic behaviour, while now we can learn the deconstructed parameters through backpropagation.

## Disentangled Variational

It builds on top of a Variational Autoencoder, by allowing the network to learn what each value of the sampled latent vector controls (represents) in the output.

It extracts a set of causal features that describe the object from a high-dimensional input space and the hope is that those features can generalise for unseen data.

Example, if we have a set of images of faces and we train a Variational Autoencoder, if we change one value of the sample vector, the output could be something randomly different, maybe the whole face change, or the color of the hairs, etc. We don't know. With Disentangled Variational autoencoder, we know what each variable of the sample vector controls, and by changing its value, we expect only that feature to change (e.g. the rotation of the face, or the color of the hairs, etc.).

This type of network can be used in **Reinforcement Learning** where the agent can now interact with a compressed representation of the environment, described by the extracted features.

### Tradeoff

If the disentanglement is too small, the network overfits because it gives more freedom and the network learns to reconstruct the input without generalising.

The opposite case, where the disentanglent is too much (higher number of features) the network looses the ability to extract the key features to represent the input and this can hurt performances when applied in real applications.

## Main applications

- Compression of data (i.e. images & sound using CNets)
- Anomaly detection: undercomplete autoencoders can be used for this task. The autoencoder has learned a lower-dimensional representation of the input dataset with minimal reconstruction loss. Reconstructing an outlier will produce a high reconstruction loss, which can easily be labelled as an anomaly.
- Latent feature representation
- Dimensionality reduction (undercomplete autoencoders)
- Image Denoising: denoising autoencoder can denoise an image or even re-construct entire missing bits of an image with a technique called Neural Inpainting.
- Image segmentation (like in self-driving cars, the environment is segmented in different objecs)
- Image generation: variational autoencoders can generate both images and time-series data. This is thanks to the parameterised distribution of the latent space that can be randomly sampled to generate discrete values. Time series data like music can also be generated.
