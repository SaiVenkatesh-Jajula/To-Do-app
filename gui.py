import PySimpleGUI as sg
import backend

label = sg.Text("Enter your Task :")
inputbox = sg.InputText(tooltip="Enter ToDo",key="value")
add = sg.Button("Add")
window = sg.Window(title='ToDos List',
                   layout=[[label, inputbox], [add], []],
                   font=("Aerial", 20))
# this line is like "dsfa" some value for class str for sg window.
#layout is like widgets
while 1:
    event, item=window.read() # when we add item - window read got an event it consists data!("Add",{'key':'input'})
    match event:
        case "Add":
            backend.appending(item['value'])
        case sg.WIN_CLOSED: #when we close X button in GUI it should break the loop.!
            break

window.close()
