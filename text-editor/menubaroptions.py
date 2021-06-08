from tkinter import filedialog
from tkinter import *
import keyboard
from tkinter import messagebox as MessageBox
import webbrowser
from functools import partial

contents = ""


def _open():
    keyboard.press_and_release("ctrl+o")


def _new():
    pass


def _paste():
    keyboard.press_and_release('ctrl+v')


def _select_all():
    keyboard.press_and_release('ctrl+a')


def _copy():
    keyboard.press_and_release('ctrl+c')


def _cut():
    keyboard.press_and_release('ctrl+x')


def _about():
    webbrowser.open("https://github.com/mrHola21/Bhola-editor", new=2)

# def _find(win,text):
#     search_list = list()
#     s = ""
#
#     def reset_list():
#         if s != entry_widget_name.get():
#             print(entry_widget_name.get())
#             search_list.clear()
#             text_widget_name.tag_remove(SEL, 1.0, "end-1c")
#
#     def search_words():
#         reset_list()
#         global search_list
#         global s
#         text_widget_name.focus_set()
#         s = entry_widget_name.get()
#
#         if s:
#             if search_list == []:
#                 idx = "1.0"
#             else:
#                 idx = search_list[-1]
#
#             idx = text_widget_name.search(s, idx, nocase=1, stopindex=END)
#             lastidx = '%s+%dc' % (idx, len(s))
#
#             try:
#                 text_widget_name.tag_remove(SEL, 1.0, lastidx)
#             except:
#                 pass
#
#             try:
#                 text_widget_name.tag_add(SEL, idx, lastidx)
#                 counter_list = []
#                 counter_list = str(idx).split('.')
#                 text_widget_name.mark_set("insert",
#                                           "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
#                 text_widget_name.see(float(int(counter_list[0])))
#                 search_list.append(lastidx)
#             except:
#                 MessageBox.showinfo("Search complete", "No further matches")
#                 search_list.clear()
#                 text_widget_name.tag_remove(SEL, 1.0, "end-1c")
#
#     lbl_frame_entry = LabelFrame(win, text="Enter the text to search", padx=5, pady=5)
#     lbl_frame_entry.grid()
#
#     entry_widget_name = Entry(lbl_frame_entry, width=50, justify="left")
#     entry_widget_name.grid()
#
#     lbl_frame_text = LabelFrame(win, text="Enter the text here", padx=5, pady=5, height=260)
#     lbl_frame_text.grid()
#
#     text_widget_name = Text(lbl_frame_text)
#     text_widget_name.grid()
#
#     scrollbar = Scrollbar(text_widget_name, orient="vertical", command=text_widget_name.yview, cursor="arrow")
#     scrollbar.grid()
#     text_widget_name.config(yscrollcommand=scrollbar.set)
#
#     button_name = Button(win, text="Search", command=search_words, padx=5, pady=5)
#     button_name.grid()
