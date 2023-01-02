import subprocess
import tkinter as tk
from tkinter import Frame, Button, Text, filedialog
import os

def check_login(username, password):
    with open("users.txt", "r") as f:
        for line in f:
            user, pwd = line.strip().split(":")
            if user == username and pwd == password:
                return True
    return False

class LoginPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login)
        
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_login(username, password):
            self.parent.switch_frame(ServerPanel)
        else:
            # Display error message
            pass

class ServerPanel(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        self.server_log = Text(self)
        self.server_log.pack()
        self.start_button = tk.Button(self, text="Start Server", command=self.start_server)
        self.stop_button = tk.Button(self, text="Stop Server", command=self.stop_server)
        self.restart_button = tk.Button(self, text="Restart Server", command=self.restart_server)
        self.select_jar_button = tk.Button(self, text="Select Server JAR", command=self.select_jar)
        self.download_plugins = tk.Button(self, text="Plugin Downloader", command=self.select_jar)
        
        self.start_button.pack()
        self.stop_button.pack()
        self.restart_button.pack()
        self.select_jar_button.pack()
        self.download_plugins.pack()
    
    def start_server(self):
        self.server_process = subprocess.Popen(["java", "-jar", self.server_jar, "nogui"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.update_log()

    def download_plugins(self):
      os.system("python3 download.py")

    
    def stop_server(self):
        self.server_process.terminate()

    def restart_server(self):
        self.stop_server()
        self.start_server()
    
    def select_jar(self):
        self.server_jar = filedialog.askopenfilename()
    
    def update_log(self):
        log = subprocess.run(["tail", "-n", "10", self.server_jar], stdout=subprocess.PIPE).stdout.decode("latin-1")
        self.server_log.insert("end", log)
        self.server_log.after(1000, self.update_log)

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = None
        self.switch_frame(LoginPage)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
