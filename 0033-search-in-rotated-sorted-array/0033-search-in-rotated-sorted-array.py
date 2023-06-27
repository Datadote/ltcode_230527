class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            L, R = 0, len(nums)-1
            min_v = math.inf
            pivot = -1
            while L <= R:
                M = L + (R-L)//2
                if min_v > nums[M]:
                    min_v = nums[M]
                    pivot = M
                if nums[M] > nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            return pivot
        
        
        def bsearch(nums, target, L, R):
            # L, R = 0, len(nums)-1
            # print('start', pivot, nums, L, R)
            while L <= R:
                M = L + (R-L)//2
                if target > nums[M]:
                    L = M + 1
                elif target < nums[M]:
                    R = M - 1
                else:
                    return M
            return -1
        
        # B search left or right side depending on pivot
        pivot = find_pivot(nums)
        # print(pivot,nums, target)
        
        if target == nums[pivot]:
            return pivot
        if pivot == 0:
            return bsearch(nums, target, 0, len(nums)-1)
        if target < nums[0]: # search right
            # print('search right')
            return bsearch(nums, target, pivot+1, len(nums)-1)
        else:
            return bsearch(nums, target, 0, pivot)
        