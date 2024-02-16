import streamlit as st
import backend

def goappend():
    newitem = st.session_state['add']
    backend.appending(newitem)
    st.session_state['add']=""

st.title("Todo App")
st.subheader("The list of tasks:")


tasks = backend.reading()
for index, item in enumerate(tasks):
     checkbox = st.checkbox(item, key=item)
     if checkbox:
          tasks.pop(index)
          backend.writing(tasks)
          del st.session_state[item]
          st.rerun()


st.text_input(label="", placeholder="Add a new Todo...",
              on_change=goappend,key="add")

