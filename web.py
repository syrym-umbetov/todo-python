import streamlit as st

FILEPATH = "/todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH, ):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo in todos:
        return
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Input", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
