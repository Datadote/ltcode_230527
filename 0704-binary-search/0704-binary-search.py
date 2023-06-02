class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while L <= R:
            M = L + (R-L)//2
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            else:
                return M
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # L, R = 0, len(nums)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target < nums[M]:
        #         R = M - 1
        #     elif target > nums[M]:
        #         L = M + 1
        #     else:
        #         return M
        # return -1
        
        # L, R = 0, len(nums)-1
        # while L<=R:
        #     M = L + (R-L)//2
        #     if nums[M] == target:
        #         return M
        #     elif nums[M] < target:
        #         L = M+1
        #     else:
        #         R = M-1
        # return -1