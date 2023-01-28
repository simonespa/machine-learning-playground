# Tensor Flow 2

It's an open source high-performance library for numerical computation.

Any numerical computation, not just machine learning. It can be used for any type GPU computing, for example to solve partial differential equations, very useful in fluid dynamics.

The way TensorFlow works is by creating a Directed Acyclic Graph to represent the computation. Each node is a mathematical operation, the edges are arrays of data flowing towards the output.

It is very popular. From a research point of view is heavily used for Deep Learning, and it is also sued at scale for production services.

## What is a tensor?

A tensor is an N-dimensional (or Rank N) array of uniform data type. The smallest tensor is represented by a scalar. By adding dimensions we have a vector, then a matrix, a cube, and so on.

Tensor are immutable stateless objects, you can't modify them once created.

We also need tensors that can change, which is why we can use `tf.Variable`

## Why a Directed Graph?

For portability. DAG is language-independent representation of the code in the model. It can run on CPUs, GPUs and TPus and it allows portability across multiple devices.

Language and hardware portability.

## TensorFlow Execution Engine

The TF execution engine is written in C++ and it is very efficient and targeted for a specific hardware chip.

## Portability

Train the model on the Cloud, run inference on the user device at the edge (mobile phone, Rasperry Pi, embedded chips, etc.) using TF lite.

## Concepts
- Tensors
- Variables
- API hierarchy
- tf.data API
  - input pipeline from models
- feature columns
- data preparation
- TensorFlow Execution Engine

## API Hierarchy

It goes from a set of low-level APIs for hardware to very abstract, high-level APIs for tasks like a complex Neural Network with many hidden layers using few line of codes with the Keras API.

### Layer 1: Hardware API

This layer has a set of APIs that target hardware platforms such as CPUs, GPUs, TPUs, Android, etc.

### Layer 2: C++ API

This is how we can create a custom TF operation. Implement it in C++ and then register as a TF operation. This allow TF to be extensible.

### Layer 3: Core Python API

This contains much of the numeric processing operations such as add, multiply, etc. Also, this API allows you to create variables, tensors, re-shape tensors and variables, etc.

### Layer 4: Python Modules

High level representation of useful Neural Network components (tf.losses, tf.metrics, tf.optimizers, tf.layers, etc). These modules can be combined together.

These modules are used to create custom NN models.

You will use this level of API if you want to customise the training phase with a custom NN.

### Layer 5: High-Level API

Some times you don't need a custom NN. You may just use a standard estimator with back propagation of the weights. This where Keras sits.

This layer of API provides: tf.estimator, tf.keras, tf.data.

It allows to easily create distributed training, data preprocessing, model definition, compilation and training.

Given this provides standard training models, it will fit most of your needs with sensible defaults.
