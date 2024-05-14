# Convolution

The convolution is a binary operation that can be applied to sequence of numbers or generally to combine functions.

The convolution of two sequences produces another sequence, which is the sum of the products of the elements of the two sequences, where the second sequence has been flipped and slided under the first sequence.

The two sequence don't have to have necessarily the same dimension.

## Notation

$(a * b)_n = \sum_{i+j = n}{a_i \cdot b_j}$

## Example

a = (1, 2, 3)
b = (4, 5, 6)

To do so, you have to flip the second sequence, so it becomes $(6, 5, 4)$, so you have

(1, 2, 3) and (6, 5, 4)

Now, align the two sequences where the first element of "a" corresponds with the last element of "b"

      (1, 2, 3)
(6, 5, 4)

which makes $1 \cdot 4 = 4$

then slide the second sequence

   (1, 2, 3)
(6, 5, 4)

so now you have: $1 \cdot 5 + 2 \cdot 4 = 5 + 8 = 13$

(1, 2, 3)
(6, 5, 4)

which is $1 \cdot 6 + 2 \cdot 5 + 3 \cdot 4 = 6 + 10 + 12 = 28$

(1, 2, 3)
   (6, 5, 4)

which is $2 \cdot 6 + 3 \cdot 5 = 12 + 15 = 27$

(1, 2, 3)
      (6, 5, 4)

and finally $3 \cdot 6 = 18$

So, the convolution of the two sequences is the following: $(a * b) = (4, 13, 28, 27, 18)$

## Applications

This operation is applied in different fields, notably in probability distribution, and image classification/detection in Machine Learning.

In probability distribution, convolution is used for example to calculate the probability of a certain number to be the sum of two dice, in general, it is used to add the probability distribution.

It can also be used to calculate the moving average of two sequences, as long as the values of the second sequence sum up to 1. The second sequence doesn't have to have the same dimension of the first one.

Notably, if the convolution is applied in 2D, it can be used to create a blurred version of an image for example, or any other effect/filter that can be applied. In this case we have a convolution of two matrix, where the second matrix represent the filter (also called the kernel). Also in this case, the values in the matrix have to add up to 1.

In the 2D example, the second matrix is actually a 180 degree rotation of the original one, similar to the 1D case, where the sequence is flipped.

IMPORTANT: in the case of the moving average, the sequence (or the matrix), has value that add up to 1. But it doesn't mean that it should always be like this. We could for example have a matrix where the values add up to 0 for example. Also, the value can be all the same, or we can give more importance to one value in particular (e.g. the one in the middle and less to the other, or they can hav e

## Python Libraries

```py
import numpy as np

np.convolve(list1, list2)
```

or

```py
import scipy.signal

scipy.signal.fftconvolve(list1, list2)
```

## Performant Operation

Convolution itself is quite computationally expensive, you have to do pointwise multiplication for each element of the sequence, and then sum the ones that overlap during the sliding of the sequence. Or, if you think in terms of the matrix, if the matrix is NXM, you'll have to do N times M multiplication to fill all the cells, and then you'll have to sum the values in each diagonal, so in the end, we have a N squared complexity.

A more performant way to do convolution is to think in terms of polynomial.

We can reduce the convolution operation to the resolution of a system of equations that involve multiple polynomials. In graphical term, it correspond in finding the coefficient of the equation, by sampling the function at multiple points, so we have enough to calculate the coefficients.

The problem is, even if we map the problem to a system of equations, the mapping itself plus the resolution of the equation will have a similar complexity to the convolution, so it would seem useless.

For this reason, we can employ a trick, and use the Fourier Transform and the FFT algorithm. Not going into details here, but you should lookup the Discrete Fourier Transform of the coefficients. See also the Fast Fourier Transform.

The important thing to point out here is that, rather than calculating the convolution in N squared steps, we'll do the same in N log N, by using the FFT method, by simply exploiting the redundancy created by the careful selection of the coefficients, that helps shaving the number of operations required.

### To Sum Up

When we have two very long list to convolve, we can:

- Compute the Fast Fourier Transform of each list, by treating them like coefficients of a polynomial and evaluating it at a very specially selected set of points
- Multiply pointwise the two results from the previous step
- Compute the inverse Fast Fourier Transform, which gives us the convolution
