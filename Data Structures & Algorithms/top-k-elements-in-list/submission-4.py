class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq = defaultdict(list)
        for key, value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        