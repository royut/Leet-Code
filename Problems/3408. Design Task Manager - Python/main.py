import heapq


class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.tasksHeap = []
        self.taskPriority = {}
        self.taskUserId = {}
        for task in tasks:
            self.add(task[0], task[1], task[2])
        print(self.tasksHeap)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        heapq.heappush(self.tasksHeap, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskUserId[taskId] = userId

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        self.taskPriority[taskId] = newPriority
        heapq.heappush(self.tasksHeap, (-newPriority, -taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        self.taskPriority[taskId] = -1

    def execTop(self):
        """
        :rtype: int
        """
        while self.tasksHeap:
            negPriority, negTaskId = heapq.heappop(self.tasksHeap)
            priority = -negPriority
            taskId = -negTaskId
            if self.taskPriority.get(taskId, -2) == priority:
                self.taskPriority[taskId] = -1
                return self.taskUserId.get(taskId, -1)
        return -1


if __name__ == "__main__":
    # Your TaskManager object will be instantiated and called as such:
    tasks = [[1, 101, 10], [2, 102, 20], [3, 103, 15], [1, 100, 10]]
    obj = TaskManager(tasks)
    obj.add(4, 104, 5)
    obj.edit(102, 8)
    obj.rmv(101)
    param_4 = obj.execTop()
