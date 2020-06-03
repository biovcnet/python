# Topic Python Lesson 6 Live code
Set-up & Binder components for Python Lesson 6

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-lesson-6-live-code/master?urlpath=lab)


## Set-up
Relative taxonomic abundance, the ratio of an Operational Taxonomic Unit's (OTU) number of reads to total reads in a sample, is commonly used in 16S rRNA library visualisations and statistics. However, at finer taxonomic divisions than phylum and order, the number of OTUs can quickly become overwhelming for plotting or broader trends/metadata relationships. Additionally, one may be interested in the relative abundance of an OTU across a broader environment type, which requires combining multiple samples. For example: across an subsurface environments, across all photic zone samples, etc.


## Script

In this script, I am going to import a .csv file of OTUs and their respective number of reads in 4 discrete samples that come from a particular subenvironment of a permanently-stratified lake. I am going to calculate the total number of reads of each OTU across all discrete samples, retain only the 20 most abundant OTUs, and calculate their relative abundances. The results will be exported as a .csv file.
