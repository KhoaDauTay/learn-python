import tkinter as tk
 
app = tk.Tk() 
app.geometry('300x200')
app.title("Basic Status Bar")

statusbar = tk.Label(app, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)

statusbar.pack(side=tk.BOTTOM, fill=tk.X)
app.mainloop()