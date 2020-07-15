# Python Lesson 9: 

## Ordinations I - Jaccard and Bray-Curtis beta diversity analyses

### What are alpha and beta diversity?

Metrics are used in bioinformatics to broadly answer:

- how species-rich or species-uniform is a sample -**alpha diversity**
- how different is the microbial composition in one environment or sample -**beta diversity**

There are many Alpha and Beta diversity metrics, and it can sometimes be confusing or difficult to determine which is the correct to use to answer your specific research questions.

In this lesson we will be focused on **beta Diversity** metrics that do not require using a phylogenetic tree. 
Because alpha diversity metrics also require a phylogenetic tree, the beta diversity metrics requiring one will be addressed during that lesson. 

These include:

- ***Bray–Curtis dissimilarity***:
  - Takes the relative abundances of species in each sample into account
  - Ranges from 0 to 1
  - 0 means the relative abundances of species of each of the two samples are exactly alike
  - 1 means the relative abundances of species of each of the two samples are completely different
  
- ***Jaccard distance***:
  - Does not take the relative abundances of species in each sample into account. This means the species abundances in each sample are treated as *binary*- present or absent.
  - Ranges from 0 to 1
  - 0 means that the two samples have exactly the same species
  - 1 means that the two samples have no species in common
  
Typically, the Bray-Curtis dissimilarity and/or Jaccard distance is determined for all combinations of samples in an OTU table. The resulting two-dimensional dataset is called a distance or dissimilarity *matrix*
  
 ### OK, I have a beta diversity matrix. What do I do with it?
 
 Once a distance or dissimilarity matrix is created, it is common to perform some sort of ***Ordination Analysis*** with it. 
  
  




[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-Lesson9-bindercontent/master)
