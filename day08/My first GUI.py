##My first GUI

import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("My first GUI")
label= tk.Label(root, text="Hello World", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20)

#This is used for a single line of text
myentry = tk.Entry(root, font=("Arial", 16))
myentry.pack(padx=20, pady=20)

#Botton
#firstbutton = tk.Button(root, text="Click me!", font= ("Arial", 16))
#firstbutton.pack(padx=10)

bottonframe= tk.Frame(root)
bottonframe.columnconfigure(0, weight=1)
bottonframe.columnconfigure(1, weight=1)
bottonframe.columnconfigure(2, weight=1)
#bottonframe.columnconfigure(3, weight=1)

btn1= tk.Button(bottonframe, text="1")
btn1.grid(row=0, column=0, sticky="nsew")

btn2= tk.Button(bottonframe, text="2")
btn2.grid(row=0, column=1, sticky="nsew")

btn3= tk.Button(bottonframe, text="3")
btn3.grid(row=0, column=2, sticky="nsew")

btn4= tk.Button(bottonframe, text="4")
btn4.grid(row=1, column=0, sticky="nsew")

btn5= tk.Button(bottonframe, text="5")
btn5.grid(row=1, column=1, sticky="nsew")

btn6= tk.Button(bottonframe, text="6")
btn6.grid(row=1, column=2, sticky="nsew")

btn7= tk.Button(bottonframe, text="7")
btn7.grid(row=2, column=0, sticky="nsew")

btn8= tk.Button(bottonframe, text="8")
btn8.grid(row=2, column=1, sticky="nsew")

btn9= tk.Button(bottonframe, text="9")
btn9.grid(row=2, column=2, sticky="nsew")

btn0= tk.Button(bottonframe, text="C")
btn0.grid(row=3, column=0, sticky="nsew")

btn0= tk.Button(bottonframe, text="0")
btn0.grid(row=3, column=1, sticky="nsew")

btnEnter = tk.Button(bottonframe, text="Enter")
btnEnter.grid(row=3, column=2, sticky="nsew")

bottonframe.pack(fill="x")


root.mainloop()

