def getBiggestDelimiter(N):
    for i in range(N//2, 1, -1):
        if N % i == 0:
            return i