class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            tmp = dfs(i+1)
            if (i < len(s)-1
                and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'))
               ):
                tmp += dfs(i+2)
            dp[i] = tmp
            return tmp
        return dfs(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dp = {len(s): 1}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == '0':
        #         return 0
        #     tmp = dfs(i+1)
        #     if (i < len(s)-1
        #         and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'))
        #        ):
        #         tmp += dfs(i+2)
        #     dp[i] = tmp
        #     return tmp
        # return dfs(0)
        
        # dp = {len(s): 1}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == '0':
        #         return 0
        #     tmp = dfs(i+1)
        #     if (i < len(s)-1
        #         and ((s[i] == '1') or (s[i] == '2' and s[i+1] in '0123456'))
        #        ):
        #         tmp += dfs(i+2)
        #     dp[i] = tmp
        #     return tmp
        # return dfs(0)
        
        # dp = {len(s): 1}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == '0':
        #         return 0
        #     tmp = dfs(i+1)
        #     if (i < len(s) - 1
        #         # 10-19 are double digit, 20-26 are other case
        #         and ((s[i]=='1') or (s[i]=='2' and s[i+1] in '0123456'))
        #        ):
        #         tmp += dfs(i+2)
        #     dp[i] = tmp
        #     return tmp
        # return dfs(0)