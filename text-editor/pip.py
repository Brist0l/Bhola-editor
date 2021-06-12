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
    def install(event):
        global module
        module = module_name.get()
        if module == "":
            error_label = tkinter.Label(text="pls provide a name!!", font=font, fg="red")
            error_label.pack(side=tkinter.LEFT, anchor="sw")
            error_label.after(3000, error_label.destroy)
        else:
            x = subprocess.run(f'pip install {module}', shell=True, capture_output=True)
            if "Requirement already satisfied".lower() in str(x).lower():
                confirm_label = tkinter.Label(text=f"{str(module)} is already present", font=font, fg="green")
                confirm_label.pack(side=tkinter.LEFT, anchor="sw")
                confirm_label.after(3000, confirm_label.destroy)
            else:
                if "ERROR".lower() in str(x).lower():
                    error_label = tkinter.Label(text=f"{str(module)} is not present!!", font=font, fg="red")
                    error_label.pack(side=tkinter.LEFT, anchor="sw")
                    error_label.after(3000, error_label.destroy)
                else:
                    confirm_label = tkinter.Label(text=f"{str(module)} installed", font=font, fg="green")
                    confirm_label.pack(side=tkinter.LEFT, anchor="sw")
                    confirm_label.after(3000, confirm_label.destroy)

    def upgrade(event):
        global module
        module = module_name.get()
        x = subprocess.run(f"pip install --upgrade {module}", shell=True, capture_output=True)
        if "Requirement already satisfied".lower() in str(x).lower():
            confirm_label = tkinter.Label(text=f"{str(module)} was already at its latest version", font=font,
                                          fg="green")
            confirm_label.pack(side=tkinter.LEFT, anchor="sw")
            confirm_label.after(3000, confirm_label.destroy)
        else:
            confirm_label = tkinter.Label(text=f"{str(module)} has been upgraded :)", font=font,
                                          fg="green")
            confirm_label.pack(side=tkinter.LEFT, anchor="sw")
            confirm_label.after(3000, confirm_label.destroy)

    def destroy(event):
        module_name.destroy()
        x.destroy()

    module_name = tkinter.StringVar()
    x = tkinter.Label(text="Pip", fg="blue", font=font)
    x.pack(side=tkinter.LEFT, anchor="sw")
    module_name = tkinter.Entry(font=font, textvariable=module_name)
    module_name.pack(side=tkinter.LEFT, anchor="sw")
    module_name.focus_set()

    # adding keyboard bindings
    module_name.bind("<Return>", install)
    module_name.bind("<Shift-Return>", upgrade)
    module_name.bind("<Escape>", destroy)
