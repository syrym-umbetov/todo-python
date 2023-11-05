import time

from functions import get_todos, write_todos

now = time.strftime("%b %d, %Y %H:%M")

print(now)


while True:
    userAction = input('add, show (display), edit, complete or exit: ').strip()

    if userAction.startswith('add'):
        todo = userAction[4:]

        todos = get_todos('todos.txt')

        todos.append(todo + '\n')

        write_todos('todos.txt', todos)
    elif userAction.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif userAction.startswith('edit'):
        try:
            number = int(userAction[5:])

            todos = get_todos('todos.txt')

            todos[number - 1] = input('Enter a new todo: ') + '\n'

            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif userAction.startswith('complete'):
        try:
            number = userAction[9:]

            todos = get_todos('todos.txt')

            todos.pop(number - 1)

            write_todos('todos.txt', todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif userAction.startswith('exit'):
        break
    else:
        print('Unknown command')
print('Bye')
