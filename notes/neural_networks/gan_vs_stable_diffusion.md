# GAN vs Stable Diffusion

Stable Diffusion models transform a noise distribution into the data distribution through a process of diffusion, gradually refining the generated image over time. This process allows for a high degree of control over the generation process, as the model can be stopped at any point to yield different levels of detail.

GANs, on the other hand, generate data in a single step, with the generator creating a data instance and the discriminator evaluating it. While this process can be faster, it can also lead to mode collapse, where the generator produces limited varieties of samples.
