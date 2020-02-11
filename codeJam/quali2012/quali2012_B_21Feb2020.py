if __name__ == '__main__':
    T = int(input().strip())

    arr = []

    for j in range(T):
        arr = list(map(int, input().rstrip().split()))
        N = arr[0]
        S = arr[1]
        p = arr[2]
        t = arr[3:]

        score = 0
        S_left = S

        assert( N == len(t) )

        for i in range(len(t)):
            X =  (t[i] - p) // 2

            if ( t[i] == 0 ):
                if ( p == 0 ):
                    score += 1
            elif ( X >= (p-1) ):
                score += 1
            elif ( X == (p-2) and S_left > 0 ):
                score += 1
                S_left -= 1

        print( "Case #" + str(j+1) + ": " + str(score) )




