# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '({}, {})'.format(self.start, self.end)

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        for index in range(0, len(intervals)):
            if intervals[index].start > newInterval.start:
                intervals.insert(index, newInterval)
                break
        else:
            intervals.append(newInterval)

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
        
intervals = [Interval(i, j) for i, j in [[1,3],[6,9]]]
print(x.insert(intervals, Interval(2, 5)))

intervals = [Interval(i, j) for i, j in [[1,2],[3,5],[6,7],[8,10],[12,16]]]
print(x.insert(intervals, Interval(4, 8)))

intervals = [Interval(i, j) for i, j in [[1, 5]]]
print(x.insert(intervals, Interval(2, 3)))