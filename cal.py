import tkinter  as tk
from tkinter import messagebox,ttk

root = tk.Tk()
root.title("Calculator")

heading_label = tk.Label(root,font = ('arial',20,'bold'),text = "CALCULATOR",pady = 20,padx = 20)
heading_label.pack()


heading_label1 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter first number",pady = (20),padx = (20))
heading_label1.pack()

first_number = tk.Entry(root,font = ('arial',20,'bold'))
first_number.pack()

heading_label2 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter second number",pady = (20),padx = (20))
heading_label2.pack()

second_number = tk.Entry(root,font = ('arial',20,'bold'))
second_number.pack()

heading_label3 = tk.Label(root,font = ('arial',20,'bold'),text = "Operation",pady = 20,padx = 20)
heading_label3.pack()

button1 = tk.Button(root, font = ('arial',20,'bold'),bd =10,text = "Addition", command = lambda: addition())
button1.pack()

button2  = tk.Button(root ,font = ('arial',20,'bold'),bd = 10, text ="Subtraction",command = lambda: subtraction() )
button2.pack()

button3 = tk.Button(root ,font = ('arial',20,'bold'),bd =10, text ="Multiplication",command = lambda: multiplication() )
button3.pack()

button4  = tk.Button(root ,font = ('arial',20,'bold'),bd =10, text ="Division",command = lambda: division() )
button4.pack()

result_label = tk.Label(root,font = ('arial',20,'bold'),text = "Result is",pady=(20),padx=(20))
result_label.pack()

button5  = tk.Button(root ,font = ('arial',20,'bold'),bd =10, text ="Clear",command = lambda: clr() )
button5.pack()





def  addition() :

    first = int(first_number.get())
    second = int(second_number.get())
    result1 = first + second
    result_label.config(text = 'Result is   ' + str(result1))

def subtraction():

    first = int(first_number.get())
    second = int(second_number.get())
    result2 = first - second
    result_label.config(text='Result is ' + str(result2))

def multiplication():

    first = float(first_number.get())
    second = float(second_number.get())
    result3 = first * second
    result_label.config(text='Result is ' + str(result3))

def division():

    first = first_number.get()
    second = second_number.get()

    try:
        first =float(first)
        second = float(second)
        result4 = first/second
        result_label.config(text='Result is ' + str(result4))
    except ZeroDivisionError:
        messagebox.showerror(ZeroDivisionError,"Division by zero is not possible")

def clr():

    first_number.delete(first = 0,last = 20)
    second_number.delete(first = 0, last = 20)

root.mainloop()