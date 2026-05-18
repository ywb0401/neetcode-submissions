class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        # print(count)
        for num, c in count.items():
            bucket[c].append(num)
        # print(burrel)
        res = []
        for j in range(len(nums), 0, -1):
            for n in bucket[j]:
                res.append(n)
                if len(res) == k:
                    return res