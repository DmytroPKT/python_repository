tasks = []
note = """Welcome to the Task manager.
Select one of the list's command and type it in the console:
1. 'add' - add new tasks,
    1.1. 'end' - finish with tasks addition;
2. 'list' - display tasks list;
3. 'del' - delete a specific task;
4. 'help' - commands list call;
5. 'exit' - stop Task manager.  """
print(note)
while True:
    user_choice = input('Enter your choice: ')

    if user_choice == 'add':
        while True:
            new_task = input('Enter new tasks:  ')
            if new_task == 'end':
                break
            else:
                tasks.append(new_task)

    elif user_choice == 'list':
        for x, task in enumerate(tasks):
            print(x, task)
            x += 1

    elif user_choice == 'help':
        print(note)

    elif user_choice == 'del':
        del_tsk = int(input('Enter task No.: '))
        print('Task ' + tasks[del_tsk] + ' removed')
        del tasks[del_tsk]

    elif user_choice == 'exit':
        exit('Bye bye')
