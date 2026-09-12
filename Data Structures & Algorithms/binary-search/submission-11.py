class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = (l + r)//2

        while l < r:
            print(mid)
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid
            mid = (l + r)//2
            print(mid)
        return -1
            

            
