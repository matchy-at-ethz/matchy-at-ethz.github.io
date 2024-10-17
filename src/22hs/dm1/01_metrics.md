# Metrics

## **Introduction to Data Mining (DM)**

- **Definition**: Data mining is the search for patterns and statistical dependencies in large datasets. It is often associated with machine learning or knowledge discovery.
- **Application**: DM is applied in biology, medicine, and various industries for personalized recommendations, personalized medicine, etc.
- **Key Topics**: Distance functions, classification, clustering, feature selection.

---

## **Personalized Medicine through Data Mining**

- **Vision**: Tailor treatments to patients’ genetic/molecular properties to increase efficacy. Drugs often work for only a fraction of patients due to genetic variability.
- **Technological Advances**: Genome sequencing has become rapid and scalable, identifying variations among millions of genetic bases.
- **Goals**: Detect correlations between diseases, drug responses, and genetic variations.

---

## **Distance Functions**

- **Key Concept**: Similarity or distance between objects is at the core of data mining.
- **Metric Definition**: A metric on vectors \\(x_1, x_2, x_3 \in \mathbb{R}^d\\) is a function \\(d\\) if:
  1. \\( d(x_1, x_2) \geq 0 \\)
  2. \\( d(x_1, x_2) = 0 \text{ if and only if } x_1 = x_2 \\)
  3. \\( d(x_1, x_2) = d(x_2, x_1) \\)
  4. \\( d(x_1, x_3) \leq d(x_1, x_2) + d(x_2, x_3) \\)

---

## **Common Distance Functions**

- **Manhattan Distance**: \\\( d(x, x') = \sum_{i=1}^d |x_i - x'_i| \\\)
- **Euclidean Distance**: \\( d(x, x') = \sqrt{\sum_{i=1}^d (x_i - x'_i)^2} \\)
- **Chebyshev Distance**: \\( d(x, x') = \max_i (|x_i - x'_i|) \\)
- **Minkowski Distance**: \\( d(x, x') = \left(\sum_{i=1}^d |x_i - x'_i|^p \right)^{1/p} \\)
  - \\( p = 1 \\) recovers the Manhattan distance, \\( p = 2 \\) recovers the Euclidean distance, and for \\( p \rightarrow \infty \\), it converges to the Chebyshev distance.

---

## **Distance on Sets and Strings**

- **Jaccard Distance**: Measures dissimilarity between sets \\( A \\) and \\( B \\).
  - Formula: \\( d(A, B) = \frac{|A \cup B| - |A \cap B|}{|A \cup B|} \\)
- **String Similarity (k-mer)**: Quantifies similarity by representing strings as histograms of k-mer frequencies. Example: the strings "downtown" and "known" can be compared based on their 3-mer substrings.

---

## **Distance on Time Series**

- **Dynamic Time Warping (DTW)**: Measures similarity between time series of different lengths or varying time intervals.
  - Recursive formula:
    \[
    DTW(i, j) = d(x_i, x'_j) + \min\left\{ DTW(i, j-1), DTW(i-1, j), DTW(i-1, j-1) \right\}
    \]
  - Used when direct time-to-time comparisons are not feasible.

---

## **Distance on Graphs**

- **Graph Comparison Problems**: Key problems include determining if two graphs are identical (graph isomorphism) or finding if one graph is contained within another (subgraph isomorphism).
- **Weisfeiler-Lehman Kernel**: Efficient method for graph comparison by iterating over node neighborhoods, compressing them, and relabeling based on sorted labels.
  - This method is highly scalable and is commonly used in chemoinformatics and bioinformatics.

---

## **Applications in Biology & Medicine**

- **Data Mining in Genetics**: Searches for disease-associated loci in genomes. Challenges include:
  - **Missing Heritability**: Many diseases show weak correlations with genetic loci due to small sample sizes, environmental factors, and oversimplified models.
  - **Interaction Search**: Efficient algorithms are needed for exploring interactions between millions of genetic loci without exhaustive enumeration.

---

## **Key Concepts in DM**

- **Knowledge Discovery Process**: Stages include data cleaning, integration, selection, transformation, mining, pattern evaluation, and presentation.
- **Outlier Detection**: Finding patients with unusual disease progression or drug response is a key challenge in personalized medicine.

---

## **Algorithms and Future of Data Mining**

- **Graph Kernels**: Algorithms for comparing large graphs (like biological networks) are critical in drug discovery and gene interaction studies.
- **Future Trends**: Increasing use of wearable devices, electronic health records, and indirect monitoring through social media is expected to fuel personalized medicine.

---

## Figures and Diagrams (Explanation)

- **Dynamic Time Warping (DTW)**: A matrix-based visual method for aligning two time series optimally by minimizing alignment costs.
- **Weisfeiler-Lehman (WL) Kernel**: Shows the iterative process of graph comparison by relabeling nodes based on their neighbor labels.
