class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = tuple(sorted(s))
            d[k].append(s)
        return d.values()
        