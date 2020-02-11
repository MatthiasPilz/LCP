import math


def find_primeFactors(A):
    A2 = int(math.floor(math.sqrt(float(A))))

    if A2 % 2 == 0:
        A2 -= 1

    for i in range(A2, 1, -2):
        if A % i == 0:
            Y = A // i
            break

    return [i, int(Y)]


T = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(T):
    Ns, Ls = input().split()

    N = int(Ns)
    L = int(Ls)

    S = input().split()

    order = []
    d = set()

    [X, Y] = find_primeFactors(int(S[0]))
    if (int(S[1]) % X == 0):
        order.append(Y)
        order.append(X)
        order.append(int(S[1]) // X)
    else:
        order.append(X)
        order.append(Y)
        order.append(int(S[1]) // Y)

    for i in range(2, L):
        order.append(int(S[i]) // order[i])

    d = set(order)

    cypher = sorted(d)

    result = ''
    for i in range(L+1):
        result += alpha[cypher.index(order[i])]

    print("Case #" + str(t + 1) + ": " + result)