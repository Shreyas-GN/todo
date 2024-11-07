# Import necessary libraries
import streamlit as st

# Title of the app
st.title("📝 To-Do List")

# Initialize the session state to hold the to-do list if it doesn't exist
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task():
    if st.session_state.new_task != "":
        st.session_state.tasks.append(st.session_state.new_task)
        st.session_state.new_task = ""  # Clear the input after adding

# Input field for a new task
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# Display the to-do list with delete options
st.write("## Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    cols = st.columns([0.9, 0.1])
    cols[0].write(f"{i + 1}. {task}")
    if cols[1].button("❌", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()  # Refresh the app to update the list