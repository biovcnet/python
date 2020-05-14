# Manipulating .fasta plain text files #

## What is a FASTA file? ##
A FASTA file is one of the most common text files used in bioinformatics across all platforms. 
It is a plain-text file of single-letter nucleotide sequences or amino acid sequences. 
The .fasta extention standards for 'fast-all'

For this exercise, we will be working with a .fasta file of 16S rRNA sequences from SILVA. 
FASTA files from SILVA can be downloaded:

* aligned (with gaps). This means that missing bases (indicated with a `.`) and gaps (indicated with a `-`) are included in the text. This format is useful if you want to directly compare sequences to one another

* with gaps common to all sequences removed (common gaps)

* unaligned (without gaps).

## FASTA FILE FORMATTING ##


Each entry in the FASTA file begins with a `>` . Entries consist of a header and a sequence. 

The header of each entry is found after the `>` and is separated from the associated sequence with the newline character `\n`. The header is formatted `accession_number.start_position.end_position (Taxonomy sequence of varying length/specificity)` :

* The accession number is a unique alphanumeric ID referencing where it is stored in NCBI GenBank
* The start and stop positions reference the beginning and end of the aligned sequences relative to *e. coli* 16S rRNA positions

# Exercise #
We will be working with an aligned `fasta with gaps` formatted fasta file of *Vibrio* 16S rRNA sequences. First, we will remove duplicate accession numbers. Accessions can appear twice, for example, if multiple rRNA regions are matched to the same accession. Secondly, we will create a table from a FASTA file including information like Accession number, start position, and stop positions.
