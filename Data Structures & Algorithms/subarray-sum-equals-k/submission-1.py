class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] += 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            compliment = curr_sum - k
            if compliment in prefix_map:
                count += prefix_map[compliment]
            prefix_map[curr_sum] += 1
        
        return count