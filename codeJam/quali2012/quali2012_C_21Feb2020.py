T = int(input().strip())

arr = []

for j in range(T):
    arr = list(map(int, input().rstrip().split()))
    A = arr[0]
    B = arr[1]

    score = 0

    for k in range(A,B+1):
        k_str = str(k)
        for i in range(1,len(k_str)):
            x = k_str[i:] + k_str[:i]
            if (x[0] != '0'):
                if ( int(x) == k ):
                    break
                if( int(x) <= B and int(x) != k and int(x) > k ):
                    score += 1

    print( "Case #" + str(j+1) + ": " + str(score) )