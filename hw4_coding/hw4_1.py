import numpy as np

min_loop_length = 4


def pair_check(tup):
    if tup in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
        return True
    return False


def cal_OPT(sequence):
    """\
    Description:
    ------------
        Implement Nussinov algorithm(dynamic programming) and construct the OPT matrix that stores the optimal score. You may use bottom up approach or top down approach.
    Parameter:
    ------------
        sequence: RNA sequence of length n, type `list`.
    Return:
    ------------
        OPT: OPT chart, an np.array of the shape (n,n)
    """
    # Implement your algorithm here

    return OPT


def traceback(OPT, sequence):
    """\
    Description:
    ------------
        Backtracking algorithm, to find the pairing of bases in RNA sequence according to DP chart.
        You can add new utility functions to help you.    
    Parameter:
    ------------
        OPT: OPT matrix from cal_OPT(sequence)
        sequence: RNA sequence of length n, type `list`.
        fill feel to include more parameters into the function aside from `OPT` and `sequence`...
    Return:
    ------------
        structure: 
            a list of tuples that stores the pairing of the optimal solution, 
            e.g. 
            For a sequence with connection of bases 1 and 2, 3 and 4(1, 2, 3, 4 are indices, counting from 0 to n-1 for sequence of length n),
            the returned structure should be [(1, 2), (3, 4)]
    """
    # Implement your algorithm here


sequences = []
with open("test_data", "r") as fp:
    for seq in fp:
        sequences.append(seq.strip("\n"))

for i, seq in enumerate(sequences):
    OPT = cal_OPT(seq)

    structure = traceback(OPT, seq)
    print(structure)
    with open("result_" + str(i) + ".txt", "w") as fp:
        for pair in structure:
            fp.write(str(pair) + "\n")
