import numpy as np


def main():
    m, n = map(int, input().split())
    x = list(map(int, input().split()))
    x = np.array(x)

    result = find_pizzaOrder_BF(m, n, x)
    print(len(result))
    print(*result)


def find_pizzaOrder_BF(m, n, x):
    slices = 0
    index = n-1
    indices = []
    while slices < m and index >= 0:
        if slices + x[index] <= m:
            slices += x[index]
            indices.append(index)

        index -= 1

    indices.reverse()
    return indices


if __name__ == "__main__":
    main()

'''    
def find_maxSlices(m, n, x):
    c = 0.0001
    s = np.array([0])

    for i in range(n):
        t = x[i] + s
        u = np.union1d(t, s)

        y = u[0]
        s = np.array([y])

        for z in u:
            if y + c*m/n < z <= m:
                y = z
                s = np.append(s, z)

    return s[-1]
'''
