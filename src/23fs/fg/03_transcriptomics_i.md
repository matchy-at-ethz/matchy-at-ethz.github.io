# Transcriptomics I

Unimportant text is grayed out but worth reading for fluency and context.

## Motivation

<span style="color:lightgray">
We are interested in the expression of genes in a cell. Altough <u>proteins are the actors</u> of genes instead of mRNA transcripts, <em>mRNAs transcripts are easier to measure</em> because selection has chosen them to convey the genetic message in a faithful way. Also there are plenty of interesting <em>non-coding RNAs</em>.
</span>

## RNA species

80% of the total RNA is rRNA. 14% is tRNA. Only 1-3% is mRNA. All other species
account for the remaining 1-3%.

![RNA species](img/03-rna-species.png)
![Prevalence of RNA species](img/03-rna-prevalence-pie-chart.png)

## RNA selection methods

![RNA selection methods](img/03-rna-selection-method.png)

- A: total RNA
  - Unbiased estimation
  - Dominate by rRNA, not very informative
- B: ribosomal reduction/depletion
  - Use probes that bind to rRNA and pull them out
  - < 5% rRNA left
- C: poly-A selection
  - Use probes that bind to poly-A tails
  - Selects for mRNA, and also some long non-coding RNAs (because they also have
    poly-A tails)
- D: cDNA capture
  - Design target probes that bind to a certain set of RNAs
  - Limited transcriptome coverage

<span style="color:lightgray">
90% of transcriptome research utilize poly-A
selection; 5% of them go for ribosomal depletion because their mRNAs are of low
quality and fragmented. The rest 5% do have high-quality mRNAs but still go for
ribosomal depletion because they want to estimate other RNA species at the same time.</span>

Note: current illumina sequencers cannot sequence miRNAs (20-25nt) and mRNA
fragments (100-300nt) together (<u>because of the large length discrepency</u>)

## RNA-seq experiment workflow

A typical RNA-seq experiment workflow is shown below.

![Typical RNA-seq experiment](img/03-rna-seq-experiment-workflow.png)

We can do either single-read sequencing or paired-end sequencing (as is shown in
the figure above) in the third step.

![Paired-end sequencing](img/03-paired-end-seq.png)

## RNA-seq mapping methods

### Considerations

#### How to map reads to a genome?

#### What if we want to map billions of reads?

#### How to deal with introns?

- Approaches
  - Map directly to **trapscript sequences** (no intron) not to the genome
    - Pro: introns are not a problem
    - Cons: unknown genes/isoforms cannot be detected
  - Spliced alignment to genome
    - Pro: finds reads from unknown gene loci or unknown isoforms
    - Con: larger search space, potentially more false positives, wrong
      alignment to pseudogenes
  - Combination of above

Sometimes a gene has an associated *retrotransposed* pseudogenes. They have
almost the same sequence as the original gene, but they are not functional
because they do not have access to promotors and thus won't be
transcribed.Usually they also contain more mutations because there are no
selection pressures to keep them intact.

### Bowtie

### TopHat2

### STAR

## Quality control and reporting considerations after mapping

### PHREAD quality

### Read trimming

Systemetic errors of sequencer

Short read length w/ paired end sequencing

3'-bias / degradation

soft trimming

### Multiple alignments and report considerations

## Expression quantification

### How to count reads?

#### Reporting isoforms

#### EM estimation

#### Alignment-free RNA-seq quantification

### Normalization
