class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            count = tuple(sorted(Counter(s).items()))
            # print(count, count_sort, count_tuple)
            h[count].append(s)
        
        res = []
        for tp, word in h.items():
            res.append(word)
        
        return res

