import tkinter
import tkinter.ttk


# theme selection
def theme():
    rb1.config(text="Dark")
    rb2.config(text="Light")
    rb1.pack(side=tkinter.RIGHT, padx=10, pady=10)
    rb2.pack(side=tkinter.RIGHT, padx=10, pady=10)


# list view
def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        if data == "theme":
            theme()


# main window
setting = tkinter.Tk()
listbox = tkinter.Listbox(setting)
listbox.insert(1, "theme")
listbox.insert(2, "font")

# variables
_theme = tkinter.StringVar()

# radio buttons
rb1 = tkinter.Radiobutton(setting, variable=_theme, value="dark")
rb2 = tkinter.Radiobutton(setting, variable=_theme, value="light")

# packing
listbox.pack(side=tkinter.LEFT, fill="x")
listbox.bind("<<ListboxSelect>>", callback)
setting.mainloop()
