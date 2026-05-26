class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            c = Counter(s).items()
            c = list(c)
            c = sorted(c, key = lambda x: x[0])
            c = tuple(c)
            hashmap[c].append(s)
        return list(hashmap.values())
