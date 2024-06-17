import tkinter as tk
from tkinter import filedialog, messagebox

import main


def select_config_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            config = main.load_config(file_path)
            main.execute_task(config)
            messagebox.showinfo("Success", "Task executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Setting up the GUI
root = tk.Tk()
root.title("Task Automation")

btn_select_file = tk.Button(root, text="Select Configuration File", command=select_config_file)
btn_select_file.pack(pady=20)

root.mainloop()
