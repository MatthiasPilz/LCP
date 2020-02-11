import math


def find_primeFactors(A):
    A2 = int(math.ceil(math.sqrt(float(A))))

    for i in range(A2, 1, -1):
        if A % i == 0:
            Y = A / i
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

    for c in S:
        [X, Y] = find_primeFactors(int(c))
        order.append([X, Y])
        d.add(X)
        d.add(Y)

    for i in range(1, len(order)):
        if order[i][0] in order[i - 1]:
            order[i - 1].remove(order[i][0])
        else:
            order[i - 1].remove(order[i][1])

    cypher = sorted(d)

    result = ''
    for i in range(L):
        result += alpha[cypher.index(order[i][0])]
    # last letter!
    result += alpha[cypher.index(order[L-1][1])]

    print("Case #" + str(t + 1) + ": " + result)
