import pytest
from Sequence_nucleotide_counter3 import count_nucleotides, porcetage_nucleotides
import sys
from io import StringIO

# Helper function to simulate running the script with arguments and input
def run_script(args, input_text):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    old_argv = sys.argv

    try:
        sys.stdin = StringIO(input_text)  # Simulate user input
        sys.stdout = StringIO()  # Capture printed output
        sys.argv = args  # Simulate command line arguments
        exec(open('Sequence_nucleotide_counter3.py').read()) # Execute the script
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        sys.argv = old_argv



def test_single_file():
    with open('sequence1.txt', 'w') as f:
        f.write("AGCTNN")

    output = run_script(['Sequence_nucleotide_counter3.py', 'sequence1.txt'], "1\nn") # 1 for one file, n to stop

    assert "A : 1 16.7" in output
    assert "C : 1 16.7" in output
    assert "G : 1 16.7" in output
    assert "T : 1 16.7" in output
    assert "Unknown : 2 33.3" in output
    assert "Total: 6" in output
    assert "All" in output
    assert "A : 1 16.7" in output # all section should be the same as single file in this case
    assert "Total: 6" in output # total in all section

    os.remove('sequence1.txt')




def test_multiple_files():
    with open('sequence1.txt', 'w') as f:
        f.write("AGCTNN")
    with open('sequence2.txt', 'w') as f:
        f.write("AAGGCCT")


    output = run_script(['Sequence_nucleotide_counter3.py', 'sequence1.txt', 'sequence2.txt'], "2\nn")

    # Check individual file outputs (order might matter based on your script)
    assert "A : 1 16.7" in output  # File 1
    assert "Total: 6" in output # file 1
    assert "A : 2 28.6" in output # file 2
    assert "Total: 7" in output # file 2


    #Check Combined "All" Output
    assert "All\nA : 3 23.1" in output
    assert "C : 2 15.4" in output
    assert "G : 2 15.4" in output
    assert "T : 2 15.4" in output
    assert "Unknown : 2 30.8" in output
    assert "Total: 13" in output # Combined total


def test_no_files():
    output = run_script(['Sequence_nucleotide_counter3.py'], "0\nn")  # 0 files, n to stop
    assert "Total: 0" in output  # Or whatever your script should output when no files provided




