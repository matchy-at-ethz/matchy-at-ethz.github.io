# Applications in Computational Biology

Here is a detailed summary and course notes for the uploaded document on **Applications in Computational Biology** from **Data Mining**:

---

## **Deleteriousness Prediction**

- **Objective**: Assess whether a genetic variant, specifically a missense variant (which causes amino acid changes), is deleterious (harmful).
- **Challenges**: Tens of thousands of variants may exist in a patient’s genome, necessitating computational tools for prediction.
- **Popular Tools**:
  - **SIFT**, **PolyPhen**, **MutationTaster**, **GERP**, **FatHMM**, among others, are widely used to predict deleteriousness.

- **Issues with Current Methods**:
  - **Type 1 Circularity**: Benchmark datasets used for both training and testing tools overlap significantly.
  - **Type 2 Circularity**: Proteins often contain only deleterious or neutral variants, leading to artificially high accuracy via majority vote.

- **Solutions**:
  - Cleanly separate training and test datasets to avoid circularity.
  - Stratify datasets by protein membership.

---

## **Phenotype Prediction and Epistasis**

- **Goal**: Predict phenotypic traits (observable characteristics) from an individual's genotype (genetic makeup).
- **Genome-Wide Association Studies (GWAS)**: Analyze genome-wide genetic variations to find associations with phenotypes.

- **Recent Work**:
  - Example from **Vilain Lab** (UCLA): Claimed that specific methylation patterns in twins could predict sexual orientation with 70% accuracy, but criticisms included small sample size and overfitting.

- **Lessons**:
  1. **Low sample sizes** still hinder predictions of complex traits.
  2. **Overfitting** must be avoided by building models that generalize well to unseen data.
  3. Correcting for **multiple testing** is crucial in high-dimensional spaces to avoid false positives.

---

## **Epistasis (Gene-Gene Interactions)**

- **Definition**: Epistasis refers to the interaction between genes where the effect of one gene is modified by one or more other genes.
- **Types**:
  - **Bateson's Masking Model**: One gene masks the effect of another gene.
  - **General Epistasis**: More complex interactions between two loci.

- **Models for Epistasis**:
  1. **Multiplicative Interaction**: Odds increase multiplicatively with certain genotypes.
  2. **Threshold Model**: Interaction only manifests when both loci contain disease-associated alleles.

- **Applications**: Epistasis is often cited as one explanation for the missing heritability of complex traits, such as breast cancer, where gene interactions affect disease risk.

---

## **Bottlenecks in Two-Locus Mapping**

- **Scale**: The large number of single nucleotide polymorphisms (SNPs), typically \\( 10^5 - 10^7 \\), leads to considering an enormous number of SNP pairs (~\\( 10^{10} - 10^{14} \\)).
- **Challenges**:
  - Multiple hypothesis testing.
  - Long computational runtimes.

- **Approaches**:
  - **Exhaustive Enumeration**: Requires specialized hardware like GPUs.
  - **Filtering Methods**: Prioritize SNPs based on statistical criteria (e.g., large main effects) or biological criteria (e.g., protein-protein interactions).

---

## **Conclusion and Future Directions**

- Data mining techniques in computational biology have advanced significantly, providing methods for predicting deleteriousness, phenotypic traits, and uncovering gene interactions.
- Major challenges still include avoiding overfitting, managing small sample sizes, and handling the computational burden of analyzing vast genetic datasets.
