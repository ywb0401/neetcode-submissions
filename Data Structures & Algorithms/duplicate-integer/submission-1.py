class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for i, j in freq.items():
            if j != 1:
                return True
        return False