import tkinter
from tkinter import Button

from practical_tasks import button_cls

root = tkinter.Tk()
root.title("Simple game")
root.geometry("300x400")

label = tkinter.Label(root,text="Welcome!")
label.grid()
button = tkinter.Button(root, text="Start game")
button.grid()

buttons =[]
def on_button_click(button_id):
    text1 = buttons[button_id].cget('text')
    if text1 == 'O':
        buttons[button_id].config(text="X")
    elif text1 == 'X':
        buttons[button_id].config(text="O")
    else:
        buttons[button_id].config(text="X")
    print(text1)


button_id =0
for i in range(2,5):
    for j in range(0,3):
        button = tkinter.Button(root, text=" ", width=10, height=5, command=lambda id=button_id: on_button_click(id))
        button.grid(row=i, column=j)
        buttons.append(button)
        button_id += 1






root.mainloop()


