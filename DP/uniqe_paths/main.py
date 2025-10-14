from functools import cache

@cache
def number_of_ways(n,m):
    if (n ==0 or m==0) : return 0
    if (n == 1 and m==1): return 1

    return number_of_ways(m-1, n) + number_of_ways(m,n-1)


print(number_of_ways(1,1))
print(number_of_ways(2,1))
print(number_of_ways(9,9))
print(number_of_ways(90,800))
print(number_of_ways(900,90))