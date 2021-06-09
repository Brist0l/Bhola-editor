import tkinter
import tkinter.ttk


def run():
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
        rb4.pack(side=tkinter.TOP, anchor="w")
        rb3.pack(side=tkinter.TOP, anchor="w")
        rb5.pack(side=tkinter.TOP, anchor="w")
        rb6.pack(side=tkinter.TOP, anchor="w")
        rb7.pack(side=tkinter.TOP, anchor="w")

    def general():
        global yes_no
        check_font_increase.pack(side=tkinter.TOP)
        yes_no = _font_increase.get()
        print(yes_no)

    def callback(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            if data == "Theme":
                theme()
            elif data == "Font":
                font()
            elif data == "General":
                general()

    # main window
    setting = tkinter.Tk()
    setting.resizable(0, 0)
    listbox = tkinter.Listbox(setting)
    listbox.insert(1, "General")
    listbox.insert(2, "Theme")
    listbox.insert(3, "Font")

    # variables
    _theme = tkinter.StringVar()
    _font = tkinter.StringVar()
    _font_increase = tkinter.IntVar()

    # theme values
    rb1 = tkinter.Radiobutton(setting, variable=_theme, value="dark")
    rb2 = tkinter.Radiobutton(setting, variable=_theme, value="light")

    # font values
    rb3 = tkinter.Radiobutton(setting, variable=_font, value="Comic Sans MS")
    rb4 = tkinter.Radiobutton(setting, variable=_font, value="System")
    rb5 = tkinter.Radiobutton(setting, variable=_font, value="Modern")
    rb6 = tkinter.Radiobutton(setting, variable=_font, value="Courier")
    rb7 = tkinter.Radiobutton(setting, variable=_font, value="MS Serif")

    # genral values
    check_font_increase = tkinter.Checkbutton(setting, variable=_font_increase, onvalue=1, offvalue=0,
                                              text="increase font size with ctrl+mousewheel")

    # packing
    listbox.pack(side=tkinter.LEFT, fill="x")
    listbox.bind("<<ListboxSelect>>", callback)
    setting.mainloop()
