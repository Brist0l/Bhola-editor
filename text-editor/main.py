import tkinter
import tkinter.filedialog
import menubar

win = tkinter.Tk("Bhola editor")
win.title("Bhola editor")
menubar.menu(win)
text = tkinter.Text(win)
text.grid()
text.focus_set()


def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = tkinter.filedialog.asksaveasfile()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()


button = tkinter.Button(win, text="Save",command=save_as)
button.grid()

win.mainloop()
