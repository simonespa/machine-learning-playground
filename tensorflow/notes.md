# Notes

During training, weights are updated by using the partial derivative of the loss with respect to each individual weight.

GradientTape is a context manager which calculate these partial differentiation

## Inference

There are three forms of inference:

- deduction: from the universal to the particular
- induction: from the particular to the universal
- abduction: from an observation to the universal

Tutte e tre le inferenze possono accrescere la conoscenza. Induzione e abduzione necessitano però di una verifica empirica dato che non contengono al loro interno una verità logica. Ma è solo tramite l’abduzione che possiamo formulare idee nuove, ricordando che esiste un margine d’errore.

Abduction is forming a hypothesis, induction is like analyzing the data from testing a hypothesis, and deduction would be used in drawing certain logical conclusions from the data gathered.

### Deduction

Deductive reasoning deals with **certainty** and involves reasoning toward certain conclusions.

### Induction

Inductive reasoning deals with **probability** and involves reasoning toward likely conclusions (based on data).

Induction can be defined as inference of general rules that explain certain data.

### Abduction

Abductive reasoning deals with **possibility** and involves reasoning toward possible conclusions (based on guesswork).

It's the process of forming a hypothesis that explains given observed phenomena. Abduction is a generalization of induction.

It is a type of reasoning that is used in formulating a hypothesis for further testing.

## Example

```python
import logging
import google.cloud.logging as cloud_logging
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging_v2.handlers import setup_logging

cloud_logger = logging.getLogger('cloudLogger')
cloud_logger.setLevel(logging.INFO)
cloud_logger.addHandler(CloudLoggingHandler(cloud_logging.Client()))
cloud_logger.addHandler(logging.StreamHandler())

import tensorflow as tf
import numpy as np

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer=tf.keras.optimizers.SGD(), loss=tf.keras.losses.MeanSquaredError())
model.fit(xs, ys, epochs=50)

cloud_logger.info(str(model.predict([10.0])))

```

## How NN learns

During training, weights are updated by using the partial derivative of the loss function with respect to each individual weight.
During the forward pass, the opeerations are recorded, so that during the backward pass the list of operations is traversed in reverse order to compute those gradients.
