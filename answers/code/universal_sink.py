# author: Hendrik Werner s4549775
# author: Constantin Blach s4329872
from numpy import matrix, sum


def is_sink(m, i):
    """
    Check whether element i is a universal sink of matrix m.

    Time complexity: O(n)

    :param m: an adjacency matrix
    :param i: the index of the element to check
    :return: whether i as a universal sink of m
    """
    sink = m[i, i] == 0
    if sink:
        sink = sum(m[i]) == 0  # out-degree
    if sink:
        sink = sum(m[:, i]) == m.shape[0] - 1  # in-degree
    return sink


def contains_universal_sink(m):
    """
    Check whether matrix m contains a universal sink.

    Time complexity: O(n)

    :param m: an adjacency matrix
    :return: whether the matrix contains a universal sink
    """
    n = m.shape[0]
    row = 0
    col = 0
    while row < n and col < n:
        if m[row, col]:
            row += 1
        else:
            col += 1
    return row < n and is_sink(m, row)
