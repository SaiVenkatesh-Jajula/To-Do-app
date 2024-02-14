def reading():
    """TO GET THE CONTENT IN A FILE"""
    with open("todo.txt", 'r') as file:
        content = file.readlines()
    return content


def writing(newlist, filename="todo.txt"):
    """TO WRITE CONTENT IN A FILE"""
    with open(filename, 'w') as file:
        file.writelines(newlist)


def appending(item):
    with open("todo.txt", 'a') as file:
        file.writelines(item + '\n')

if __name__=="__main__":
    print("This is Backend")
    print("Checking ToDos List: \n", reading())
