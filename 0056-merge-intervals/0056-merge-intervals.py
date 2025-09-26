class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if not intervals:
        #     return [[]]
        # intervals.sort()
        # res = []
        # start, end = intervals[0]
        # for i in range(1, len(intervals)):
        #     if end < intervals[i][0]:
        #         res.append([start, end])
        #         start, end = intervals[i]
        #     else:
        #         if end >= intervals[i][0]:
        #             start = min(start, intervals[i][0])
        #             end = max(end , intervals[i][1])

        # res.append([start,end])
        # return res

        intervals.sort()
        res=[intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                start, end = res.pop()
                res.append([min(start, intervals[i][0]), max(end, intervals[i][1])])
        return res

        