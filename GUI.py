import tkinter as tk
from tkinter import ttk

root = tk.Tk()
title = root.title("Calculator")

# WINDOW ATTRIBUTE
root.resizable(False, False)
window_width = 500
window_height = 500
root.iconbitmap('./asset/calculator.ico')

# FRAME
ttk.Label(root, text = 'this is a label placed in root.').pack()
frame = tk.Frame(root)
leftFrame = tk.Frame(root)
leftFrame.pack(side='left')
rightFrame = tk.Frame(root)
rightFrame.pack(side='right')

# LABEL
label1 = ttk.Label(leftFrame, text = 'this is a label placed in left frame.').pack()
label2 = ttk.Label(rightFrame, text = 'this is a label placed in right frame.').pack()

# CHECK FOR EVENT
def button_clicked():
    print(True)

# BUTTON
bt1 = ttk.Button(root, text = "HELLO WORLD", command = button_clicked)
bt1.pack()

# CENTER WINDOW
screenX = root.winfo_screenwidth()
screenY = root.winfo_screenheight()
centerX = int(screenX/2 - window_width/2)
centerY = int(screenY/2 - window_height/2)

# SET WINDOWS WIDTH AND HEIGHT
root.geometry(f'{window_width}x{window_height}+{centerX}+{centerY}')

root.mainloop()