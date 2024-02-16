import streamlit as st
import backend

def goappend():
    newitem = st.session_state['add']
    backend.appending(newitem)
    st.session_state['add']=""

# def godelete():
#     pass

st.title("Todo App")
st.subheader("The list of tasks:")


tasks = backend.reading()
for item in tasks:
    st.checkbox(item)

st.text_input(label="", placeholder="Add a new Todo...",
              on_change=goappend,key="add")
#st.session_state
print("The end")
