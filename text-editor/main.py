import tkinter
import tkinter.filedialog
import menubar
import sidebar
from menubaroptions import contents
import hierarchical

# creating the main window
win = tkinter.Tk("Bhola editor")

# setting the max size
# win.maxsize(win.winfo_screenheight(), win.winfo_screenwidth())

# setting the min size
win.minsize(500, 500)

# specifying the title
win.title("Bhola editor")

# declaring an icon
icon = tkinter.PhotoImage(file="Imgs/main_ico.png")
sidebar.show()
# setting the icon img as the icon
win.iconphoto(True, icon)
# adding the menu
menubar.menu(win)

# adding the main writing space
text = tkinter.Text(win)
text.pack(expand=True, side=tkinter.TOP, fill=tkinter.BOTH)
text.focus_set()  # sets the cursor at the writing space


# saving logic
def save_as(event):
    global text
    t = text.get("1.0", "end-1c")
    save_location = tkinter.filedialog.asksaveasfile()
    try:
        file1 = open(save_location, "w+")
        file1.write(t)
        file1.close()
    except TypeError:
        pass


def _open_file(event):
    global file
    file = tkinter.filedialog.askopenfilename()
    if file == "":
        file = None
    else:
        text.delete(1.0, tkinter.END)
        with open(file, "r+") as f:
            text.insert(1.0, f.read())


def _open_folder(event):
    hierarchical.run()


text.insert(tkinter.INSERT, contents)

Scroll = tkinter.Scrollbar(text)
Scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
Scroll.config(command=text.yview)
text.config(yscrollcommand=Scroll.set)


# adding keybindings
win.bind("<Control-s>", save_as)
win.bind("<Control-o>", _open_file)
win.bind("<Control-Shift-O>", _open_folder)


# the main thing
win.mainloop()
