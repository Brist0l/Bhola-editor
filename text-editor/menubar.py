import tkinter


def menu(win):
    menu_ = tkinter.Menu(win)

    def file():
        file_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="File", menu=file_)
        file_.add_command(label='New File', command=None)
        file_.add_command(label='Open...', command=None)
        file_.add_command(label='Save', command=None)
        file_.add_separator()
        file_.add_command(label='Exit', command=win.destroy)

    def edit():
        edit = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Cut', command=None)
        edit.add_command(label='Copy', command=None)
        edit.add_command(label='Paste', command=None)
        edit.add_command(label='Select All', command=None)
        edit.add_separator()
        edit.add_command(label='Find...', command=None)
        edit.add_command(label='Find again', command=None)

    def _help():
        help_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Help', menu=help_)
        help_.add_command(label='Tk Help', command=None)
        help_.add_command(label='Demo', command=None)
        help_.add_separator()
        help_.add_command(label='About Tk', command=None)

    file()
    edit()
    _help()
    win.config(menu=menu_)
