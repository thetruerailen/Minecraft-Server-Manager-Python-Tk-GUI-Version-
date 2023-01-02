import tkinter as tk
from tkinter import Frame, Button, Text, filedialog
import requests
import os

class DownloadPluginWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        self.plugin_url_label = tk.Label(self, text="Enter plugin download URL:")
        self.plugin_url_entry = tk.Entry(self)
        self.download_button = tk.Button(self, text="Download Plugin", command=self.download_plugin)
        
        self.plugin_url_label.pack()
        self.plugin_url_entry.pack()
        self.download_button.pack()
    
    def download_plugin(self):
        plugin_url = self.plugin_url_entry.get()
        # Check if plugins folder exists, create it if it doesn't
        if not os.path.exists("plugins"):
            os.makedirs("plugins")
        # Download plugin
        plugin_file = requests.get(plugin_url)
        # Save plugin to plugins folder
        open(f"plugins/{plugin_url.split('/')[-1]}", "wb").write(plugin_file.content)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
