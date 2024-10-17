# What is Evolution?

## Key Concepts

- **Evolution**:
  - Refers to changes in the frequency of different types within a population over generations.
  - In biological terms, it specifically describes changes in allele frequencies in a gene pool.

- **Reproduction**:
  - Evolution requires a population of reproducing individuals for allele frequencies to evolve.

- **Exponential Growth ("Malthusian law")**:
  - **Discrete Model**: Population doubles with each generation. The growth equation is \\( x_{t+1} = 2x_t \\), leading to \\( x_t = x_0 \cdot 2^t \\).
  - **Continuous Model**: For continuous time, the growth rate is described by \\( x'(t) = r \cdot x(t) \\) with solution \\( x(t) = x_0 e^{rt} \\).

- **Cell Death**:
  - Mortality is included in the population model with the equation \\( x'(t) = (r - d) \cdot x(t) \\), where \\(d\\) is the death rate.
  - The **basic reproductive ratio** \\( R_0 = \frac{r}{d} \\) defines population growth dynamics:
    - \\( R_0 > 1 \\): Population grows.
    - \\( R_0 < 1 \\): Population shrinks to extinction.
    - \\( R_0 = 1 \\): Population size remains constant but is unstable.

- **Logistic Growth**:
  - When a population approaches its carrying capacity \\(K\\), the growth rate slows according to the logistic equation:
    \\[
    x'(t) = r x(t) \left( 1 - \frac{x(t)}{K} \right)
    \\]
  - The population reaches equilibrium at the carrying capacity \\(K\\).

- **Logistic Difference Equation**:
  - In discrete time, the logistic map is described by \\( x_{t+1} = a x_t (1 - x_t) \\), where \\(a\\) is the growth rate.
  - This simple equation can exhibit chaotic behavior for certain values of \\(a\\).

- **Selection**:
  - **Independent Types**: For two types \\(A\\) and \\(B\\) with exponential growth rates \\(a\\) and \\(b\\), their relative proportions evolve according to:
    \\[
    \frac{x(t)}{y(t)} = \frac{x_0}{y_0} e^{(a - b)t}
    \\]
    - If \\(a > b\\), type \\(A\\) outcompetes type \\(B\\), and vice versa.

- **Two Competing Types**:
  - When the total population is constrained, the selection dynamics for two competing types \\(A\\) and \\(B\\) follow:
    \\[
    x'(t) = x(t)(1 - x(t))(a - b)
    \\]
  - The system describes the competition between two types based on their fitness.

- **Probability Simplex**:
  - The state of a population with multiple types is represented on a **probability simplex**, where each point corresponds to the relative frequencies of types in a population.

- **Subexponential vs. Superexponential Growth**:
  - **Subexponential Growth** (\\(c < 1\\)): Stable coexistence of multiple types, even if one has a fitness advantage.
  - **Superexponential Growth** (\\(c > 1\\)): One type dominates and drives the other to extinction, leading to an unstable mixed equilibrium.

- **Mutation**:
  - Mutation introduces genetic diversity, even in the absence of selection.
  - For two types with mutation rates \\(u_1\\) and \\(u_2\\), the equilibrium frequencies depend on the mutation rates:
    \\[
    x^* = \frac{u_2}{u_1 + u_2}
    \\]
    - Mutation allows coexistence of types, even with no fitness differences.

- **Hardy-Weinberg Principle**:
  - Describes how allele frequencies in a large, randomly mating population reach equilibrium after one round of random mating.
  - Genotype frequencies follow:
    \\[
    x = p^2, \quad y = 2pq, \quad z = q^2
    \\]
  - These frequencies remain constant over generations unless external factors such as mutation or selection are introduced.

---

## Key Equations and Models

- **Exponential Growth**:
  \\[
  x'(t) = r \cdot x(t) \quad \Rightarrow \quad x(t) = x_0 e^{rt}
  \\]
  - Describes exponential population growth in continuous time.

- **Logistic Growth**:
  \\[
  x'(t) = r \cdot x(t) \left( 1 - \frac{x(t)}{K} \right)
  \quad \Rightarrow \quad x(t) = \frac{Kx_0 e^{rt}}{K + x_0 (e^{rt} - 1)}
  \\]
  - Describes population growth with carrying capacity \\(K\\).

- **Selection Dynamics**:
  \\[
  x'(t) = x(t)(1 - x(t))(a - b)
  \\]
  - Models competition between two types based on relative fitness.

- **Mutation Dynamics**:
  \\[
  x'(t) = u_2 - x(u_1 + u_2) \quad \Rightarrow \quad x^* = \frac{u_2}{u_1 + u_2}
  \\]
  - Describes coexistence due to mutation, even when both types have equal fitness.

- **Hardy-Weinberg Equilibrium**:
  \\[
  p = x + \frac{y}{2}, \quad q = z + \frac{y}{2}
  \\]
  - Allele frequencies remain constant under random mating.

---

## Summary Points

- Evolution is driven by the reproduction of individuals and changes in allele frequencies over generations.
- Population growth can be modeled using exponential and logistic equations, which describe different growth dynamics, including constraints like death and carrying capacity.
- Selection dynamics favor individuals with higher relative fitness, leading to the survival of the fittest.
- Subexponential growth allows for coexistence, while superexponential growth leads to the dominance of one type.
- Mutation introduces genetic variation and can drive coexistence even in the absence of fitness differences.
- The Hardy-Weinberg principle explains how allele and genotype frequencies stabilize in a large, randomly mating population.
