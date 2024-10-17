# Classification Algorithms

Here is a detailed summary of the **Classification Algorithms** in the uploaded document organized into bullet points and course notes. I have included key equations, concepts, and figures where possible.

---

## **Classification Overview**

- **Problem**: Given an object \\(x\\), predict its class label \\(y\\). Examples include identifying objects in computer vision, detecting fraudulent credit card transactions, and gene classification in personalized medicine.
- **Types**:
  - **Binary classification**: \\(y \in \{0, 1\}\\)
  - **Multiclass classification**: \\(y \in \{1, \dots, n\}\\)
  - **Regression**: \\(y \in \mathbb{R}\\)

---

## **Evaluating Classifiers**

- **Contingency Table**: For binary classification, results are represented as:

    |       | \\(y = 1\\) |\\( y = -1 \\)|
    |-------|-------|--------|
    | \\( f(x) = 1 \\) | TP    | FP     |
    |\\( f(x) = -1 \\)| FN    | TN     |

  TP: True Positive, FP: False Positive, FN: False Negative, TN: True Negative.

- **Accuracy**:
  \\[
  \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
  \\]
  Accuracy is not ideal for imbalanced classes, which leads to focusing on **precision** and **recall**:

- **Precision**: \\( \frac{TP}{TP + FP} \\)

- **Recall**: \\( \frac{TP}{TP + FN} \\)

- **ROC Curve**: Plots **true positive rate** (sensitivity) vs. **false positive rate**. A perfect classifier's curve passes through the point (0,1). The **Area Under the Curve (AUC)** is a metric summarizing the performance of the classifier:
  \\[
  AUC = P\left(\text{positive point gets higher score than negative}\right)
  \\]

---

## **Cross-Validation and Bootstrapping**

- **Cross-Validation**: Split data into \\(k\\) subsets, train on \\(k-1\\), and test on the remaining subset. This is repeated \\(k\\) times.
- **Bootstrapping**: Random sampling with replacement to create multiple training/test splits, averaging results over multiple iterations.
- **Parameter Tuning**: Use internal cross-validation on training data to optimize model parameters without overfitting.

---

## **Nearest Neighbors (k-NN)**

- **k-NN**: Classifies a point based on the majority label of its \\(k\\) nearest neighbors.
  - **Distance Metric**: The Euclidean distance is often used:
    \\[
    d(x, x') = \sqrt{\sum_{i=1}^d (x_i - x'_i)^2}
    \\]
  - **Challenges**: Selecting \\(k\\), runtime optimization, and handling high-dimensional data.

- **Mahalanobis Distance**:
 \\[
  d_M(x, x') = \sqrt{(x - x')^\top \Sigma^{-1} (x - x')}
 \\]
  where \\(\Sigma\\) is the covariance matrix of the dataset.

---

## **Naive Bayes Classifier**

- **Bayes' Rule**:
 \\[
  P(Y = y | X = x) = \frac{P(X = x | Y = y) P(Y = y)}{P(X = x)}
 \\]
  - The classifier assumes **conditional independence** of features:
   \\[
    P(X | Y = y) = \prod_{j=1}^d P(X_j | Y = y)
   \\]

- **Prediction**:
 \\[
  \hat{y} = \arg\max_{y} P(Y = y) \prod_{j=1}^d P(X_j | Y = y)
 \\]
  - Naive Bayes works well in practice despite the strong independence assumption.

---

## **Linear Discriminant Analysis (LDA)**

- **Assumptions**:
  - Data from each class is normally distributed with the same covariance matrix but different means \\(\mu_0\\) and \\(\mu_1\\).

- **Log-Likelihood Ratio**:
 \\[
  f(x) = \log\left( \frac{P(Y=1|X=x)}{P(Y=0|X=x)} \right)
 \\]
  - Linear discriminant: \\( f(x) = w^\top x + b \\), where \\(w = (\mu_1 - \mu_0)^\top \Sigma^{-1}\\).

---

## **Logistic Regression**

- **Logistic Function**:
 \\[
  f(z) = \frac{1}{1 + e^{-z}}
 \\]
  where \\(z = w^\top x + b\\).

- **Training**: Minimizing the logistic loss:
 \\[
  \mathcal{L}(w) = \frac{1}{n} \sum_{i=1}^n \log(1 + e^{-y_i (w^\top x_i)})
 \\]
  - The weights \\(w\\) are learned by gradient descent or other optimization techniques.

---

## **Decision Trees**

- **Concept**: Split the data recursively based on feature values to maximize information gain, using criteria like **entropy** and the **Gini index**:
  - **Entropy**:
   \\[
    H(D) = -\sum_{i=1}^m p_i \log_2(p_i)
   \\]
  - **Gini Index**:
   \\[
    Gini(D) = 1 - \sum_{i=1}^m p_i^2
   \\]
- **Random Forests**: Ensemble of decision trees, each built on random subsets of data and features.

---

## **Support Vector Machines (SVM)**

- **Hard-Margin SVM**: Finds the hyperplane that maximizes the margin between classes:
 \\[
  \min_w \frac{1}{2} \|w\|^2 \quad \text{s.t.} \, y_i (w^\top x_i + b) \geq 1
 \\]
- **Soft-Margin SVM**: Allows some misclassification using slack variables \\(\xi\\):
 \\[
  \min_w \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \xi_i \quad \text{s.t.} \, y_i (w^\top x_i + b) \geq 1 - \xi_i
 \\]
  where \\(C\\) controls the trade-off between margin size and misclassification.

---

## **Kernel Methods**

- **Kernel Trick**: Maps data into a higher-dimensional space to make it linearly separable. Common kernels include:
  - **Linear Kernel**: \\( k(x, x') = x^\top x' \\)
  - **Polynomial Kernel**: \\( k(x, x') = (x^\top x' + c)^d \\)
  - **Gaussian (RBF) Kernel**:
   \\[
    k(x, x') = \exp\left(- \frac{\|x - x'\|^2}{2\sigma^2}\right)
   \\]

---

## **Figures/Diagrams**

1. **ROC Curves**: Visualization of model performance with true positive vs. false positive rates.
2. **Logistic Function**: S-shaped curve representing the probability output from logistic regression.
3. **Decision Trees**: Flowchart-like structures splitting data based on feature values.
