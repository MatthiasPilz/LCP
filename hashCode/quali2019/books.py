def read_input():
    # B - books
    # L - libraries
    # D - days
    B, L, D = map(int, input().split())

    # S - scores
    S = list(map(int, input().split()))

    # N - ID of the books
    # T - time to sign up
    # M - number of books per day
    N = []
    T = []
    M = []
    for j in range(L):
        N_j, T_j, M_j = map(int, input().split())

        T.append(T_j)
        M.append(M_j)

        N_j = list(map(int, input().split()))
        N.append(N_j)
        # N[L][j] first index is the library, second list is the available books

    return B, L, D, S, N, T, M

def print_all(B, L, D, S, N, T, M):
    print(B)
    print(L)
    print(D)
    print(S)
    print(N)
    print(T)
    print(M)

def sort_andReturnIndex(A):
    return sorted(range(len(A)), key=lambda k: A[k])

def find_maxPossibleBookExport(D, N, T, M):
    maxBookExport = []
    for i in range(len(N)):
        maxBookExport.append((D-T[i])*M[i])

    return maxBookExport

def solution_sortedByTime(B, L, D, S, N, T, M):
    # sort libraries by lenght of sign-up
    T_indexSorted = sort_andReturnIndex(T)

    # Y is the output of which library we sign up to (ordered)
    Y = T_indexSorted

    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))
        bookIDs.append(N[Y[i]])

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def solution_sortedByBooksExported(B, L, D, S, N, T, M):
    # sort libraries by lenght of sign-up
    booksExported_indexSorted = sort_andReturnIndex(find_maxPossibleBookExport(D, N, T, M))

    # Y is the output of which library we sign up to (ordered)
    Y = booksExported_indexSorted

    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))
        bookIDs.append(N[Y[i]])

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def solution_sortedByScore(B, L, D, S, N, T, M):
    sumOfScores = calc_scores(S, N)

    sumOfScores_sortedByIndex = sort_andReturnIndex(sumOfScores)
    Y = sumOfScores_sortedByIndex
    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))
        bookIDs.append(N[Y[i]])

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def calc_scores(S, N):
    sumOfScores = [0 for i in range(len(N))]

    for i in range(len(N)):
        for b in N[i]:
            sumOfScores[i] += S[b]
    return sumOfScores

def solution_sortedByTimeAndBookScore(B, L, D, S, N, T, M):
    # sort libraries by lenght of sign-up
    T_indexSorted = sort_andReturnIndex(T)

    # Y is the output of which library we sign up to (ordered)
    Y = T_indexSorted

    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))

        listOfBooksInCurrentLibrary = N[Y[i]]
        scoresOfCurrentLibrary = []
        for j in range(len(N[Y[i]])):
            scoresOfCurrentLibrary.append(S[listOfBooksInCurrentLibrary[j]])

        scoresOfCurrentSorted = sort_andReturnIndex(scoresOfCurrentLibrary)
        scoresOfCurrentSorted.reverse()

        bookIDperLibrary = []
        for k in range(len(N[Y[i]])):
            indexWithHighestScore = scoresOfCurrentSorted[k]
            bookIDperLibrary.append(N[Y[i]][indexWithHighestScore])

        bookIDs.append(bookIDperLibrary)

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def solution_sortedByScoreFIXED(B, L, D, S, N, T, M):
    sumOfScores = calc_scores(S, N)

    sumOfScores_sortedByIndex = sort_andReturnIndex(sumOfScores)

    # FIXED SORTING :)
    sumOfScores_sortedByIndex.reverse()

    Y = sumOfScores_sortedByIndex
    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))
        bookIDs.append(N[Y[i]])

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def solution_sortedByBooksExportedANDScores(B, L, D, S, N, T, M):
    # sort libraries number of books they could export if we sign up on day one..
    booksExported_indexSorted = sort_andReturnIndex(find_maxPossibleBookExport(D, N, T, M))
    booksExported_indexSorted.reverse()

    # Y is the output of which library we sign up to (ordered)
    Y = booksExported_indexSorted

    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))

        listOfBooksInCurrentLibrary = N[Y[i]]
        scoresOfCurrentLibrary = []
        # print(listOfBooksInCurrentLibrary)
        for j in range(len(N[Y[i]])):
            scoresOfCurrentLibrary.append(S[listOfBooksInCurrentLibrary[j]])

        scoresOfCurrentSorted = sort_andReturnIndex(scoresOfCurrentLibrary)
        scoresOfCurrentSorted.reverse()
        # print(scoresOfCurrentLibrary)
        # print(scoresOfCurrentSorted)
        # print("")

        bookIDperLibrary = []
        for k in range(len(N[Y[i]])):
            indexWithHighestScore = scoresOfCurrentSorted[k]
            bookIDperLibrary.append(N[Y[i]][indexWithHighestScore])

        bookIDs.append(bookIDperLibrary)

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

