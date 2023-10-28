
# ----------------------------------------------------- Import -------------------------------------------------------------- #
from customtkinter import *
import tkinter

root = CTk()
set_appearance_mode("dark")
set_default_color_theme("green")
w = 600
h = 700
root.geometry(f"{w}x{h}")
root.resizable("False","False")
root.title("Simple Calculator")


equation=""
def show(value):
    global equation
    equation+=value
    label_res.configure(text=equation)
def clear():
    global equation
    equation = ""
    label_res.configure(text=equation)

def calculate():
    global equation
    if equation!="":
        try:
            result = eval(equation)
        except:
            result = "Error"
    label_res.configure(text=result)
    equation = str(result)



frame = CTkFrame(root, width=400, height=600, corner_radius=5)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

frame1 = CTkFrame(frame,width=370,height=100, corner_radius=5 )
frame1.place(relx=0.03, rely=0.03, anchor=tkinter.NW)
label_res = CTkLabel(master=frame1,width=346,height=79,bg_color="white",font=CTkFont(weight="bold",size=30),text="",text_color="black")
label_res.place(relx = 0.03,rely=0.1,anchor=tkinter.NW)



frame2 = CTkFrame(frame, width=370, height=430, corner_radius=5)
frame2.place(relx=0.03, rely=0.25, anchor=tkinter.NW)

button_ac = CTkButton(master=frame2, width=70, height=60, text="AC",command=lambda :clear(),fg_color="#3697f5",font=CTkFont(weight="bold",size=20),hover_color="white")
button_ac.place(relx=0.03, rely=0.03, anchor=tkinter.NW)

button_per = CTkButton(master=frame2, width=70, height=60, text="(",font=CTkFont(weight="bold",size=20),command=lambda:show("("))
button_per.place(relx=0.25, rely=0.03, anchor=tkinter.NW)

button = CTkButton(master=frame2, width=70, height=60, text=")",font=CTkFont(weight="bold",size=20),command=lambda:show(")"))
button.place(relx=0.48, rely=0.03, anchor=tkinter.NW)

button_div = CTkButton(master=frame2, width=100, height=60, text="\u00f7", font=CTkFont(weight="bold", size=30),command=lambda:show("/"))
button_div.place(relx=0.7, rely=0.03, anchor=tkinter.NW)



button_7 = CTkButton(master=frame2, width=70, height=60, text="7",font=CTkFont(weight="bold",size=20),command=lambda:show("7"))
button_7.place(relx=0.03, rely=0.23, anchor=tkinter.NW)

button_8 = CTkButton(master=frame2, width=70, height=60, text="8",font=CTkFont(weight="bold",size=20),command=lambda:show("8"))
button_8.place(relx=0.25, rely=0.23, anchor=tkinter.NW)

button_9 = CTkButton(master=frame2, width=70, height=60, text="9",font=CTkFont(weight="bold",size=20),command=lambda:show("9"))
button_9.place(relx=0.48, rely=0.23, anchor=tkinter.NW)

button_mul = CTkButton(master=frame2, width=100, height=60, text="\u00D7",font=CTkFont(weight="bold",size=30),command=lambda:show("*"))
button_mul.place(relx=0.7, rely=0.23, anchor=tkinter.NW)



button_4 = CTkButton(master=frame2, width=70, height=60, text="4",font=CTkFont(weight="bold",size=20),command=lambda:show("4"))
button_4.place(relx=0.03, rely=0.43, anchor=tkinter.NW)

button_5 = CTkButton(master=frame2, width=70, height=60, text="5",font=CTkFont(weight="bold",size=20),command=lambda:show("5"))
button_5.place(relx=0.25, rely=0.43, anchor=tkinter.NW)

button_6 = CTkButton(master=frame2, width=70, height=60, text="6",font=CTkFont(weight="bold",size=20),command=lambda:show("6"))
button_6.place(relx=0.48, rely=0.43, anchor=tkinter.NW)

button_sub = CTkButton(master=frame2, width=100, height=60, text="-", font=CTkFont(weight="bold", size=30),command=lambda:show("-"))
button_sub.place(relx=0.7, rely=0.43, anchor=tkinter.NW)




button_1 = CTkButton(master=frame2, width=70, height=60, text="1",font=CTkFont(weight="bold",size=20),command=lambda:show("1"))
button_1.place(relx=0.03, rely=0.63, anchor=tkinter.NW)

button_2 = CTkButton(master=frame2, width=70, height=60, text="2",font=CTkFont(weight="bold",size=20),command=lambda:show("2"))
button_2.place(relx=0.25, rely=0.63, anchor=tkinter.NW)

button_3 = CTkButton(master=frame2, width=70, height=60, text="3",font=CTkFont(weight="bold",size=20),command=lambda:show("3"))
button_3.place(relx=0.48, rely=0.63, anchor=tkinter.NW)

button_add = CTkButton(master=frame2, width=100, height=60, text="+", font=CTkFont(weight="bold", size=30),command=lambda:show("+"))
button_add.place(relx=0.7, rely=0.63, anchor=tkinter.NW)




button_0 = CTkButton(master=frame2, width=150, height=60, text="0",font=CTkFont(weight="bold",size=20),command=lambda:show("0"))
button_0.place(relx=0.03, rely=0.83, anchor=tkinter.NW)

button1_dot = CTkButton(master=frame2, width=70, height=60, text=".", font=CTkFont(weight="bold", size=40),command=lambda:show("."))
button1_dot.place(relx=0.48, rely=0.83, anchor=tkinter.NW)

button_equal = CTkButton(master=frame2, width=100, height=60, text="=", font=CTkFont(weight="bold", size=30),fg_color="#fe9037",command=lambda:calculate())
button_equal.place(relx=0.7, rely=0.83, anchor=tkinter.NW)



root.mainloop()
