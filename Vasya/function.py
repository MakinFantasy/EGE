def f(n):
    s = 0
    while n > 0:
        o = n % 10
        s += o
        n = n // 10
    return s


res = f(131)
print(res)
        
