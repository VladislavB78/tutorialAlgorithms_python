+ [Task Subtask ComplexTask Status](#task-subtask-complextask-status)
+ [Task manager](#task-manager)


## Task Subtask ComplexTask Status
```python
class Task:
    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
```
```python
import Task


class Subtask(Task):
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id  # have complex task id
```
```python
import Task


class ComplexTask(Task):
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks  # contains list of subtasks
```
```python
from enum import Enum


class Status(Enum):
    NEW = 1
    ASSIGNED = 2
    COMPLETED = 3
```

## Task manager
```python
import Task, Subtask, ComplexTask
import Status


class TaskManager:

    def __init__(self):
        self.tasks = dict()
        self.subtasks = dict()
        self.complex_tasks = dict()

    def create_task(self, task):
        self.tasks[task.id] = task

    def create_subtask(self, subtask):
        self.subtasks[subtask.id] = subtask

    def create_complex_task(self, complex_task):
        self.complex_tasks[complex_task.id] = complex_task

    def get_tasks(self):
        return self.tasks

    def get_subtasks(self):
        return self.subtasks

    def get_complex_tasks(self):
        return self.complex_tasks

    def get_tasks_by_id(self, id):
        return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        return [key for key, val in self.subtasks.items() if val.parent_id == id]

    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id)

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        self.subtasks.clear()
        self.complex_tasks.clear()

    def remove_complex_tasks(self):
        self.complex_tasks.clear()
        self.subtasks.clear()

    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        st = self.subtasks.pop(id)
        memo = []
        for key, val in self.complex_tasks.items():
            if st.parent_id == key and id in val.subtasks:
                val.subtasks.remove(id)
                if len(val.subtasks) == 0:
                    memo.append(key)
        for el in memo:
            self.remove_complex_task_by_id(el)

    def remove_complex_task_by_id(self, id):
        ct = self.complex_tasks.pop(id)
        memo = ct.subtasks

        for el in memo:
            self.remove_subtask_by_id(el)

    def update_status(self, task):
        self.tasks[task.id] = task
```

