# Autoencoders

Autoencoder is a version of Encoder-Decoder architecture, where both the input and target domain are the same. This means that the Autoencoder learns the encoding (latent representation) of the input on a lower dimension and then tries to reconstruct it with minimal loss, to be as similar to the input as possible.

The Autoencoder is categorised as a self-supervised learning technique rather than unsupervised, because it uses the input as ground truth for training. Not all of the Autoencoder types use the input as the ground truth as we'll see.

The aim of an autoencoder is to minimise the so-called "reconstruction loss". The lower is the loss, the better the input reconstruction is.

## Undercomplete autoencoders

It is the simplest form of autoencoders. It's an unsupervised method to learn the latent space which is a compressed version of the input. The output of this network is the same as the input. A "reconstruction error" is the loss function used to quantify how much information has been lost from the input during the reconstruction of the latent space.

It uses the same image for input and ground truth.

This form of compression can be seen as a dimensionality reduction technique. Unlike PCA, autoencoders learn non-linear relationships. An autoencoder with linear activation function only can be reduced to the same level of PCA.

This sort of "dimensionality reduction" is called **manifold learning** because the encoder learns non-linear manifolds.

Being an Encoder-Decoder architecture, one can use LSTMs or CNNs.

## Sparse autoencoders

Similar to the undercomplete autoencoders, this network can be tuned by changing the number of nodes at each hiden layer. The sparsity function calculates a penalty which is directly proportional to the number of neurons being activated. This penalty acts as a regularization term.

## Contractive autoencoders


## Denoising autoencoders

This is the first type of Autoencoder that doesn't use the input image as the ground truth. A noisy version of the input image is fed into the network. The noise is added via an automatic alteration. The denoiser will learn the representation and try to reconstruct the image without noise.

The autoencoder maps the image to a lower-dimensional manifold, were filtering the image is simpler. This type of autoencoder learns the lower-dimensional encoding of the input thanks to the non-linar dimensionality reduction. The loss function in this case is either L2 or L1.

## Variational Autoencoders (for generative modelling)

This type of autoencoder express the the latent attributes learned in a probabilistic fashion. The reason for this is because the latent space is not continuous, which is makes it harder to be interpolated.

By representing the latent space with distribution, we create a continuous latent space

The primary use of variational autoencoders can be seen in generative modeling.

## Main applications

Autoencoders are mainly used for image denoising and dimensionality reduction for data visualization.

### Dimensionality Reduction

**Undercomplete autoencoders** can be used for this task.

### Image denoising

The **Denoising Autoencoder** can perform this task. They can denoise complex images that cannot be denoised by other methods.

### Generation of images or time series data

**Variational Autoencoders** can generate both images and time-series data. This is thanks to the parameterised distribution of the latent space that can be randomly sampled to generate discrete values. Time series data like music can also be generated.

### Anomaly detection

**Undercomplete Autoencoders** can be used for this task. The autoencoder has learned a lower-dimensional representation of the input dataset with minimal reconstruction loss. Reconstructing an outlier will produce a high reconstruction loss, which can easily be labelled as an anomaly.
