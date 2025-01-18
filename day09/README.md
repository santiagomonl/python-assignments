# DNA Sequence Analysis Tool

This tool allows you to analyze DNA sequences from FASTA or GeneBank files. It provides two main functionalities:

1. Find the longest repeated subsequence in a DNA sequence.

2. Locate a specific codon and display it with 5 upstream and downstream base pairs of context.

## Features

* Processes files in FASTA or GeneBank format.

* Identifies the longest repeating subsequence within the DNA sequence.

* Searches for a specified codon and displays it with its surrounding context.

* Flexible command-line interface for specifying desired analyses.

## Installation

* Clone the repository

* Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Dependencies

The tool requires Python 3.7 or higher and the following packages:

* argparse

* re

* Biopython

Use requirements.txt for installing:
```bash
pip install -r requirements.txt
```

# Usage

## Run the program with the desired options:

``` bash
python analyze.py FILE [--duplicate] [--FindtheCodon CODON]
```

## Options

* FILE: Path to the input file in FASTA or GeneBank format.

* --duplicate: Finds the longest repeated subsequence in the DNA sequence.

* --FindtheCodon CODON: Searches for the specified codon and displays it with 5 upstream and downstream base pairs.

## Examples

* Find the longest repeated subsequence:

```bash
python analyze.py Gliomedin_Homo_sapiens.txt --duplicate
```

*Locate a specific codon (ATG) with context:

```bash
python analyze.py Gliomedin_Homo_sapiens.txt --FindtheCodon ATG
```

* Perform both analyses:

```bash
python analyze.py Gliomedin_Homo_sapiens.txt --duplicate --FindtheCodon ATG
```

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.

