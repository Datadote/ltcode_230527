class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        min_v = math.inf
        while L <= R:
            M = L + (R-L)//2
            min_v = min(min_v, nums[M])
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M - 1
        return min_v
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # L, R = 0, len(nums)-1
        # min_v = math.inf
        # while L <= R:
        #     M = L + (R-L)//2
        #     min_v = min(min_v, nums[M])
        #     if nums[M] > nums[R]:
        #         L = M + 1
        #     else:
        #         R = M - 1
        # return min_v

        # min_v = math.inf
        # L, R = 0, len(nums)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     min_v = min(min_v, nums[M])
        #     if nums[M] > nums[R]:
        #         L = M + 1
        #     else:
        #         R = M - 1
        # return min_v

        # L, R = 0, len(nums) - 1
        # min_num = math.inf
        # while L <= R:
        #     M = L + (R-L)//2
        #     min_num = min(min_num, nums[M])
        #     # print(min_num, M, nums[M])
        #     if nums[M]>=nums[L] and nums[L]<nums[R]:
        #         R = M - 1
        #     elif nums[M]<=nums[R] and nums[L]>nums[R]:
        #         R = M - 1
        #     else:
        #         L = M + 1
        # return min_num