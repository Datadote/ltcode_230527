class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1], []
        tmp = 1
        for n in nums:
            tmp *= n
            prefix.append(tmp)
        tmp = 1
        for n in nums[::-1]:
            tmp *= n
            postfix.append(tmp)
        postfix = postfix[::-1]
        postfix.append(1)
        # # nums
        # print(prefix)
        # print(postfix)
        for i in range(len(nums)):
            # print(prefix[i], postfix[i+1])
            nums[i] = prefix[i]*postfix[i+1]
        # print(nums)
        return nums