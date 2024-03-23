import tkinter as tk 
from tkinter import ttk

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
      super().__init__(master =parent)
      self.rowconfigure(0, weight = 1)
      self.columnconfigure((0,1,2 ), weight = 1,uniform='a')
      ttk.Label(self,text=label_text).grid(row=0,column=0)
      ttk.Button(self,text = button_text).grid(row=0,column=1)
      self.pack(expand = True, fill ='both')
window =tk.Tk()
window.title('widget and return')
window.geometry('400x600')

Segment(window,'label','button')
Segment(window,'test','click')
Segment(window,'hello','test')

window.mainloop()

# class App(tk.Tk):
# class Menu(ttk.Frame):
# class Main(ttk.Frame):
#     def __init__ (self,parent):
#         self.place(relx=0.3,y=0,relwidth=0.7,relheight=1)
#         Entry(self,'Entry1,'Button 1','green')
#         Entry(self,'Entry2,'Button 2','blue')
# class Entry(ttk.Frame):
    
# app('Class based app',(600,600))