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
        sys_os = "Linux , u are a cool guy "
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
        if module == "":
            error_label = tkinter.Label(pipwin, text="pls provide a name!!", font=font, fg="red")
            error_label.pack()
            error_label.after(3000, error_label.destroy)
        else:
            x = subprocess.run(f'pip install {module}', shell=True, capture_output=True)
            if "Requirement already satisfied".lower() in str(x).lower():
                confirm_label = tkinter.Label(pipwin, text=f"{str(module)} is already present", font=font, fg="green")
                confirm_label.pack()
                confirm_label.after(3000, confirm_label.destroy)
            else:
                if "ERROR".lower() in str(x).lower():
                    error_label = tkinter.Label(pipwin, text=f"{str(module)} is not present!!", font=font, fg="red")
                    error_label.pack()
                    error_label.after(3000, error_label.destroy)
                else:
                    confirm_label = tkinter.Label(pipwin, text=f"{str(module)} installed", font=font, fg="green")
                    confirm_label.pack()
                    confirm_label.after(3000, confirm_label.destroy)

    def upgrade(event):
        global module
        module = module_name.get()
        x = subprocess.run(f"pip install --upgrade {module}", shell=True, capture_output=True)
        if "Requirement already satisfied".lower() in str(x).lower():
            confirm_label = tkinter.Label(pipwin, text=f"{str(module)} was already at its latest version", font=font,
                                          fg="green")
            confirm_label.pack()
            confirm_label.after(3000, confirm_label.destroy)
        else:
            confirm_label = tkinter.Label(pipwin, text=f"{str(module)} has been upgraded :)", font=font,
                                          fg="green")
            confirm_label.pack()
            confirm_label.after(3000, confirm_label.destroy)

    def destroy(event):
        pipwin.destroy()

    pipwin = tkinter.Tk()
    # icon = tkinter.PhotoImage(file="Imgs/pip_ico.png")
    # pipwin.iconphoto(False, icon)
    pipwin.resizable(0, 0)

    module_name = tkinter.StringVar()
    tkinter.Label(pipwin, text=sys_os, fg=label_colour, font=font).pack()
    module_name = tkinter.Entry(pipwin, fg=label_colour, font=font, textvariable=module_name)
    module_name.pack()
    module_name.focus_set()

    # adding keyboard bindings
    pipwin.bind("<Return>", install)
    pipwin.bind("<Shift-Return>", upgrade)
    pipwin.bind("<Escape>", destroy)

    # the main thing
    pipwin.mainloop()
