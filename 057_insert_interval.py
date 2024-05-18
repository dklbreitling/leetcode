class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def merge(a, b):
            return [min(a[START], b[START]), max(a[END], b[END])]

        def comes_before(a, b):
            return a[END] < b[START]

        new = []
        START = 0
        END = 1

        for index, interval in enumerate(intervals):
            if comes_before(interval, newInterval):
                new.append(interval)
            elif comes_before(newInterval, interval):
                new.append(newInterval)
                return new + intervals[index:]
            else:
                newInterval = merge(interval, newInterval)

        return new + [newInterval]
 
