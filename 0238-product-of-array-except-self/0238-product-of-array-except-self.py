class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1], [1]
        tmp = 1
        for n in nums:
            tmp *= n
            pre.append(tmp)
        tmp = 1
        for n in nums[::-1]:
            tmp *= n
            post.append(tmp)
        post = post[::-1]
        for i in range(len(nums)):
            nums[i] = pre[i] * post[i+1]
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # pre, post = [1], [1]
        # tmp = 1
        # for n in nums:
        #     tmp *= n
        #     pre.append(tmp)
        # tmp = 1
        # for n in nums[::-1]:
        #     tmp *= n
        #     post.append(tmp)
        # post = post[::-1]
        # for i in range(len(nums)):
        #     nums[i] = pre[i] * post[i+1]
        # return nums
    
        # pre, post = [1], [1]
        # tmp = 1
        # for n in nums:
        #     tmp *= n
        #     pre.append(tmp)
        # tmp = 1
        # for n in nums[::-1]:
        #     tmp *= n
        #     post.append(tmp)
        # post = post[::-1]
        # for i in range(len(nums)):
        #     nums[i] = pre[i] * post[i+1]
        # return nums
        
        # pre, post = [1], [1]
        # tmp = 1
        # for n in nums:
        #     tmp *= n
        #     pre.append(tmp)
        # tmp = 1
        # for n in nums[::-1]:
        #     tmp *= n
        #     post.append(tmp)
        # post = post[::-1]
        # for i in range(len(nums)):
        #     nums[i] = pre[i] * post[i+1]
        # return nums