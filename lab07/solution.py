import numpy as np


def reshape_rows(values, width):
    if len(values) % width:
        return []
    return np.asarray(values, dtype=float).reshape(-1, width).tolist()


def block(matrix, rows, columns):
    return np.asarray(matrix, dtype=float)[np.ix_(rows, columns)].tolist()


def column_means(matrix):
    if not len(matrix):
        return []
    return np.round(np.asarray(matrix, dtype=float).mean(axis=0), 6).tolist()


def column_range(matrix, column):
    col = np.asarray(matrix, dtype=float)[:, column]
    return float(np.round(np.ptp(col), 6))