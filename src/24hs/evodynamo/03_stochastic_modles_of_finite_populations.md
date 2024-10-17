# Stochastic Models of Finite Populations

## Key Concepts

- **Gambler’s Ruin**:
  - A classical problem in probability theory where a random walk eventually results in one party (player or bank) losing all resources, illustrating the inevitability of random processes reaching absorbing states.

- **Markov Chains**:
  - **Definition**: A stochastic process where the next state depends only on the current state, not on the sequence of previous states. Described by a transition matrix.
  - **Ergodicity**: A Markov chain is ergodic if it is aperiodic and irreducible, meaning every state can be reached from any other, and a unique stationary distribution exists.

- **The Moran Process**:
  - A **birth-death process** where each step involves selecting one individual to reproduce and one to die in a population of constant size \\(N\\).
  - **State space**: The number of individuals of type \\(A\\) in the population, ranging from 0 to \\(N\\).
  - The process is a Markov chain with **two absorbing states**: either all individuals are of type \\(A\\) (fixation) or all are of type \\(B\\) (extinction).
  - **Neutral Drift**: In the absence of selection, the allele frequencies change randomly due to drift.

- **Fixation Probability**:
  - The probability that a mutant allele reaches fixation (becomes the only allele in the population) starting from a certain frequency.
  - In the Moran process, the fixation probability of a neutral allele is \\(x_i = i / N\\) where \\(i\\) is the initial number of individuals with the mutant allele.

- **Birth-Death Process**:
  - A process where population changes occur incrementally (by one individual at each step), often modeled using transition probabilities.
  - Transition probabilities in the Moran process are:
    \\[
    P_{i, i+1} = p(1 - p), \quad P_{i, i-1} = (1 - p)p, \quad P_{i, i} = p^2 + (1 - p)^2
    \\]
  - This tri-diagonal matrix structure means the population size can change by at most one individual per step.

- **Absorption Probabilities**:
  - The probability of ending in state \\(N\\) (all type A) when starting from state \\(i\\) is given by:
    \\[
    x_i = \frac{1 + \sum_{j=1}^{i-1} \prod_{k=1}^{j} \gamma_k}{1 + \sum_{j=1}^{N-1} \prod_{k=1}^{j} \gamma_k}
    \\]
    where \\(\gamma_i = \frac{\beta_i}{\alpha_i}\\) represents the ratio of death to birth rates for different states.

- **Mean Fixation Time**:
  - For large population sizes, the expected time to fixation for a neutral allele is approximately \\(N^2[(1 - p) \log(1 - p) + p \log p]\\) generations.
  - The diversity (heterozygosity) decays exponentially at a rate proportional to \\(2 / N^2\\), quantifying the effect of genetic drift.

- **Moran Process with Selection**:
  - **Selection** introduces differential reproduction rates. Let \\(r_A = r\\) be the reproduction rate of type \\(A\\), and \\(r_B = 1\\) for type \\(B\\). The probabilities of reproducing type \\(A\\) or type \\(B\\) are modeled as competing exponentials.
  - Transition probabilities for the Moran process with selection are:
    \\[
    P(T_A < T_B) = \frac{r^i}{r^i + (N - i)}
    \\]

- **Poisson Process**:
  - A counting process where events (e.g., mutations) occur randomly over time, with the number of events in any interval following a Poisson distribution.
  - **Inter-arrival times** between events follow an exponential distribution with parameter \\(\lambda\\), where \\(\lambda t\\) is the expected number of events in time \\(t\\).

- **Rate of Evolution**:
  - The rate at which a beneficial mutation takes over the population is proportional to the mutation rate \\(u\\) and the fixation probability \\(\rho\\). If the mutant is neutral, the rate of evolution is simply the mutation rate \\(R = u\\).

- **Molecular Clock of Neutral Evolution**:
  - Neutral mutations accumulate at a constant rate, independent of population size, leading to the idea of a molecular clock used to estimate evolutionary timescales.

---

## Key Equations and Models

- **Conditional Probability**:
  \\[
  P(X | Y) = \frac{P(X, Y)}{P(Y)}
  \\]
  - Bayes' theorem and the law of total probability allow the calculation of posterior probabilities in stochastic models.

- **Exponential Distribution**:
  - Probability density function:
    \\[
    f(x) = \lambda e^{-\lambda x}
    \\]
  - **Memoryless property**: \\(P(X > s + t | X > t) = P(X > s)\\), meaning the probability of an event occurring in the future does not depend on how long it has already been.

- **Moran Process Transition Probabilities**:
  \\[
  P_{i, i+1} = p(1 - p), \quad P_{i, i-1} = (1 - p)p, \quad P_{i, i} = p^2 + (1 - p)^2
  \\]
  - Describes the random drift of allele frequencies in a finite population.

- **Fixation Probability in the Moran Process**:
  \\[
  x_i = \frac{i}{N}
  \\]
  - For neutral mutations, the probability of fixation is simply the initial frequency of the allele.

- **Absorption Probability in Birth-Death Process**:
  \\[
  x_i = \frac{1 + \sum_{j=1}^{i-1} \prod_{k=1}^{j} \gamma_k}{1 + \sum_{j=1}^{N-1} \prod_{k=1}^{j} \gamma_k}
  \\]
  - Represents the probability of ending up in a certain absorbing state (all type \\(A\\)).

- **Rate of Evolution**:
  \\[
  R = N u \rho
  \\]
  - Describes how fast a population evolves from one state to another under mutation and selection.

---

## Summary Points

- The **Moran process** is a fundamental birth-death process in population genetics, capturing the dynamics of allele frequencies in finite populations.
- **Markov chains** and stochastic processes underpin the mathematical framework, where each state represents a different composition of the population.
- **Fixation probabilities** and **mean fixation time** can be analytically derived for both neutral and selectively advantageous alleles.
- **Poisson processes** model random mutation events, and the molecular clock of neutral evolution assumes that mutations accumulate at a constant rate over time.
- The **Moran process with selection** introduces competing reproduction rates, influencing the rate at which beneficial alleles spread in the population.
