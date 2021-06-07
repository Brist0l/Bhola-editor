import tkinter
import menubaroptions
from functools import partial
import emoji
import Setting
import pip



def menu(win):
    menu_ = tkinter.Menu(win)

    def file():
        file_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="File", menu=file_)
        file_.add_command(label=emoji.emojize(':page_facing_up: New File'), command=None)
        file_.add_command(label=emoji.emojize(':open_mailbox_with_lowered_flag: Open'), command=menubaroptions._open)
        file_.add_command(label=emoji.emojize(':gear:Setting'), command=Setting.run)
        # file_.add_command(label="Save", command=save_as)
        file_.add_separator()
        file_.add_command(label='Exit', command=win.destroy)

    def edit():
        edit = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='cut', command=menubaroptions._cut)
        edit.add_command(label='copy', command=menubaroptions._copy)
        edit.add_command(label='Paste', command=menubaroptions._paste)
        edit.add_command(label='Select All', command=menubaroptions._select_all)
        # edit.add_separator()
        # find=partial(menubaroptions._find,win)
        # edit.add_command(label='Find...', command=find)
        # edit.add_command(label='Find and replace',command=None)

    def _help():
        help_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label='Help', menu=help_)
        help_.add_command(label='About This editor', command=menubaroptions._about)

    def _tools():
        tools_ = tkinter.Menu(menu_, tearoff=0)
        menu_.add_cascade(label="Tools", menu=tools_)
        tools_.add_command(label="Install package", command=pip.run)

    file()
    edit()
    _help()
    _tools()
    win.config(menu=menu_)
