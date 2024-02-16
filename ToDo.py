import PySimpleGUI as sg
import backend
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

sg.theme("Black")
timelabel=sg.Text(key="clock")
label = sg.Text("Enter your Task :")
inputbox = sg.InputText(tooltip="Enter ToDo", key="inputboxvalue")
add = sg.Button("Add")
listbox = sg.Listbox(values=backend.reading(), key='listboxvalue', enable_events=True, size=[45, 12])
edit = sg.Button("Edit")
complete = sg.Button("complete")
exit = sg.Button("Exit")

window = sg.Window(title='ToDos List',
                   layout=[[timelabel],
                       [label, inputbox, add],
                       [listbox, edit, complete],
                       [exit]
                   ],
                   font=("Aerial", 15))

while 1:
    event, item = window.read(timeout=300)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            backend.appending(item['inputboxvalue'])
            latestlist = backend.reading()
            window['listboxvalue'].update(values=latestlist)
            window["inputboxvalue"].update("")

        case "Edit":
            try:
                editlist=backend.reading()
                index=editlist.index(item["listboxvalue"][0])
                editlist[index]=item['inputboxvalue']+'\n'
                backend.writing(editlist)
                window["listboxvalue"].update(values=editlist)
            except IndexError:
                sg.popup("Please select item to edit", font=("Aerial", 10))

        case "complete":
            try:
                oldlist=backend.reading()
                oldlist.remove(item["listboxvalue"][0])
                backend.writing(oldlist)
                window["listboxvalue"].update(values=oldlist)
                window["inputboxvalue"].update("")
            except IndexError:
                sg.popup("Please select atleast an item to mention as completed", font=('Aerial', 15))

        case "listboxvalue":
            window["inputboxvalue"].update(value=item["listboxvalue"][0])

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
