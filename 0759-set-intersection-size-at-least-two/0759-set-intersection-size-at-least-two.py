class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1], -x[0]))
        arr = [intervals[0][1] -1, intervals[0][1]]
        for start, end in intervals[1:]:
            if arr[-2] < start <= arr[-1]:
                arr.append(end)
            elif start > arr[-1]:
                arr += [end - 1, end]
        return len(arr)