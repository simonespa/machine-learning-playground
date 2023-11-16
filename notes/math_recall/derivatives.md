# Derivatives

The derivative of a function $f$ is the rate at which the function value is changing with respect to $x$, given $f(x)$ and a given value of $x$.

Weights are updated by using the partial derivative of the loss with respect to each individual weight.

By first principle, the derivative of a function $f(x)$ is

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

where we apply the limit for h tending to zero of the **difference quotient**. The application of this mechanism on different type of functions can be summarised with the following rules:

- Constant: $(c)' = 0$
- Power rule: $(x^n)' = nx^{n-1}$
- Exponential: $(e^x)' = e^x$
- Sine: $(sin)' = cos$
- Cosine: $(cos)' = -sin$
- Tangent: $(tan)' = sec^2$
- Secant: $(sec)' = sec tan$
- Arcsine: $ (arcsin)' = (sin^{-1})' = \frac{1}{\sqrt{1 - x^2}}$
- Arc cosine: (arccos)' = $(cos^{-1})' = - \frac{1}{\sqrt{1 - x^2}}$
- Arctangent: $(arctan)' = (tan^{-1})' = \frac{1}{x^2 + 1}$
- Arcsecant: $(arcsec)' = (sec^{-1})' = \frac{1}{x \sqrt{x^2 - 1}}$
- Sum: $(f + g)' = f' + g'$
- Difference: $(f - g)' = f' - g'$
- Product: $(fg)' = f'g + fg'$
- Quotient: $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$
- Reciprocal: $(\frac{1}{f})' = \frac{-f'}{f^2}$
- Chain rule: $(f(g))' = f'(g) g'$

## Calculator

Derivative calculator: https://calculator-derivative.com/partial-derivative-calculator

## Reference

Table of derivatives: https://math.stackexchange.com/questions/4181083/derivative-with-chain-rule-of-sum-of-squares-error-function-when-fitting-the-dat