def solution_FariborzSplitSorting(B, L, D, S, N, T, M, one, two):
    firstB = one
    secondB = two

    T_indexSorted = sort_andReturnIndex(T)
    Y = T_indexSorted[:firstB]

    T_indexSorted[:firstB] = []

    sumOfScores = calc_scores(S, N)
    for i in range(len(Y)):
        del sumOfScores[Y[i]]

    sumScores_sorted = sort_andReturnIndex(sumOfScores)
    sumScores_sorted.reverse()

    counter = 0
    k = 0
    while counter < secondB-firstB:
        if sumScores_sorted[k] not in Y:
            Y.append(sumScores_sorted[k])
            counter += 1
        k += 1

    missingLibraries = []
    for i in range(L):
        if i not in Y:
            missingLibraries.append(i)

    timeOfMissingLibraries = []
    for i in range(len(missingLibraries)):
        timeOfMissingLibraries.append(T[i])

    missingLibraries_sorted = sort_andReturnIndex(timeOfMissingLibraries)

    for i in range(len(missingLibraries_sorted)):
        Y.append(missingLibraries[missingLibraries_sorted[i]])

    K = []
    bookIDs = []
    for i in range(L):
        K.append(len(N[Y[i]]))

        listOfBooksInCurrentLibrary = N[Y[i]]
        scoresOfCurrentLibrary = []
        for j in range(len(N[Y[i]])):
            scoresOfCurrentLibrary.append(S[listOfBooksInCurrentLibrary[j]])

        scoresOfCurrentSorted = sort_andReturnIndex(scoresOfCurrentLibrary)
        scoresOfCurrentSorted.reverse()

        bookIDperLibrary = []
        for k in range(len(N[Y[i]])):
            indexWithHighestScore = scoresOfCurrentSorted[k]
            bookIDperLibrary.append(N[Y[i]][indexWithHighestScore])

        bookIDs.append(bookIDperLibrary)

    A = L
    print(A)
    for i in range(A):
        print(str(Y[i]) + " " + str(K[i]))
        print(*bookIDs[i])

if __name__ == "__main__":
    B, L, D, S, N, T, M = read_input()
    #print_all(B, L, D, S, N, T, M)
    #solution_sortedByTime(B, L, D, S, N, T, M)                     # --> firstSolution
    #solution_sortedByScore(B, L, D, S, N, T, M)                    # --> secondSolution
    #solution_sortedByBooksExported(B, L, D, S, N, T, M)            # --> 3
    #solution_sortedByScoreFIXED(B, L, D, S, N, T, M)                # --> 4
    #solution_sortedByTimeAndBookScore(B, L, D, S, N, T, M)          # --> 5
    #solution_sortedByBooksExportedANDScores(B, L, D, S, N, T, M)    # --> 6

    one = int(0.01*L)
    two = int(0.99*L)
    solution_FariborzSplitSorting(B, L, D, S, N, T, M, one, two)
