class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            L, R = i+1, len(nums)-1
            while L<R:
                total = nums[i] + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L<R and nums[L] == nums[L-1]:
                        L += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 break
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
            
#             L, R = i+1, len(nums)-1
#             while L < R:
#                 total = nums[i] + nums[L] + nums[R]
#                 if total > 0:
#                     R -= 1
#                 elif total < 0:
#                     L += 1
#                 else:
#                     res.append([nums[i], nums[L], nums[R]])
#                     L += 1
#                     while L<R and nums[L]==nums[L-1]:
#                         L += 1
#         return res 
        
#         res = []
#         nums.sort() # python sort = mergesort variant = O(n)
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
            
#             L, R = i+1, len(nums)-1
#             while L < R:
#                 total = nums[i] + nums[L] + nums[R]
#                 if total > 0:
#                     R -= 1
#                 elif total < 0:
#                     L += 1
#                 else:
#                     res.append([nums[i], nums[L], nums[R]])
#                     L += 1
#                     while nums[L]==nums[L-1] and L < R:
#                         L += 1
#         return res