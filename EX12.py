import tkinter as tk

win=tk.Tk()
PASS='12345'
USER='admin'

def authentication():
    if PASS==b and USER==a:
        btn1.config(background ='green') 
    else:   
        btn1.config(background ='red') 



lb1=tk.Label(win,text='User')
en1=tk.Entry(win)


lb2=tk.Label(win,text='Password')
en2=tk.Entry(win)


btn1=tk.Button(win,text='Click here',command = authentication)

lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
btn1.pack()

win.mainloop()
