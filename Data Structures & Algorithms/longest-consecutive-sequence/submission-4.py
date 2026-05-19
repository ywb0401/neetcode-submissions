class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                cur = 0
                while num in nums:
                    cur += 1
                    num += 1
                res = max(cur, res)

        return res
