import PySimpleGUI as sg

label = sg.Text("Enter your Task :")
inputbox = sg.InputText(tooltip="Enter ToDo")
add = sg.Button("Add")
window = sg.Window(title='ToDos List', layout=[[label, inputbox],[add]]) # this line is like "dsfa" some value for class str for sg window.
#layout is like widgets
window.read()

window.close()
