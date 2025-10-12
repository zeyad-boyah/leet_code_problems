class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def memoize(func):
            cache = {}
            def wrapper(*args):
                if args in cache:
                    return cache[args]
                result = func(*args)
                cache[args] = result
                return result
            return wrapper

        @memoize
        def dfs(i):
            if i>= n:
                return i == n
            return dfs( i +1) + dfs(i+2)
        
        return dfs(0)
    