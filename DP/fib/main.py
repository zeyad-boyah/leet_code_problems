from functools import cache


@cache 
def fib(n):
    if n<=2: return 1
    return fib(n-1)+ fib(n-2)


print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(40))
print(fib(100))
