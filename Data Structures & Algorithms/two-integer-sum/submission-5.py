class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_map.keys():
                return [nums_map[compliment], i]
            nums_map[num] = i