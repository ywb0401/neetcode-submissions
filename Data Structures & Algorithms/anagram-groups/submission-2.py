class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            c = sorted(s)
            hashmap[tuple(c)].append(s)
        res = []
        for i, j in hashmap.items():
            res.append(j)
        return res