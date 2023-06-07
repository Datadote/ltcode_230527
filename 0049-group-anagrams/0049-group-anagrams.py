class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] += 1
            d[tuple(count)].append(s)
        return d.values()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         index = ord(c) - ord('a')
        #         count[index] += 1
        #     d[tuple(count)].append(s)
        # return d.values()
        
        # # O(N*K), O(N*K)
        # d = defaultdict(list)
        # for s in strs:
        #     key = [0]*26
        #     for c in s:
        #         idx = ord(c) - ord('a')
        #         key[idx] += 1
        #     d[tuple(key)].append(s)
        # return d.values()
    
        # O(N * klogk) O(N*K)
        # d = defaultdict(list)
        # for s in strs:
        #     k = tuple(sorted(s))
        #     d[k].append(s)
        # return d.values()
    
    
    # d = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         # index = ord(c) - ord('a')
        #         # count[index] += 1
        #         count[ord(c) - ord('a')] += 1
        #     d[tuple(count)].append(s)
        # return d.values()
        
        # d = defaultdict(list)
        # for s in strs:
        #     k = tuple(sorted(s))
        #     d[k].append(s)
        # return d.values()