# Neural Networks

## Single Layer Perceptron

This is the simplest feedforward neural network and does not contain any hidden layer.

Also known as TLU (Threshold Logic Unit)

## Types of Neural Networks

* Recurrent Neural Network (RNN)
* Feedforward Neural Network (FNN)
* Perceptron
* Convolutional Nerual Network (CNN)
* Radial basis function network
* Modular Neural Network (MNN)
* Multilayer Perceptron
* Function
* Generative Adversarial Network
* Autoencoder
* Deep belief network
* Self-organizing map
* Spiking neural network
* Long short-term memory
* Hopfield network
* Time delay neural network
* Convolutional Neural Network U Net
* Boltzmann machine
* Residual neural network
* Optical neural network
* Neocognitron
* Radial basis function

## CNN

CNNs are efficient in Computer Vision tasks such as
- Image classification
- Object detection
- Segmentation

They are not so good in NLP given images are a 2D representation of a 3D world, while text is sequential

## Sequential data

RNN => LSTM/GRU => Attention Mechanism/Transformers

### RNN

Recurrent Neural Networks are good at modelling sequential data such as: text, audio, time series data,

- suffer from short term memory, they aren't good at retaining memory long enough, hence they can't catch context in a text which is far away. Imagine a long paragraph that near the end of it references something that was explicitly defined at the beginning. This problem refers to the so called **coreference resolution** which happens when in english we use pronouns "he/she/it"
- slow during training.
- vanishing/exploding gradient

### LSTM

Long Short-Term Memory networks are able to resolve the **coreference resolution** because they retain a longer-term context in memory and are able to resolve references in text using pronouns.

### GRU



## References
- https://www.mygreatlearning.com/blog/types-of-neural-networks/

##
