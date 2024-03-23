#https://youtu.be/xYqWu7ZF4rk?list=PLpMixYKO4EXeaGnqT_YWx7_mA77bz2VqM
import tkinter as tk
import tkinter as ttk
def func():
    print('michel')
window = tk.Tk()
window.title('window and widget')
window.geometry('600x500')
tk.Text(window).place(x=10, y=30,width=250)
tk.Text(window).place(x=251, y=30,width=250)
tk.Text(window).place(x=10, y=300,width=500)
b1 = ttk.Button(window,text='press',command=func).pack()

window.mainloop()