def todo():
    task_list = []

    def inner(fn, **kwargs):
        return fn(task_list, **kwargs)

    return inner


def filter_active_tasks(task_list):
    new_task_list = []

    for task_instance_ in task_list:
        if not task_instance_['is_done']:
            new_task_list.append(task_instance_)
    print('Your active tasks: ')
    return new_task_list


def filter_completed_tasks(task_list):
    done_task_list = []

    for task_instance_ in task_list:
        if task_instance_['is_done']:
            done_task_list.append(task_instance_)
    print('Your have completed these tasks: ')
    return done_task_list


def get_task(task_list, task_name):
    task = None

    for task_instance_ in task_list:
        if task_instance_['name'] == task_name:
            task = task_instance_
            break

    return task


def add_task(task_list, task):
    task_list.append(task)
    return task_list


def delete_task(task_list, task_name):
    task = get_task(task_list, task_name)

    if task is None:
        raise ValueError(f'The task {task_name} does not exist.')

    task_list.remove(task)

    return task_list


def toggle_task_done(task_list, task_name):
    task = get_task(task_list, task_name)

    if task is None:
        raise ValueError(f'The task {task_name} does not exist.')

    task['is_done'] = True if not task['is_done'] else False

    return task_list


def mark_all_as_done(task_list):
    for task_instance_ in task_list:
        task_instance_['is_done'] = True

    return task_list


task_instance = todo()

print(task_instance(add_task, task={'name': 'write paper', 'is_done': False}))
print(task_instance(add_task, task={'name': 'prepare lecture', 'is_done': False}))
print(task_instance(add_task, task={'name': 'examination pending', 'is_done': False}))
print(task_instance(add_task, task={'name': 'get some rest', 'is_done': True}))

print(task_instance(delete_task, task_name='examination pending'))

print(task_instance(toggle_task_done, task_name='get some rest'))
print(task_instance(toggle_task_done, task_name='get some rest'))

print(task_instance(filter_active_tasks))
print(task_instance(filter_completed_tasks))
# print(task_instance(mark_all_as_done))
