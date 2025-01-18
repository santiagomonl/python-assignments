import argparse
import re

def read_fasta_or_genbank(file_path):
    """Reads a FASTA or GeneBank file and returns the sequence as a string."""
    with open(file_path, 'r') as file:
        sequence = []
        for line in file:
            if not line.startswith('>') and not line.startswith('LOCUS') and not line.startswith('ORIGIN'):
                sequence.append(line.strip())
        return ''.join(sequence)

def find_longest_repeated_subsequence_optimized(sequence, k): # k is the k-mer size
    """Finds the longest subsequence that repeats itself in the sequence."""
    kmers = {}
    longest_repeat = ""

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        if kmer in kmers:
            if len(kmer) > len(longest_repeat):
                longest_repeat = kmer  # Or handle multiple occurrences
        else:
            kmers[kmer] = i

    return longest_repeat

def find_codon_with_context(sequence, codon, context=5):
    """Finds all occurrences of a codon and prints the codon with upstream and downstream context."""
    matches = [(m.start(), m.end()) for m in re.finditer(codon, sequence)]
    results = []

    for start, end in matches:
        upstream = sequence[max(0, start - context):start]
        downstream = sequence[end:end + context]
        results.append((upstream, codon, downstream))

    return results

def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences.")
    parser.add_argument("file", help="Path to the input file (FASTA or GeneBank format).")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated subsequence.")
    parser.add_argument("--FindtheCodon", type=str, help="Codon to search for with context.")

    args = parser.parse_args()
    sequence = read_fasta_or_genbank(args.file)

    if args.duplicate:
        longest_subsequence = find_longest_repeated_subsequence_optimized(sequence, k=10)  # Specify a k-mer size here
        print(f"Longest repeated subsequence: {longest_subsequence}")


    if args.FindtheCodon:
        codon_results = find_codon_with_context(sequence, args.FindtheCodon)
        print(f"Occurrences of codon '{args.FindtheCodon}' with context:")
        for upstream, codon, downstream in codon_results:
            print(f"{upstream}[{codon}]{downstream}")

if __name__ == "__main__":
    main()
