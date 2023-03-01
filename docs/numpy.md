# Numpy

Numpy arrays are mutable and must be a collection of values of the same type.
Numpy arrays can be made immutable by calling the `setflags(write=False)` on the array.

## Data Types

https://numpy.org/doc/stable/user/basics.types.html

## Array creation

[Array creation](https://numpy.org/doc/stable/reference/routines.array-creation.html) (deterministic):
- `np.linspace`
- `np.arange`
- `np.ones`
- `np.zeros`
- `np.eye`

[Random sampling](https://numpy.org/doc/stable/reference/random/index.html):
- `np.random.rand`
- `np.random.randint`
- `np.random.randn`
- `np.random.choice`
