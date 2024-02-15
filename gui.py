import PySimpleGUI as sg
import backend

label = sg.Text("Enter your Task :")
inputbox = sg.InputText(tooltip="Enter ToDo", key="inputboxvalue")
add = sg.Button("Add")
listbox = sg.Listbox(values=backend.reading(), key='listboxvalue',
                     enable_events=True, size=[45, 12])
edit = sg.Button("Edit")
window = sg.Window(title='ToDos List',
                   layout=[[label, inputbox, add], [listbox, edit]],
                   font=("Aerial", 15))

while 1:
    event, item=window.read()
    # print(event)
    # print(item)
    match event:
        case "Add":
            backend.appending(item['inputboxvalue'])
            latestlist=backend.reading()
            window['listboxvalue'].update(values=latestlist)
        case "Edit":
            print("Now clicked edit button")
            editlist=backend.reading()
            index=editlist.index(item["listboxvalue"][0])
            editlist[index]=item['inputboxvalue']+'\n'
            backend.writing(editlist)
            window["listboxvalue"].update(values=editlist)
        case "listboxvalue":
            window["inputboxvalue"].update(value=item["listboxvalue"][0])
        case sg.WIN_CLOSED:
            break

window.close()
