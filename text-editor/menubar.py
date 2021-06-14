import tkinter
import menubaroptions
import Setting
import pip


def menu(win):
    menu_ = tkinter.Menu(win)

    def file():
        file_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="File", menu=file_)
        file_.add_command(label='New File', accelerator="Ctrl+N", compound=tkinter.LEFT, command=None)
        file_.add_command(label='Open', accelerator="Ctrl+O", command=menubaroptions._open)
        file_.add_command(label='Setting', accelerator="Ctrl+Alt+S", command=Setting.run)
        file_.add_command(label="Save", command=menubaroptions._save)
        file_.add_separator()
        file_.add_command(label='Exit', command=win.destroy)

    def edit():
        edit = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='cut', command=menubaroptions._cut)
        edit.add_command(label="Undo",command=menubaroptions._undo)
        edit.add_command(label="Redo",command=menubaroptions._redo)
        edit.add_command(label='copy', command=menubaroptions._copy)
        edit.add_command(label='Paste', command=menubaroptions._paste)
        edit.add_command(label='Select All', command=menubaroptions._select_all)
        edit.add_separator()
        edit.add_command(label='Find...',accelerator="Ctrl+F", command=None)
        # edit.add_command(label='Find and replace',command=None)

    def _help():
        help_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Help', menu=help_)
        help_.add_command(label='About This editor', command=menubaroptions._about)

    def _view():
        view = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="Themes", menu=view)
        view.add_checkbutton(label="Show Line num", )
        view.add_radiobutton(label="Default White",
                             )

    def _tools():
        tools_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="Tools", menu=tools_)
        tools_.add_command(label="Install package", command=pip.run)

    file()
    edit()
    _view()
    _help()
    _tools()
    win.config(menu=menu_)
