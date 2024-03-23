#https://youtu.be/DIjnbbRt5Pk?list=PLpMixYKO4EXeaGnqT_YWx7_mA77bz2VqM
import tkinter as tk 
from tkinter import ttk
def func():
    entry_text = entry.get()
    label['text']=entry_text
def func1():
    label['text']='josephine lawyer'
    entry['state']='enabled'
    
    
    # print(label.configure())#whenu run the funct u will see all options in terminal
#print the content of the entry 
    # print(entry.get())
#update the label use configure better then config
    # label.configure(text='go premium')
#same as label.configure
    # label.configure(text='go premium')

window = tk.Tk()
window.title('getting and setting widget')
window.geometry('200x300')

label = ttk.Label(master=window,text='some text')
label.pack()

entry= ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window,text='the button',command=func)
button.pack()

exercise_button = ttk.Button(master=window,text='exercise',command=func1)
exercise_button.pack()
window.mainloop()