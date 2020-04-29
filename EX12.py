import tkinter as tk

win=tk.Tk()

lb1=tk.Label(win,text='User')
en1=tk.Entry(win)
a=en1.get()

lb2=tk.Label(win,text='Password')
en2=tk.Entry(win)
b=en2.get()

btn1=tk.Button(win,text='Click here')

lb1.pack()
lb2.pack()
en1.pack()
en2.pack()
btn1.pack()
