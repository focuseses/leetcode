# O(n^2)
class Solution:
    def merge(self, intervals):
        ranges = []
        intervals.sort()
        low = intervals[0][0]
        high = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] <= high and intervals[i][1] > high:
                high = intervals[i][1]
            if intervals[i][0] > high:
                ranges.append([low, high])
                low = intervals[i][0]
                high = intervals[i][1]
        ranges.append([low, high])
        return ranges

        