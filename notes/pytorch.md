# PyTorch

PyTorch has 2 APIs: Python and C++

## Extensions
- [Captum](https://captum.ai/): Model interpretability for PyTorch
- [PyG](https://pyg.org/): PyTorch Geometric for Graph Neural Networks (see also PyTorch Geometric for Graph Neural Networks)
- [Skorch](https://skorch.readthedocs.io/en/stable/): Scikit Learn compatible NN library wrapper for PyTorch

## Libraries
- Torchaudio
- Torchtext
- Torchvision
- Torchserve
- Torch_xla

## Top features
- Tensors
- Autograd
- APIs
- Libraries

## Data
The DataSet and DataLoader class are the main ones.

## Autograd

Automatic Differentiation Engine

Neural Network training has 2 phases.

Forward Propagation: the input is passed through all the layers, computed with all the parameters and passed through all functions to generate an output

Backward Propagation it's made by 3 steps:
- Traverses backward from the output to the input
- Collects derivatives of the error with respect to the parameters of the functions
- Optimises the parameters using stocastich gradient descent
