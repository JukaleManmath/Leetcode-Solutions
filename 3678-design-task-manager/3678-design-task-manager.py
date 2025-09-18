class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskinfo = {}
        self.heap = []

        for user, task, priority in tasks:
            self.taskinfo[task] = (user, priority)

            heapq.heappush(self.heap, (-priority, -task))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskinfo[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        user, _ = self.taskinfo[taskId]
        self.taskinfo[taskId] = (user, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.taskinfo[taskId]
        

    def execTop(self) -> int:
        while self.heap:
            negP, negtask = heapq.heappop(self.heap)
            if -negtask in self.taskinfo and self.taskinfo[-negtask][1] == -negP:
                user, _= self.taskinfo.pop(-negtask)
                return user
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()