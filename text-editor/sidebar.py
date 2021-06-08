import tkinter


def run(win):
    icon = tkinter.PhotoImage(file=r"Imgs/run.png")
    photo = icon.subsample(12, 12)
    run_btn = tkinter.Button(win, image=photo, compound=tkinter.LEFT)
    run_btn.image = photo
    run_btn.pack(side=tkinter.RIGHT, anchor="nw")
