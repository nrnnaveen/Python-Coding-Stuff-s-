# 🧮 Mini Calculator App
# Developed using Python + Tkinter

from tkinter import *

# Create main window
root = Tk()
root.title("Mini Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for displaying expressions
expression = ""
input_text = StringVar()

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# UI Design
entry_frame = Frame(root, bg="black")
entry_frame.pack(fill=BOTH)

input_field = Entry(entry_frame, textvariable=input_text, font=('Arial', 20, 'bold'), bg="black", fg="white", bd=10, justify='right')
input_field.pack(fill=BOTH, ipadx=8, ipady=15)

button_frame = Frame(root)
button_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+')
]

for row in buttons:
    frame = Frame(button_frame)
    frame.pack(expand=True, fill='both')
    for char in row:
        if char == 'C':
            Button(frame, text=char, font=('Arial', 18), command=clear).pack(side=LEFT, expand=True, fill='both')
        else:
            Button(frame, text=char, font=('Arial', 18), command=lambda ch=char: press(ch)).pack(side=LEFT, expand=True, fill='both')

equal_button = Button(root, text='=', font=('Arial', 18), bg='lightgreen', command=equalpress)
equal_button.pack(expand=True, fill='both')

root.mainloop()
