import tkinter

start = tkinter.Tk()
tkinter.Label(start, text="Which languages do you work with?").grid()
tkinter.Checkbutton(start, text="Python").grid()
tkinter.Checkbutton(start, text="Java").grid()
tkinter.Checkbutton(start, text="JavaScript").grid()
start.mainloop()
