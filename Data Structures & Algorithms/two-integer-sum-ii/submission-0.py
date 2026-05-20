class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            print(l, r)
            print(numbers[l], numbers[r], target, numbers[l] + numbers[r] == target)
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
                # r -= 1
            else:
                # l += 1
                r -= 1
                
        return [0, 0]