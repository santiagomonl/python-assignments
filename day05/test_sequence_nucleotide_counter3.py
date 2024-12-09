import pytest
from Sequence_nucleotide_counter3 import count_nucleotides, porcetage_nucleotides
import sys
from io import StringIO

def run_script(args, input_text):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    old_argv = sys.argv

    try:
        sys.stdin = StringIO(input_text) 
        sys.stdout = StringIO()  
        sys.argv = args  
        exec(open('Sequence_nucleotide_counter3.py').read()) 
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        sys.argv = old_argv



def test_single_file():
    with open('sequence1.txt', 'w') as f:
        f.write("AGCTNN")

    output = run_script(['Sequence_nucleotide_counter3.py', 'sequence1.txt'], "1\nn") 

    assert "A : 1 16.7%" in output
    assert "C : 1 16.7%" in output
    assert "G : 1 16.7%" in output
    assert "T : 1 16.7%" in output
    assert "Unknown : 2 33.3%" in output
    assert "Total: 6" in output
    assert "All" in output
    assert "A : 1 16.7%" in output 
    assert "Total: 6" in output 

def test_multiple_files():
    with open('sequence1.txt', 'w') as f:
        f.write("AGCTNN")
    with open('sequence2.txt', 'w') as f:
        f.write("AAGGCCT")


    output = run_script(['Sequence_nucleotide_counter3.py', 'sequence1.txt', 'sequence2.txt'], "2\nn")

    assert "A : 1 16.7%" in output 
    assert "Total: 6" in output
    assert "A : 2 28.6%" in output 
    assert "Total: 7" in output 


    assert "All\nA : 3 23.1%" in output
    assert "C : 2 15.4%" in output
    assert "G : 2 15.4%" in output
    assert "T : 2 15.4%" in output
    assert "Unknown : 2 30.8%" in output
    assert "Total: 13" in output


def test_no_files():
    output = run_script(['Sequence_nucleotide_counter3.py'], "0\nn")  
    assert "Total: 0" in output  

def test_empty_file(): 
    with open('sequence1.txt', 'w') as f:
        f.write("")
    output = run_script(['Sequence_nucleotide_counter3.py', 'sequence1.txt'], "1\nn")
    assert "Total: 0" in output
    assert "All\nTotal: 0" in output 



