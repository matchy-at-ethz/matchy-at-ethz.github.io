# Feature Selection

Here is a detailed summary and course notes for the uploaded document on **Feature Selection** from **Data Mining**:

---

## **What is Feature Selection?**

- **Definition**: Feature selection involves identifying a relevant subset of features \\( X \\) that are most predictive of the output variable \\( Y \\) in supervised learning tasks.
- **Distinction**:
  - **Feature Ranking**: Orders features by relevance.
  - **Feature Transformation**: Transforms original features into a new representation.

---

## **Why Feature Selection?**

- **Goals**:
  - Detect causal relationships.
  - Remove noisy or irrelevant features.
  - Reduce computational cost and improve interpretability.
  - Speed up learning and improve accuracy.
- **Two Modes**:
  - **Filter Approach**: Select features a priori based on a quality metric (e.g., information criterion).
  - **Wrapper Approach**: Select features specific to a learning algorithm.

---

## **Feature Selection as an Optimization Problem**

- **Objective**: Given a feature set \\( D \\) and a quality function \\( q \\), select the subset \\( S \\) of size \\( n' \\) that maximizes \\( q \\):
  \\[
  \arg \max_{S \subset D \land |S|=n'} q(S)
  \\]
- **Challenges**: The problem is combinatorial and computationally intractable (exponential in \\( n' \\)).

---

## **Greedy Feature Selection**

- **Forward Feature Selection**:
  - Start with an empty set.
  - Iteratively add the feature that maximizes the quality function until the desired number of features is selected.
  \\[
  S^{\ast} \leftarrow S^{\ast} \cup \arg \max_j q(S^{\ast} \cup j)
  \\]

- **Backward Elimination**:
  - Start with all features.
  - Iteratively remove the least informative feature.
  \\[
  S^{\ast} \leftarrow S^{\ast} \setminus \arg \max_j q(S^{\ast} \setminus j)
  \\]

- **Optimality**: Greedy approaches are optimal if the quality function \\( q \\) is **additive** or **submodular** (exhibits diminishing returns).

---

## **Key Metrics for Feature Selection**

1. **Correlation Coefficient** \\( \rho_{X, Y} \\):
   \\[
   \rho_{X, Y} = \frac{\text{cov}(X, Y)}{\sigma_X \sigma_Y}
   \\]
   Measures linear dependence between features \\( X \\) and \\( Y \\).

2. **Mutual Information** \\( I(X, Y) \\):
   \\[
   I(X, Y) = \sum_{x \in X, y \in Y} p(X = x, Y = y) \log \left( \frac{p(X = x, Y = y)}{p(X = x) p(Y = y)} \right)
   \\]
   Measures how much knowing \\( X \\) reduces uncertainty about \\( Y \\).

3. **Hilbert-Schmidt Independence Criterion (HSIC)**:
   \\[
   \text{HSIC}(X, Y) \propto \text{trace}(KHLH)
   \\]
   - \\( K \\): kernel matrix on \\( X \\).
   - \\( L \\): kernel matrix on \\( Y \\).
   - \\( H \\): centering matrix.
   - HSIC measures dependence between two variables in a kernel space.

---

## **Submodular Functions**

- A set function \\( q \\) is **submodular** if it satisfies diminishing returns:
  \\[
  q(S \cup X) - q(S) \geq q(T \cup X) - q(T), \quad \text{for } S \subseteq T
  \\]
- **Greedy Near-Optimality**: If \\( q \\) is submodular and non-decreasing, greedy selection guarantees at least 63% of the optimal solution:
  \\[
  q(S) \geq (1 - \frac{1}{e}) \max_{|T| = |S|} q(T)
  \\]

---

## **Wrapper Methods**

- **Not Embedded**: Use a learning algorithm as a quality measure for feature sets.
  - **Simple Wrapper**: Apply a classifier to each feature and evaluate its quality.
  - Extend to groups of features with **heuristic search** (greedy, Monte Carlo, etc.).

- **Embedded Methods**: Feature selection is integrated into the learning algorithm.
  - Example: **\\( \ell_0 \\)-norm SVM** iterates between feature re-scaling and SVM training.

---

## **Probe Method** for Determining the Number of Features

- **Problem**: Random features may show significant correlations, leading to false positives.
- **Solution**: Insert fake (random) features and stop when the first fake feature is selected.

---

## **Unsupervised Feature Selection**

- **No Target Variable**: Select features that are informative based on specific criteria such as:
  - **Saliency**: Features with high variance.
  - **Entropy**: Features with a uniform distribution of values.
  - **Smoothness**: Features with moderate curvature in time series data.
  - **Density**: Features connected to many other variables.

---

## **Feature Selection in Practice**

- **10 Questions from Guyon and Elisseeff**:
  1. Do you have domain knowledge?
  2. Are the features commensurate (measurable on the same scale)?
  3. Do you suspect feature interdependence?
  4. Do you need to prune the feature set?
  5. Should features be ranked individually?
  6. Do you need a predictor?
  7. Is your data “dirty”?
  8. What should you try first (linear predictors, forward selection, etc.)?
  9. Do you have the resources to test multiple methods?
  10. Do you want a stable solution (e.g., via bootstrapping)?

---

## **Revealing Examples**

- **Redundancy**: Highly correlated features are redundant, but they can still provide complementary information.
- **Collaborative Variables**: Two variables that are individually irrelevant can become important when considered together.
