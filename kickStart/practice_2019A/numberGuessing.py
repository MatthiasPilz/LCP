import sys

T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().split())
    N = int(input().strip())

    # first guess 'by hand' --> then start the loop
    lastGuess = (A + B) // 2
    print(lastGuess)
    sys.stdout.flush()

    message = input().strip()
    n = 1
    upper = B
    lower = A + 1

    while (n <= N) and (message != "CORRECT"):
        if message == "WRONG_ANSWER":
            break
        elif message == "TOO_SMALL":
            nextGuess = (lastGuess + upper) // 2
            lower = lastGuess + 1
        elif message == "TOO_BIG":
            nextGuess = (lower + lastGuess) // 2
            upper = lastGuess - 1

        lastGuess = nextGuess
        print(lastGuess)
        sys.stdout.flush()
        message = input().strip()
        n += 1
