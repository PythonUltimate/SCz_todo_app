def todo():
    task_list = []

    def inner(fn, task):
        return fn(task_list, task)

    return inner


def add_task(task_list, task):
    task_list.append(task)
    return task_list


task_instance = todo()

print(task_instance(add_task, 'write paper'))
print(task_instance(add_task, 'prepare lecture'))
print(task_instance(add_task, 'examination pending'))
