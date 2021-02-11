def fib(n):     # print deret Fibonacci sampai n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return deret Fibonacci sampai n
    ret = []
    a, b = 0, 1
    while a < n:
        ret.append(a)
        a, b = b, a+b
    return ret
