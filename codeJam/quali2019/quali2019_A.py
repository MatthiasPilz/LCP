T = int(input())

for i in range(T):
    N = input()

    numDigits = len(N)
    A = ''
    for j in range(numDigits):
        if ( N[j] == '4' ):
            A += '3'
        else:
            A += str(N[j])

    Aint = int(A)
    B = int(N) - Aint

    s = "Case #" + str(i + 1) + ": " + str(Aint) + " " + str(B)
    print(s)