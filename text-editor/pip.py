import tkinter
import sys
import subprocess

module = ""


def run():
    # font info
    font = ("Arial", 15)

    # important vars
    sys_os = ""
    label_colour = ""

    # checking the OS
    if sys.platform.startswith('linux'):
        sys_os = "Linux"
        label_colour = "green"
    elif sys.platform.startswith("win"):
        sys_os = "Windows"
        label_colour = "#0110FE"
    elif sys.platform.startswith("darwin"):
        sys_os = "Mac OS a.k.a amir log"
        label_colour = "grey"

    def install(event):
        global module
        module = module_name.get()
        print(module)
        x = subprocess.run(f'pip install {module}', shell=True, capture_output=True)
        if "Requirement already satisfied" in str(x):
            confirm_label = tkinter.Label(pipwin, text=f"{str(module)} is already present", font=font, fg="green")
            confirm_label.pack()
            confirm_label.after(3000, pipwin.destroy)
        else:
            confirm_label = tkinter.Label(pipwin, text=f"{str(module)} installed", font=font, fg="green")
            confirm_label.pack()
            confirm_label.after(3000, pipwin.destroy)

    pipwin = tkinter.Tk()
    pipwin.focus_set()
    module_name = tkinter.StringVar()
    tkinter.Label(pipwin, text=sys_os, fg=label_colour, font=font).pack()
    module_name = tkinter.Entry(pipwin, fg=label_colour, font=font, textvariable=module_name)
    module_name.focus_set()
    module_name.pack()
    pipwin.bind("<Return>", install)
    pipwin.mainloop()
