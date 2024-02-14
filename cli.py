from backend import reading, writing, appending
import time
print(time.strftime("%d-%m-%Y : %H:%M:%S"))

while True:
    n = input("Enter 'add', 'show', 'edit', 'complete', exit' task : ").strip()

    if n.startswith("add"):
        entry = n[4:]
        appending(entry)

    elif n.startswith("show"):
        todos = reading()
        for index, item in enumerate(todos):
            newitem = item.strip('\n')
            print(f"{index + 1}-{newitem}")

    elif n.startswith("edit"):
        try:
            n = int(n[5:])
            todos = reading()
            todos[n - 1] = input("Enter new ToDo:") + '\n'
            writing(todos)
        except ValueError:
            print("Please Check and Enter serial no. to edit the task!")
            continue

    elif n.startswith("complete"):
        try:
            value = int(n[9:])
            todos = reading()
            todos.pop(value - 1)
            writing(todos)
        except (IndexError, ValueError):
            print("Enter valid serial number to delete the task in the list!")
            continue

    elif n.startswith("exit"):
        break

    else:
        print("Enter valid key")

print("The End")
