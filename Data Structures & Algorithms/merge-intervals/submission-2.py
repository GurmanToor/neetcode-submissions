class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        res.append(intervals.pop(0))

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                if interval[1] >= res[-1][1]:
                    res[-1][1] = interval[1]
            else:
                res.append(interval)
        return res
