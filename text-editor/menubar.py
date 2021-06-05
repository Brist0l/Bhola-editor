import tkinter


def menu(win):
    menu_ = tkinter.Menu(win)
    file = tkinter.Menu(menu_, tearoff=0)
    menu_.add_cascade(label="File", menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=win.destroy)

    win.config(menu=menu_)
