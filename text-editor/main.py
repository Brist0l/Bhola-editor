import tkinter
import tkinter.filedialog
import menubar

win = tkinter.Tk("Bhola editor")
win.title("Bhola editor")
menubar.menu(win)
text = tkinter.Text(win)
text.pack(expand=True, side=tkinter.TOP, fill=tkinter.BOTH)
text.focus_set()


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


win.bind("<Control-s>", save_as)

win.mainloop()
