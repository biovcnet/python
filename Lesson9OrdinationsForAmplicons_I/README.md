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
There are many of these, including (but no limited to): 

 - Principle Coordinates Analysis (PCoA), also know as a multi-dimensional scaling analysis (MDS).
 - Redundancy Analysis
 - Correspondence Analysis/Detrended Correspondence Analysis
 - Canonical Correlation Analysis (CCA)
 
 In this lesson, will be focused on PCoA. 
 
 In a PCoA, a line is fit to a collection of points (in this case, our Jaccard or Bray-Curtis matrices) that most minimizes the average square distance from any   given point to that line. This vector is the first *principle component*, and corresponds to the greatest variance in the matrix. This process is repeated, with the next line being orthogonal to the one before. The results from a PCoA are the *component scores* of the individual data points along that principal component. 
 
Often, software will also return a "proportions explained" datatable showing how much of the dataset's variance is captured by each principal component. This guides the user in chosing the appropriate number of dimensions to examine their data. By using some number of principal components, the complexity of the transformed data set is greatly reduced, which helps in searching for meaningful sample clustering when viewed in principal component space. 

In bioinformatics, the Jaccard or Bray-Curtis matrices that have been transformed by a PCoA are often visualized in a three-dimensional plot that is color-coded using metadata tables. The matrices are associated with metadata values by sample ID. This helps the user visually search for any metadata patterns that match the clustering patterns of the transformed data in PCoA space.
 
 
 
  
  




[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-Lesson9-bindercontent/master)
