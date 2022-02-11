def check_simple(n):
    if n==1 or n==2 or n==3:
        return True
    for i in range(2,n):
        if n%i==0:
            print (n,i,n%i)
            return False
    return True
