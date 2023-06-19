class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2}
        def fibo(n):
            if n in d:
                return d[n]
            tmp = fibo(n-1) + fibo(n-2)
            d[n] = tmp
            return tmp
        return fibo(n)