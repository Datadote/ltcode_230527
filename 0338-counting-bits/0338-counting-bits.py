class Solution:
    def countBits(self, n: int) -> List[int]:
        def numBits(n):
            res = 0
            while n:
                res += n % 2
                n = n >> 1
            return res
        res = []
        for i in range(n+1):
            res.append(numBits(i))
        return res