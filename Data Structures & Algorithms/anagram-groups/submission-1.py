class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            c = sorted(s)
            # print(c)
            hashmap[str(c)].append(s)
        res = []
        for i, j in hashmap.items():
            res.append(j)
            print(i, j)
        # print(hashmap.get())
        return res