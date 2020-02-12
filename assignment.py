from tkinter import *

def register():
    print(asfsdf)

def login():
    print("You click on the login button")


def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("User name")
    Label(screen, text="user name",width="30",height="2", font=("calibri",14)).pack()
    Label(screen, text="").pack()
    Button(screen,text="Login",command=login).pack()
    Label(screen, text="").pack()
    Button(screen, text="register",command=register).pack()
    Label(screen, text="").pack()
    screen.mainloop()
main_screen()