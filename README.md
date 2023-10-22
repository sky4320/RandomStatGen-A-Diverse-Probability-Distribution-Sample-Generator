# RandomStatGen

RandomStatGen is a Python project that allows you to generate random samples from various probability distributions. It's a versatile tool that can help you simulate data for statistical and analytical purposes. This README provides instructions on how to use the project and examples of input formats for different distributions.

## Getting Started

Follow the steps below to execute the RandomStatGen project:

1. Clone the project repository or download the source code.

2. Open a terminal or command prompt.

3. Navigate to the directory where the project code is located.

4. Run the code with the following command, providing the type of distribution and required arguments for that distribution:

    ```bash
    python random_stat_gen.py [no_of_samples] [distribution] [distribution-specific-arguments]
    ```

## Input Format

Here's the breakdown of the input parameters:

- `[no_of_samples]`: The number of samples you want to generate from the specified probability distribution.

- `[distribution]`: The type of probability distribution you want to sample from. Choose from the supported distributions:

    - "bernoulli"
    - "binomial"
    - "geometric"
    - "neg-binomial"
    - "poisson"
    - "arb-discrete"
    - "uniform"
    - "exponential"
    - "gamma"
    - "normal"

- `[distribution-specific-arguments]`: These arguments depend on the selected distribution and should be provided accordingly.

## Examples

Here are a few examples of how to use RandomStatGen with different distributions:

1. To generate 100 samples from a Bernoulli distribution with a probability of success (p) of 0.3:

    ```bash
    python random_stat_gen.py 100 bernoulli 0.3
    ```

2. To generate 200 samples from a Poisson distribution with a lambda (λ) value of 2.5:

    ```bash
    python random_stat_gen.py 200 poisson 2.5
    ```

3. To generate 500 samples from a Uniform distribution in the range of 5 to 10:

    ```bash
    python random_stat_gen.py 500 uniform 5 10
    ```

4. To generate 150 samples from a Normal distribution with a mean (μ) of 5 and standard deviation (σ) of 1.5:

    ```bash
    python random_stat_gen.py 150 normal 5 1.5
    ```

## Supported Distributions

- **Bernoulli**
- **Binomial**
- **Geometric**
- **Negative Binomial**
- **Poisson**
- **Arbitrary Discrete**
- **Uniform**
- **Exponential**
- **Gamma**
- **Normal**

## Note

Make sure you have Python installed on your system and have the required dependencies, like `numpy`, if they are not included in the project.

## Author

Siva Keshav Yalamandala
  Email: sxy3510@mavs.uta.edu

## License

This project is open for collaboration and contributions. Feel free to use it, modify it, and contribute to its development. It is released under the [MIT License](LICENSE).

Happy sampling!
