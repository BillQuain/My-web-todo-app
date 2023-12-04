import streamlit as st
import functions


def add_todo():
    user_input = st.session_state["new_todo"] + '\n'
    todos.append(user_input)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("To-Do App")
st.subheader("this is my to-do app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

