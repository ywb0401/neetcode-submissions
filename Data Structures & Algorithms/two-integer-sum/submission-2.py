class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = defaultdict(int)
        for idx, num in enumerate(nums):
            # print(idx, num)
            # print(h)
            if num in h:
                # print("y", h[num], target-num)
                return [h[num], idx]
            h[target-num] = idx