# Topic Python Lesson 5 Live code
Set-up & Binder components for Python Lesson 5

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biovcnet/topic-python-lesson-5-live-code/master?urlpath=lab)


## Set-up
Accessing data from NCBI can sometimes be a pain in the a**. One common problem I run into is downloading genomes from GenBank in a large-scale automated fashion.

(Almost) Daily NCBI produces an update of the current genomes in GenBank. You can download that content through their [FTP website](ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/).

The file `assembly_summary_genbank.txt` contains identifiers and the FTP address for all genomes in GenBank. For the version I am currently looking at consists of file that is **212MB** and contains **722,260** genome entries.

If we had a list of unique identifiers linked to genomes we were interested in, we could create a file that has the FTP locations of all the files we are interested in, and download them using the Unix command `wget`.

## Script

Provided a list of unique identifiers, create `wget` commands to download the genome files of interest.

The file `assembly_summary_genbank_subset.txt` contains 15 entries to practice parsing with - `sag-uniq-ids.txt` & `taxon-ids.txt` provide two different types of unique identifiers that can be parsed from this list.
