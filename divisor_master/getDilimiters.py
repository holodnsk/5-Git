def getDilimiters(N):
    dilimiters = [1]
    if N==1:
        return dilimiters
    for i in range(2,N):
        if N%i==0:
          dilimiters.append(i)
    dilimiters.append(N)
    return dilimiters