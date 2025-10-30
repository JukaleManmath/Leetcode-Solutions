class ExamTracker:

    def __init__(self):
        self.times= []
        self.ps = []

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        if not self.ps:
            self.ps.append(score)
        else:  
            self.ps.append(score + self.ps[-1])

    def totalScore(self, startTime: int, endTime: int) -> int:
        s = bisect_left(self.times, startTime)
        e = bisect_right(self.times, endTime) - 1
        if s > e:
            return 0
        return self.ps[e] - self.ps[s-1] if s > 0 else self.ps[e]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)