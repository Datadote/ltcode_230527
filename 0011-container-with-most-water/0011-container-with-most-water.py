class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_a = 0
        L, R = 0, len(height) - 1
        while L < R:
            area = (R-L) * min(height[L], height[R])
            max_a = max(max_a, area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_a
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_a = 0
        # L, R = 0, len(height)-1
        # while L < R:
        #     area = (R-L) * min(height[L], height[R])
        #     max_a = max(max_a, area)
        #     if height[L] <= height[R]:
        #         L += 1
        #     else:
        #         R -= 1
        # return max_a        
        
        # max_a = -math.inf
        # L, R = 0, len(height)-1
        # while L < R:
        #     area = (R-L) * min(height[L], height[R])
        #     max_a = max(max_a, area)
        #     if height[L] > height[R]:
        #         R -= 1
        #     else:
        #         L += 1
        # return max_a
        
        # L, R = 0, len(height)-1
        # max_a = min(height[L], height[R]) * (R-L+1)
        # while L < R:
        #     if height[R] > height[R-1]:
        #         R -= 1
        #         continue
        #     else:
        #     # : height[L] > height[L+1]:
        #         L += 1
        #         continue
        #     area = min(height[L], height[R]) * (R-L+1)
        #     max_a = max(max_a, area)
        #     L += 1
        # return max_a