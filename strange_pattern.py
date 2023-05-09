import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    n, m = shape
    pattern = np.full(shape , False, dtype = bool)
    for j in range(m):
        for i in range(n):
            if (i % 3 == 0 and j % 3 == 0) or (i % 3 == 1 and j % 3 == 2) or (i % 3 == 2 and j % 3 == 1):
                pattern[i, j] = True
    return pattern







if __name__ == "__main__":
    print(strange_pattern((6, 8)))
    print(strange_pattern((2,2)))
