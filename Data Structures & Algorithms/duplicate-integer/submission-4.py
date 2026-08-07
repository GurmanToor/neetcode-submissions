class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            num_set.add(num)
        return len(nums) != len(num_set)
        