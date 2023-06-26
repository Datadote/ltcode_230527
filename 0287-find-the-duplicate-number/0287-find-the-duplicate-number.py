class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # slow = fast = 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[fast]
        #     fast = nums[fast]
        #     if nums[slow] == nums[fast]:
        #         break
        # slow2 = 0
        # while True:
        #     slow2 = nums[slow2]
        #     slow = nums[slow]
        #     if slow == slow2:
        #         return slow2