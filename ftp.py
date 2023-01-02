import os
import tkinter as tk
from tkinter import Listbox

class DirectoryViewer(tk.Tk):
    def __init__(self, directory, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.directory = directory
        self.create_widgets()
    
    def create_widgets(self):
        self.listbox = Listbox(self)
        self.listbox.pack()
        
        for item in os.listdir(self.directory):
            self.listbox.insert("end", item)

app = DirectoryViewer("/")
app.mainloop()
