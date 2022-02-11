from divisor_master.checker import *

def getCanonicalDilimitersList(N):
    if N==1: return [1]
    return getCanonicalDilimitersRecursed(N)

def getCanonicalDilimitersRecursed(N):
    result = []
    for i in range(2, N+1):
        if i ==1: return result
        if check_simple(i):
            if N % i == 0:
                result.append(i)
                result = result + getCanonicalDilimitersRecursed(N // i)
                return result
    return result
