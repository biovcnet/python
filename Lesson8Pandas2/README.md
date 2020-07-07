## Python Lesson 8: Pandas, Part 2

Now that we have established the basic syntax and usage of python pandas, we are going to move on to a more practical example of how pandas is used in bioinformatics. Along the way, I will also introduce some of the more advanced pandas functions, such as multi-index slicing and `.groupby` 

In the below-linked python notebook, we will import a Particle-Associated OTU table and a metadata table from my own field work at Fayetteville Green Lake, NY. By Particle-Associated, I refer to DNA that was extracted from particles that were captured on a 2.7 micron filter. The tasks will be:

- clean up the metadata table (get rid of entries that are not in the OTU table)
- clean up the OTU table
- filter the OTU table to retain only photoautotrophs (in Fayetteville Green Lake, these include Purple and Green Sulfur Bacteria and Cyanobacteria)
- Examine the abundances of the photoautotrophs in relationship to relevant binned (categorical) metadata 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-Lesson8-bindercontent/master)
