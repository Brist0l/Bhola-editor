from tkinter import filedialog
import tkinter
import keyboard


def _open():
    filedialog.askopenfilename()


def _new():
    pass


def _paste():
    keyboard.press_and_release('ctrl+v')


def _select_all():
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('ctrl+a')


def _copy():
    keyboard.press_and_release('ctrl+c')
