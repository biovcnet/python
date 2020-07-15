# Python Lesson 9: 

## Ordinations I - Jaccard and Bray-Curtis beta diversity analyses

### What are alpha and beta diversity?

Metrics are used in bioinformatics to broadly answer:

- how species-rich or species-uniform is a sample -**alpha diversity**
- how different is the microbial composition in one environment or sample -**beta diversity**

There are many Alpha and Beta diversity metrics, and it can sometimes be confusing or difficult to determine which is the correct to use to answer your specific research questions.

In this lesson we will be focused on **beta Diversity** metrics that do not require using a phylogenetic tree. 

These include:

- ***Bray–Curtis dissimilarity***:
  - Takes the relative abundances of species in each sample into account
  - Ranges from 0 to 1
  - 0 means the relative abundances of species of each of the two samples are exactly alike
  - 1 means the relative abundances of species of each of the two samples are completely different
  
- ***Jaccard distance***:
  - Does not take the relative abundances of species in each sample into account. This means the species abundances are converted to a *binary* format- Present (1) or absent (0).




[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-Lesson9-bindercontent/master)
