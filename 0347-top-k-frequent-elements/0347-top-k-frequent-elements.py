class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        topk = [x for x,_ in count.most_common(k)]
        return topk
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = defaultdict(int)
#         for n in nums:
#             d[n] += 1
#         topk = sorted(d.items(), key = lambda x: x[1])[::-1]
#         topk = [x[0] for x in topk[:k]]
#         return topk
        
        # count = Counter(nums)
        # topk = [ele for ele,_ in count.most_common(k)]
        # return topk