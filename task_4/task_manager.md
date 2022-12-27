# Task manager

+ [Task Subtask ComplexTask Status](#task-subtask-complextask-status)
+ [TaskManager](#taskmanager)
+ [Unit tests](#unit-tests)


## Task Subtask ComplexTask Status
```python
class Task:

    def __init__(self, id, name, description, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
```
```python
import Task


class Subtask(Task):
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.__parent_id = parent_id  # have complex task id

    def get_parent_id(self):
        return self.__parent_id
```
```python
import Task


class ComplexTask(Task):
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.__subtasks_ids = subtasks_ids  # contains list of subtasks

    def get_subtasks_ids(self):
        return self.__subtasks_ids

    def add_subtask_id(self, new_subtask_id):
        self.__subtasks_ids.append(new_subtask_id)

    def remove_subtask_id(self, subtask_id):
        self.__subtasks_ids.remove(subtask_id)
        return len(self.__subtasks_ids) == 0
```
```python
from enum import Enum


class Status(Enum):
    NEW = 1
    ASSIGNED = 2
    COMPLETED = 3
```

## TaskManager
```python
import Task, Subtask, ComplexTask
import Status


class TaskManager:

    __id_series = 0

    def __init__(self):
        self.__tasks = dict()
        self.__subtasks = dict()
        self.__complex_tasks = dict()

    def __get_and_increment_id(self):
        next_id_value = TaskManager.__id_series
        TaskManager.__id_series += 1
        return next_id_value

    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description, Status.NEW)
        self.__tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, parent_id):
        current_id = self.__get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, Status.NEW, parent_id)
        self.__subtasks[current_id] = new_subtask

        complex_task = self.get_complex_task_by_id(parent_id)
        complex_task.add_subtask_id(new_subtask.get_id())

        return new_subtask

    def create_complex_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_complex_task = ComplexTask(current_id, name, description, Status.NEW, [])
        self.__complex_tasks[current_id] = new_complex_task
        return new_complex_task

    def get_tasks(self):
        return self.__tasks

    def get_subtasks(self):
        return self.__subtasks

    def get_complex_tasks(self):
        return self.__complex_tasks

    def get_tasks_by_id(self, id):
        return self.__tasks.get(id, None)

    def get_subtask_by_id(self, id):
        return self.__subtasks.get(id, None)

    def get_complex_task_by_id(self, id):
        return self.__complex_tasks.get(id, None)

    def remove_tasks(self):
        self.__tasks.clear()

    def remove_subtasks(self):
        self.__subtasks.clear()
        self.__complex_tasks.clear()

    def remove_complex_tasks(self):
        self.__complex_tasks.clear()
        self.__subtasks.clear()

    def remove_task_by_id(self, id):
        self.__tasks.pop(id)

    def remove_subtask_by_id(self, id):
        st = self.__subtasks.pop(id)
        parent_id = st.get_parent_id()
        ct = self.get_complex_task_by_id(parent_id)
        is_empty = ct.remove_subtask_id(id)

        if is_empty:
            self.__complex_tasks.pop(parent_id)

    def remove_complex_task_by_id(self, id):
        ct = self.__complex_tasks.pop(id)
        subtasks_ids = ct.get_subtasks_ids()

        for st_id in subtasks_ids:
            self.__subtasks.pop(st_id)

    def update_status(self, id, status):
        ans = self.get_tasks_by_id(id)
        if ans is not None:
            ans.set_status(status)
            return

        ans = self.get_subtask_by_id(id)
        if ans is not None:
            ans.set_status(status)
            return

        ans = self.get_complex_task_by_id(id)
        if ans is not None:
            ans.set_status(status)
```

## Unit tests
```python
import unittest
import TaskManager, Task, Subtask, ComplexTask
import Status


class TestTaskManager(unittest.TestCase):

    def setUp(self) -> None:
        self.__manager = TaskManager()

    def test_create_task(self):
        task = self.__manager.create_task('Task 1', 'Test task 1 created')

        self.assertEqual(len(self.__manager.get_tasks()), 1)
        self.assertEqual(self.__manager.get_tasks_by_id(task.get_id()).get_name(), 'Task 1')

    def test_create_subtask(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        parent_id = complex_task.get_id()
        subtask = self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', parent_id)

        self.assertEqual(subtask.get_name(), 'Subtask 1')
        self.assertEqual(subtask.get_parent_id(), parent_id)

    def test_create_complex_task(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')

        self.assertEqual(complex_task.get_subtasks_ids(), [])
        self.assertEqual(self.__manager.get_complex_task_by_id(complex_task.get_id()).get_status(), Status.NEW)

    def test_get_tasks(self):
        self.__manager.create_task('Task 1', 'Test task 1 created')

        tasks = self.__manager.get_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(type(tasks), dict)

    def test_get_subtasks(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task.get_id())

        subtasks = self.__manager.get_subtasks()

        self.assertEqual(len(subtasks), 1)
        self.assertEqual(type(subtasks), dict)

    def test_get_complex_tasks(self):
        self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')

        complex_tasks = self.__manager.get_complex_tasks()

        self.assertEqual(len(complex_tasks), 1)
        self.assertEqual(type(complex_tasks), dict)

    def test_get_task_by_id(self):
        task = self.__manager.create_task('Task 1', 'Test task 1 created')

        result = self.__manager.get_tasks_by_id(task.get_id())

        self.assertEqual(type(result), Task)
        self.assertEqual(result.get_name(), task.get_name())

    def test_get_subtask_by_id(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        subtask = self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task.get_id())

        result = self.__manager.get_subtask_by_id(subtask.get_id())

        self.assertEqual(type(result), Subtask)
        self.assertEqual(result.get_name(), subtask.get_name())

    def test_get_complex_tasks_by_id(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')

        result = self.__manager.get_complex_task_by_id(complex_task.get_id())

        self.assertEqual(type(result), ComplexTask)
        self.assertEqual(result.get_name(), complex_task.get_name())

    def test_remove_tasks(self):
        self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        self.__manager.remove_tasks()

        result = self.__manager.get_tasks()

        self.assertEqual(len(result), 0)

    def test_remove_subtasks(self):
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task.get_id())

        self.__manager.remove_subtasks()
        result = self.__manager.get_subtasks()

        self.assertEqual(len(result), 0)

    def test_remove_complex_tasks(self):
        self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        self.__manager.remove_complex_tasks()

        result = self.__manager.get_complex_tasks()

        self.assertEqual(len(result), 0)

    def test_remove_task_by_id(self):
        task = self.__manager.create_task('Task 1', 'Test task 1 created')
        self.__manager.remove_task_by_id(task.get_id())
        result = self.__manager.get_tasks_by_id(task.get_id())

        self.assertEqual(result, None)

    def test_remove_subtask_by_id(self):
        complex_task_1 = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        complex_task_2 = self.__manager.create_complex_task('Complex task 2', 'Complex task 2 created')
        subtask_1 = self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task_1.get_id())
        subtask_2 = self.__manager.create_subtask('Subtask 2', 'Subtask 2 created', complex_task_1.get_id())
        subtask_3 = self.__manager.create_subtask('Subtask 3', 'Subtask 3 created', complex_task_2.get_id())

        self.__manager.remove_subtask_by_id(subtask_1.get_id())
        self.__manager.remove_subtask_by_id(subtask_3.get_id())

        result_1 = self.__manager.get_subtask_by_id(subtask_1.get_id())
        result_2 = self.__manager.get_complex_task_by_id(complex_task_1.get_id())
        result_3 = self.__manager.get_complex_task_by_id(complex_task_2.get_id())

        self.assertEqual(result_1, None)
        self.assertEqual(type(result_2), ComplexTask)
        self.assertEqual(result_3, None)

    def test_remove_complex_task_by_id(self):
        complex_task_1 = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        complex_task_2 = self.__manager.create_complex_task('Complex task 2', 'Complex task 2 created')
        subtask_1 = self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task_1.get_id())
        subtask_2 = self.__manager.create_subtask('Subtask 2', 'Subtask 2 created', complex_task_1.get_id())
        subtask_3 = self.__manager.create_subtask('Subtask 3', 'Subtask 3 created', complex_task_2.get_id())

        self.__manager.remove_complex_task_by_id(complex_task_1.get_id())

        result_1 = self.__manager.get_complex_task_by_id(complex_task_1.get_id())
        result_2 = self.__manager.get_subtask_by_id(subtask_1.get_id())
        result_3 = self.__manager.get_subtask_by_id(subtask_3.get_id())

        self.assertEqual(result_1, None)
        self.assertEqual(result_2, None)
        self.assertEqual(type(result_3), Subtask)

    def test_update_status(self):
        task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        complex_task = self.__manager.create_complex_task('Complex task 1', 'Complex task 1 created')
        subtask = self.__manager.create_subtask('Subtask 1', 'Subtask 1 created', complex_task.get_id())

        self.__manager.update_status(subtask.get_id(), Status.ASSIGNED)
        self.__manager.update_status(complex_task.get_id(), Status.COMPLETED)
        self.__manager.update_status(task.get_id(), Status.ASSIGNED)

        self.assertEqual(subtask.get_status(), Status.ASSIGNED)
        self.assertEqual(complex_task.get_status(), Status.COMPLETED)
        self.assertEqual(task.get_status(), Status.ASSIGNED)


if __name__ == '__main__':
    unittest.main()

```
