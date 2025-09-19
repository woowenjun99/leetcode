from sortedcontainers import SortedSet
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_id_to_priority: dict[int, int] = {}
        self.task_id_to_user_id: dict[int, int] = {}
        self.sorted_priority_task_id = SortedSet()
        for user_id, task_id, priority in tasks:
            self.task_id_to_user_id[task_id] = user_id
            self.task_id_to_priority[task_id] = priority
            self.sorted_priority_task_id.add((-priority, -task_id))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_id_to_user_id[taskId] = userId
        self.task_id_to_priority[taskId] = priority
        self.sorted_priority_task_id.add((-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        current_priority = self.task_id_to_priority[taskId]
        self.sorted_priority_task_id.remove((-current_priority, -taskId))
        self.task_id_to_priority[taskId] = newPriority
        self.sorted_priority_task_id.add((-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        current_priority = self.task_id_to_priority[taskId]
        self.sorted_priority_task_id.remove((-current_priority, -taskId))
        del self.task_id_to_priority[taskId]
        del self.task_id_to_user_id[taskId]

    def execTop(self) -> int:
        if not self.sorted_priority_task_id: return -1
        _, task_id = self.sorted_priority_task_id[0]
        user_id = self.task_id_to_user_id[-task_id]
        self.rmv(-task_id)
        return user_id