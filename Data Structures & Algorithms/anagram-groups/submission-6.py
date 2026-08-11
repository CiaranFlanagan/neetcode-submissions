class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            sorted_strs[sorted_s].append(s)
        return list(sorted_strs.values())
        