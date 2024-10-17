# Clustering

## **What is Clustering?**

- **Definition**: Clustering is the task of grouping a set of objects such that objects in the same group (cluster) are more similar to each other than to those in other groups. It is an example of **unsupervised learning** since no predefined labels (training data) are used.
- **Applications**:
  - Grouping images to discover categories.
  - Clustering patient data to uncover disease subtypes.
  - Detecting communities in social networks.

---

## **k-means Clustering**

- **Objective**: Partition data into \\( k \\) clusters by minimizing the variance within each cluster:
  \\\[
  V(D) = \sum_{i=1}^{k} \sum_{x_j \in S_i} (x_j - \mu_i)^2
  \\]
  - \\( S_i \\): the \\(i\\)-th cluster
  - \\( \mu_i \\): the mean of the cluster
  - \\( D \\): dataset

- **Algorithm (Lloyd's Algorithm)**:
  1. Partition data into \\( k \\) initial clusters.
  2. Compute the mean for each cluster.
  3. Reassign each point to the closest cluster mean.
  4. Repeat until no point changes its cluster.

- **Challenges**:
  - Sensitive to the choice of \\( k \\) (number of clusters).
  - Initialization affects the final result, and the algorithm might converge to a **local optimum**.
  - **Order-dependent**: the final clusters depend on the initial configuration.

- **Silhouette Coefficient**: A metric to evaluate the quality of clustering:
  \\\[
  s(x) = \frac{d(x, \mu_{C'}) - d(x, \mu_C)}{\max(d(x, \mu_C), d(x, \mu_{C'})}
  \\]
  - \\( s(x) \approx 1 \\): Well clustered.
  - \\( s(x) \approx 0 \\): Between clusters.
  - \\( s(x) < 0 \\): Incorrectly clustered.

---

## **k-medoids Clustering**

- **Similar to k-means**, but instead of the mean, it uses the **medoid** (the most centrally located point in a cluster).
  - Formula for the medoid:
    \\\[
    m_i = \arg \min_{x_j \in S_i} ||x_j - \mu_i||^2
    \\]
  - This method is more **robust** to outliers since it restricts cluster centers to actual data points.

---

## **Kernel k-means**

- **Idea**: Apply k-means clustering in a high-dimensional feature space using **kernels** to handle complex, non-linear boundaries.
  - Key step: Instead of directly computing distances, use kernel functions:
    \\\[
    d(x_1, x_2) = \| \phi(x_1) - \phi(x_2) \|^2 = k(x_1, x_1) - 2k(x_1, x_2) + k(x_2, x_2)
    \\]
  - Kernel k-means is especially useful for clustering **graphs** or **strings**.

---

## **Graph-Based Clustering**

- **Graph Representation**: A dataset is represented as a graph \\( G = (V, E) \\), where nodes \\( V \\) are objects and edges \\( E \\) are weighted by the similarity between objects.
- **Steps**:
  1. Define a threshold \\( \theta \\).
  2. Remove all edges with weight \\( w_{ij} > \theta \\).
  3. Each **connected component** in the graph forms a cluster.

- **DBScan (Density-Based Spatial Clustering of Applications with Noise)**:
  - **Core Idea**: Group points that are closely packed together and mark outliers as noise.
  - **Core Object**: A point is considered a core object if there are at least **MinPoints** neighbors within a distance \\( \epsilon \\). Clusters are built by iteratively expanding core objects.

---

## **Spectral Clustering**

- **Concept**: Uses the **graph Laplacian** to connect graph-based clustering with k-means.
  - The **Laplacian matrix** \\( L = D - W \\), where \\( D \\) is the degree matrix and \\( W \\) is the adjacency matrix, helps find clusters by minimizing a **cut** in the graph:
    \\\[
    \min \frac{1}{2} \sum_{a=1}^{k} \sum_{b=1}^{k} \kappa(C_a, C_b)
    \\]
    where \\( \kappa \\) measures the weight of edges between clusters.

- **Procedure**:
  1. Compute the **eigenvectors** of the Laplacian matrix.
  2. Use the **k smallest eigenvectors** to form a new representation of the data.
  3. Apply k-means to this new representation.

---

## **EM Clustering (Expectation-Maximization)**

- **Soft k-means**: Instead of hard assignments, points are assigned probabilistically to clusters.
  - **E-step**: Compute the probability that each point belongs to each cluster.
  - **M-step**: Update the cluster parameters (means and covariances) based on these probabilities.

- **Gaussian Mixture Models (GMMs)**: EM is often used to estimate the parameters for mixtures of Gaussian distributions.

---

## **Hierarchical Clustering**

- **Concept**: Instead of flat clusters, it builds a **hierarchy** of clusters where clusters can contain subclusters.
- **Methods**:
  - **Single Link**: Minimum distance between points in two clusters.
  - **Complete Link**: Maximum distance between points in two clusters.
  - **Average Link**: Average distance between all pairs of points in two clusters.

- **Dendrogram**: A tree-like structure used to represent the hierarchy.

---

## **Comparison of Clustering Algorithms**

- **k-means**:
  - Fast and simple.
  - Sensitive to initialization.
  - Good for large datasets with clear cluster boundaries.

- **k-medoids**: More robust to outliers but slower than k-means.

- **Graph-based Clustering (DBScan)**:
  - Handles noise well.
  - No need to specify the number of clusters.
  - Struggles with varying density clusters.

- **Spectral Clustering**: Good for complex data but computationally expensive.

- **EM Clustering**: Handles soft assignments and works well with **Gaussian mixtures**, but prone to convergence to local optima.

- **Hierarchical Clustering**: Captures the nested structure but can be computationally expensive for large datasets.
