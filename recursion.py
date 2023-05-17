def xPWRn(x,n):
    if x == 0:
        return 1
    if x == 1:
        return 1
    if n == 0:
        return 1
    if n % 2 == 0:
        return xPWRn(x, n//2) * xPWRn(x, n//2)
    else:
        a = xPWRn(x, (n-1)//2)
        return x * a * a

def fibbNum(x):
    if x == 0 or x == 1:
        return 1
    return x*fibbNum(x-1)


ans = xPWRn(4,3)
print(ans) 

res = fibbNum(5)
print(res)