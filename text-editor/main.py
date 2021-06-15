import tkinter
from tkinter import *
import tkinter.filedialog
import menubar
import sidebar
import hierarchical
import tkinter.font
import sys
import subprocess

# static variables
BACKGROUND = "#333333"
FOREGROUND = "#E9F0F2"
KEYWORD = "#FEB801"
# ENG_WORDS = open("word-lists/american-english.txt").read().split("\n")
KEYWORDS = open("word-lists/keywords").read().split("\n")

# creating the main window
win = tkinter.Tk()

# font
font = tkinter.font.Font(family="Arial", size=12)

# setting the max size
win.maxsize(win.winfo_screenheight(), win.winfo_screenwidth())

# setting the min size
win.minsize(500, 500)

# for the find
find_font = tkinter.font.Font(family="Arial", size=12)
e = tkinter.StringVar()
x = tkinter.Entry(textvariable=e, font=find_font)
y = tkinter.Label(text="Find")

# specifying the title
win.title("Bhola editor")

# declaring an icon
icon = tkinter.PhotoImage(file="Imgs/main_ico.png")
sidebar.show()

# setting the icon img as the icon
win.iconphoto(True, icon)

# adding the menu
menubar.menu(win)

fileName = ""
# adding the main writing space
text = tkinter.Text(win, font=font, bg=BACKGROUND, fg=FOREGROUND, insertbackground=FOREGROUND, borderwidth=0,
                    highlightthickness=0,undo=True)
output = Text(win,height=10)
text.pack(expand=True, side=tkinter.TOP, fill=tkinter.BOTH)
output.pack()
text.focus_set()  # sets the cursor at the writing space
# text.tag_configure("misspelled", foreground=MISSPELLED, underline=True)
text.tag_configure("highlight", foreground=KEYWORD, underline=False)



# saving logic
def save_as(event):
    global text
    files = [('Python Files', '*.py')]
    t = text.get("1.0", tkinter.END)
    save_location = tkinter.filedialog.asksaveasfile(filetypes=files)
    if save_location != None:
        try:
            with open(save_location.name, "r+") as file1:file1.write(t)
        except TypeError as e:
            errorwin = tkinter.Toplevel()
            errorlabel = tkinter.Label(errorwin,text=e,font=find_font)
            errorlabel.pack()


def _open_file(event):
    global file,filename
    file = tkinter.filedialog.askopenfilename()
    filename = file
    if file == "":
        file = None
    else:
        text.delete(1.0, tkinter.END)
        with open(file, "r+") as f:
            text.insert(1.0, f.read())


def _open_folder(event):
    hierarchical.run()


def change_font_size(event):
    fontsize = font['size']
    if event.num == 5 or event.delta == -120:
        if fontsize == 7:
            pass
        else:
            font.configure(size=fontsize - 1)
    if event.num == 4 or event.delta == 120:
        if fontsize == 35:
            pass
        else:
            font.configure(size=fontsize + 1)


def on_find(event):
    def find(event):
        def change():
            text.tag_config('found', foreground=FOREGROUND)

        text.tag_remove('found', '1.0', tkinter.END)
        s = e.get()
        if s:
            idx = '1.0'
            while 1:
                idx = text.search(s, idx, nocase=1,
                                  stopindex=tkinter.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                text.tag_add('found', idx, lastidx)
                idx = lastidx
        text.tag_config('found', foreground='red')
        text.after(1000, change)

    def destroy(event):
        y.destroy()
        x.destroy()

    y.pack(side=tkinter.LEFT, anchor="sw")
    x.pack(side=tkinter.LEFT, anchor="sw")
    x.focus_set()
    x.bind("<Return>", find)
    x.bind("<Escape>", destroy)


def Syntaxhighlight(event):
    index = text.search(r'\s', "insert", backwards=True, regexp=True)
    if index == "":
        index = "1.0"
    else:
        index = text.index("%s+1c" % index)
    word = text.get(index, "insert")
    if word in KEYWORDS:
        text.tag_add("highlight", index, "%s+%dc" % (index, len(word)))
    else:
        text.tag_remove("highlight", index, "%s+%dc" % (index, len(word)))


Scroll = tkinter.Scrollbar(text)
Scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
Scroll.config(command=text.yview)
text.config(yscrollcommand=Scroll.set)

def undo(event):
    global text
    text.edit_undo
def redo(event):
    global text
    text.edit_redo
def new(event):
    text.delete(1.0, END)

def run(event):
    # code2run = text.get("1.0",END)
    # exec(code2run)
    command = f"python {filename}"
    pro = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, error = pro.communicate()
    output.insert('1.0',out)

# adding keybindings
win.bind("<Control-s>", save_as)
win.bind("<Control-z>", undo)
win.bind("<Control-y>", redo)
win.bind("<Control-s>", save_as)
win.bind("<Control-n>", new)
win.bind("<Control-r>", run)
win.bind("<Control-o>", _open_file)
win.bind("<Control-Shift-O>", _open_folder)
if sys.platform.startswith("linux"):
    win.bind("<Control-Button-4>", change_font_size)
    win.bind("<Control-Button-5>", change_font_size)
else:
    win.bind("<Control-MouseWheel>", change_font_size)
win.bind("<Control-f>", on_find)
text.bind("<Key>", Syntaxhighlight)

# the main thing
win.mainloop()