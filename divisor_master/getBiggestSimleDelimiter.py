from divisor_master.getDilimiters import *
from divisor_master.checker import *
def getSimpleBiggestDelimiter(N):
    delimiters = getDilimiters(N)
    max = 1
    for i in delimiters:
        if check_simple(i):
            max = i
    return max