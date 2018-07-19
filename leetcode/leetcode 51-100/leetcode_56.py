# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '({}, {})'.format(self.start, self.end)

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        intervals.sort(key=lambda interval: (interval.start, -interval.end))
        start = intervals[0]
        for index in range(1, len(intervals)):
            current = intervals[index]
            if start.end >= current.start:
                start = Interval(start.start, max(current.end, start.end))
                intervals[index] = start
                intervals[index - 1] = None
            else:
                start = current

        return list(filter(bool, intervals))

x = Solution()
print(x.merge([Interval(i, j) for i, j in [[1,3],[2,6],[8,10],[15,18]]]))
print(x.merge([Interval(i, j) for i, j in [[1,4],[1,5]]]))
        