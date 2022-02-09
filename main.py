
from speech import*
import tkinter

root = tkinter.Tk()
root.geometry("720x450")
root.title("GUI Text To Speech")


#############################Text Area
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side= tkinter.RIGHT, fill= tkinter.Y)
textbox =  tkinter.Text(root)
textbox.pack()
# attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

def startact():
    txt = textbox.get(1.0, "end-1c")
    threadedsay(txt)




btn = tkinter.Button(text="Play ",command=startact,background="Gray",foreground="Pink")
btn.pack()


root.mainloop()
