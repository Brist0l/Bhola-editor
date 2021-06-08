import tkinter
import tkinter.filedialog
import menubar
import sidebar

win = tkinter.Tk("Bhola editor")

# specifying the title
win.title("Bhola editor")

# declaring an icon
icon = tkinter.PhotoImage(file="Imgs/main_ico.png")
sidebar.run(win=win)
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


# adding keybindings
win.bind("<Control-s>", save_as)

# the main thing
win.mainloop()
