class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        topk = [ele for ele,_ in count.most_common(k)]
        return topk