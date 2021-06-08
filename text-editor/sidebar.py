import tkinter
import sys
import subprocess


def show():
    def run():
        _file = sys.argv[0]

    icon = tkinter.PhotoImage(file=r"Imgs/run.png")
    photo = icon.subsample(12, 12)
    run_btn = tkinter.Button(image=photo, bg="pink", compound=tkinter.LEFT)
    run_btn.image = photo
    run_btn.pack(side=tkinter.RIGHT, anchor="nw")
