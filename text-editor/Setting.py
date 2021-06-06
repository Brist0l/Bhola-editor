import tkinter
import tkinter.ttk


# theme selection
def theme():
    rb1.config(text="Dark")
    rb2.config(text="Light")
    rb1.pack(side=tkinter.RIGHT, padx=10, pady=10)
    rb2.pack(side=tkinter.RIGHT, padx=10, pady=10)


def font():
    rb3.config(text="Comic Sans MS")
    rb4.config(text="System")
    rb5.config(text="Modern")
    rb6.config(text="Courier")
    rb7.config(text="MS Serif")
    rb3.pack(side=tkinter.TOP, anchor="w")
    rb4.pack(side=tkinter.TOP, anchor="w")
    rb5.pack(side=tkinter.TOP, anchor="w")
    rb6.pack(side=tkinter.TOP, anchor="w")
    rb7.pack(side=tkinter.TOP, anchor="w")


# list view
def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        if data == "theme":
            theme()
        elif data == "font":
            font()


# main window
setting = tkinter.Tk()
listbox = tkinter.Listbox(setting)
listbox.insert(1, "theme")
listbox.insert(2, "font")

# variables
_theme = tkinter.StringVar()
_font = tkinter.StringVar()

# theme values
rb1 = tkinter.Radiobutton(setting, variable=_theme, value="dark")
rb2 = tkinter.Radiobutton(setting, variable=_theme, value="light")

# font values
rb3 = tkinter.Radiobutton(setting, variable=_font, value="Comic Sans MS")
rb4 = tkinter.Radiobutton(setting, variable=_font, value="System")
rb5 = tkinter.Radiobutton(setting, variable=_font, value="Modern")
rb6 = tkinter.Radiobutton(setting, variable=_font, value="Courier")
rb7 = tkinter.Radiobutton(setting, variable=_font, value="MS Serif")

# packing
listbox.pack(side=tkinter.LEFT, fill="x")
listbox.bind("<<ListboxSelect>>", callback)
setting.mainloop()
