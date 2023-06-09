class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total > target:
                R -= 1
            elif total < target:
                L += 1
            else:
                return [L+1, R+1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # L, R = 0, len(numbers)-1
        # while L <= R:
        #     total = numbers[L] + numbers[R]
        #     if target > total:
        #         L += 1
        #     elif target < total:
        #         R -= 1
        #     else:
        #         return [L+1, R+1]
        
        # L, R = 0, len(numbers)-1
        # while L <= R:
        #     total = numbers[L] + numbers[R]
        #     if total < target:
        #         L += 1
        #     elif total > target:
        #         R -= 1
        #     else:
        #         return [L+1, R+1]

        # L, R = 0, len(numbers)-1
        # while L <= R:
        #     cur_sum = numbers[L] + numbers[R]
        #     if cur_sum < target:
        #         L += 1
        #     elif cur_sum > target:
        #         R -= 1
        #     else:
        #         return [L+1, R+1]
        
        # L, R = 0, len(numbers)-1
        # while L<R:
        #     if numbers[L]+numbers[R] == target:
        #         return [L+1, R+1]
        #     while (numbers[L]+numbers[R] < target):
        #         L += 1
        #         continue
        #     while (numbers[L]+numbers[R] > target):
        #         R -= 1
        #         continue