class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for i, c in hashmap.items():
            bucket[c].append(i)
        res = []
        for j in range(len(bucket)-1, -1, -1):
            for num in bucket[j]:
                res.append(num)
            if len(res) >= k:
                return res