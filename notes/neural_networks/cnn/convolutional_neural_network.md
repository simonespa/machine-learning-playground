# Convolutional Neural Network

## Reference
- [But what is a convolution? | 3Blue1Brown](https://www.youtube.com/watch?v=KuXjwB4LzSA)
- [Image Classification with Convolutional Neural Networks (CNNs) | StatQuest](https://www.youtube.com/watch?v=HGwBXDKFk9I)

## Benefits
- Reduce the number of inputs: the size of the input is given by the size of the image $N \times M$
- Noise tolerant: tolerates slight modifications of the image such as shifts of pixels.
- Uses pixel correlation: correlate similar pixels within the same neighborhood together.

## Steps
Apply a filter to the image through convolution (a.k.a. a Kernel). Kernels are randomly initialised and then learned during training. The convolution with Kernel creates a reduced-size 2D matrix which is called **feature map**

Feature maps groups neighboring pixels together, which is how the CNNs take advantage of pixel correlation

Run the feature map through a ReLU activation function.

Then we run another filter to the feature map, only this time we group pixels together, select the maximum value (or the average) and then slide the window to adjacent groups rather than overlapping he cells. This operation is called **Max Pooling** (or **Mean Pooling** if the mean is applied).

> Note: the max pooling selects the maximum number, signalling the portion of pixels that match the specific filter

Take the **Max Pooled** layer and flatten it to plug in as input in a Fully-Connected NN.

## Why 3x3 Kernels?

They are much more computationally efficient than the 5x5 or 7x7. By chaining multiple 3x3 kernels together, we can cover bigger patches on the initial layer at low cost. A 3x3 convolution on the first layer can only see a 3x3 patch on the original image, but a 3x3 convolution on the second layer can see a combined 5x5 patch on the input image (and so on).

The nth layers have a receptive fiedl which is combined by the overlapping of the combinations.

For example, two 3x3 convolution can see the same patched area than a single 5x5.

## Stacking channels

An RGB image of $N \times M$ dimension can be addressed with a 3D convolution operation. The kernel will have a $N \times M \times C$ size were $N$ and $M$ can be different (usually be a $3 \times 3$) and $C$ (the number of channels) must be equal. The output of this convolution will create a 2D feature map.

We can apply multipl convolution in parallel (e.g. vertical-edge and horizontal-edge detection). Both of them will create two 2D feature maps. These feature maps can be stacked together, creating a 3D feature map where the number of channels is equal to the number of parallel convolution applied to the original image.
