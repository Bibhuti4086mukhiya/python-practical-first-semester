from tkinter import *
wn=Tk()
wn.title("hddh")
wn.geometry("200x20")
def abc():
    lbl_1 = Label(wn, text="hello ! ")

    lbl_2 = Label(wn, text="world")
    lbl_1.pack(padx=10, pady=20)
    lbl_2.pack(padx=10, pady=20)
    Button_1=Button(wn,text="check")
    Button_1.pack(side="right")

    Button_1.bind("<Button_1>",abc)

wn.mainloop()
