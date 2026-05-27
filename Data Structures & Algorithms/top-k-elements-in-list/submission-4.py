class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        print(count)
        bucket = [[] for _ in range(len(nums)+1)]
        for i in range(len(count)):
            bucket[count[i][1]].append(count[i][0])
        print(bucket)
        res = []
        for j in range(len(nums), -1, -1):
            if bucket[j] != []:
                for num in bucket[j]:
                    res.append(num)
            if len(res) == k:
                return res

