class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            large = -heapq.heappop(stones)
            small = -heapq.heappop(stones)
            diff = large - small
            if diff > 0:
                heapq.heappush(stones, -diff)
        return -stones[0] if stones else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stones = [-x for x in stones]
        # heapq.heapify(stones)
        # while len(stones) > 1:
        #     large = -heapq.heappop(stones)
        #     small = -heapq.heappop(stones)
        #     diff = large - small
        #     if diff > 0:
        #         heapq.heappush(stones, -diff)
        # return -stones[0] if stones else 0
        
        # stones = [-x for x in stones]
        # heapq.heapify(stones) # O(n)
        # while len(stones) > 1:
        #     large = -heapq.heappop(stones) # O(logN)
        #     small = -heapq.heappop(stones)
        #     diff = large - small
        #     if diff > 0:
        #         heapq.heappush(stones, -diff)
        # return -stones[0] if stones else 0