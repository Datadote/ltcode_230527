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
        for i in range(len(nums)):
            nums[i] = prefix[i]*postfix[i+1]
        return nums