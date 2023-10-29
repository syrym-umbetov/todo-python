import PySimpleGUI as sg
from functions import get_todos, write_todos
import time


sg.theme("GreenMono")
clock = sg.Text(key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(tooltip='Add item', size=10,
                       image_source='add.png', key='Add')
list_box = sg.Listbox(values=get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10]
                      )
edit_button = sg.Button("Edit")
delete_button = sg.Button(key="Delete", image_source='complete.png')
close_button = sg.Button("Close")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, delete_button],
          ]

window = sg.Window(
    'My To-Do App',
    layout=layout,
    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == 'Add':
        todos = get_todos()
        todos.append(values['todo'] + '\n')
        write_todos(todos)
        window['todos'].update(values=todos)
    elif event == 'Edit':
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))
    elif event == 'Delete':
        try:
            todo_to_delete = values['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_delete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))
    elif event == sg.WIN_CLOSED:
        break
    # elif 'todos':
    #     window['todo'].update(value=values['todos'][0])
window.close()
