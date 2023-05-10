# Principal Component Analysis

1. Calculate the center of mass of the dataset by calculating the mean for each dimension and selecting the corresponding datapoint.
2. Shift the dataset moving the center of mass of the dataset on the origin of the frame of reference.
3. Draw a random line passing through the cener of mass (i.e. the origin now)
4. Project each datapoint onto this line orthogonally
5. To find the line of "best fit" you need to rotate this line around the origin to maximise the sum of the distances of these projected points to the origin, or minimise the sum of the distances of the original datapoints with respect to the projection on the line.

NOTE 1: to prove that maximising the spread of the points is equivalent to minimise the distances, we can use the Pythagorean theorem that statse $a^2 = b^2 + c^2$. Given that `a` (which is the distance of the datapoint wrt the origin) doesn't change and that `b` and `c` are inversely proportional, if the distance `b` decreases, the spread `c` increases and viceversa.

NOTE 2: Conceptually we would minimise the distance, but PCA actually maximise the spread of the projected points, because it's easier to calculate the distance from the origin.

The process is iterative and consist of:
a. Measure all the distances `d_i`, square them (so negative values don't cancel out positive ones) and sume them up. This value is the **sum of the square distances**.
b. Rotate and measure the **SSdistance** again until it is maximised.

The line that maximises the spread of the projected datapoints wrt the origin is called **Principal Component**. There is one principal component per dimension. A dataset of N features will have N principal components from 1 to N.

c. Calculate the slope of the principal component. Let's say it's 0.25, this means that for every 4 unit of movement along the positive X axis, we go 1 unit up the positive Y axis. The ratio is 4:1 for the X axis with a magnitude of movement along the X axis bigger than the one along the Y axis. This means that the data are mostly spread out along the X axis, and the spread or variance is explained mostly by this direction.

The 4:1 ratio I mentioned is called **linear combination" of X and Y axees.

d. Once calculated the ratio (e.g. 4:1), we have the coordinate of a point, in this case (4, 1). This point has a distance from the origin. We can use the Pythagorean theorem to calculate this distance. In this case the distance is 4.12. When we do PCA using SVD (Singular Value Decomposition), the distance from the origin is scaled to 1.

e. To scale the distance we divide each side of the triangle (Pythagorean theorem) by the distance of this point from the origin. This changes the values of each side of the triangle, making the distance equal to 1, and the new scaled value too. This changes the value (e.g. 0.97 and 0.242) but not the ration which is still 4:1 in this case.

**IMPORTANT**: this unit-1 vector we calculated made of 0.97 parts of X and 0.242 parts of Y, is called **Singular Vector** or **Eigen Vector** for the principal component. The proportion we calculated (0.97 and 0.242 for example) are called **Loading Scores**. The average of the sum of the squared distances of the projected points from the origin is called **Eigenvalue** for the Principal Component, while the square root of this average is called **Singular Value** for the Principal Component.

**NOTE**: once we calculate the PC1, we calculate the second PC and so on. Each principal component is orthogonal to the previous PC.

Once we find all the principal component, we can simply rotate them all until they coincide with the X/Y axis. Then, take the projections and calculae the new datapoints in the new frame of reference.

##IMPORTANT**: the **Eigenvalue** corresponds to **Variation** (their formula is the same). This means that we can sum all the Eigenvalues. How do we calculate it? Example: let's say we have `PC1 = 15` and `PC2 = 3` this makes a total variation of `18`. This means that PC1 accounts for $\frac{15}{18} = 0.83 = 83%$ of the total variation around the principal component wherease PC2 accounts for $\frac{3}{18} = 0.17 = 17%$ (or $1 - 0.83$) of total variation.

## Scree plot

It's a bar chart that represents the percentage of variation that each PC (on the X axis) accounts for, with the percentage on the Y axis.
