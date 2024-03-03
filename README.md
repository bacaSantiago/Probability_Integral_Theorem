# Random Number Generation with Probability Integral Theorem

## Overview

This Python program demonstrates the use of the Probability Integral Theorem to generate arbitrary random numbers. The theorem states that if you can generate numbers with a continuous uniform distribution in the interval x ∈ [0,1], you can generate any distribution using the corresponding inverse cumulative distribution function.

## Dependencies

Make sure you have the following libraries installed:

- NumPy (version 1.19.5 or later)
- Matplotlib (version 3.4.3 or later)

You can install these libraries using the following command:

```bash
pip install numpy matplotlib
```

## Exercise 1: Histogram of Uniform Random Numbers in [0, 1]

This exercise aims to generate a large sample of uniform random numbers in the interval [0, 1]. The sample is created using the `np.random.uniform` function from the NumPy library, and a histogram is plotted to visualize the distribution. The red line in the histogram represents the theoretical value expected for a uniform distribution.

## Exercise 2: Histogram of Transformed Sample with Exponential Distribution

In this exercise, the uniform random sample generated in Exercise 1 is transformed into a new sample with an exponential distribution. The transformation is achieved by using the inverse of the cumulative distribution function (CDF) for the exponential distribution. The resulting sample is then plotted along with the theoretical probability density function (PDF) for comparison.

## Exercise 3: Histogram of Transformed Sample with Rayleigh Distribution

The third exercise follows a similar procedure as Exercise 2, but this time the transformation is applied to a Rayleigh distribution. The Rayleigh distribution has a different PDF and CDF, and the resulting transformed sample is visualized through a histogram. Theoretical values based on the Rayleigh PDF are overlaid for comparison.

## Note

Ensure you have the necessary permissions to execute the script, and consider adjusting the parameters (e.g., sample size, distribution parameters) based on your specific requirements. Understanding these exercises can provide insights into generating random numbers following specific probability distributions using the Probability Integral Theorem.