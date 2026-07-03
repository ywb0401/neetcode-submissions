class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
                # return [i]
            hashmap[target - nums[i]] = i
            print(hashmap)