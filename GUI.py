import tkinter as tk

root = tk.Tk()
root.title("GUI")

# WINDOW ATTRIBUTE
window_width = 500
window_height = 500
root.resizable(False, False)
screenX = root.winfo_screenwidth()
screenY = root.winfo_screenheight()
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.5)

# CENTER WINDOW
centerX = int(screenX/2 - window_width/2)
centerY = int(screenY/2 - window_height/2)

# SET WINDOWS WIDTH AND HEIGHT
root.geometry(f'{window_width}x{window_height}+{centerX}+{centerY}')

root.mainloop()