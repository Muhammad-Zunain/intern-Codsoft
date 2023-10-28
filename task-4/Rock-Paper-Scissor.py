
# ----------------------------------------------------- Import -------------------------------------------------------------- #

import random
from customtkinter import *
import tkinter
from PIL import Image

root = CTk(fg_color="#3d657d")
set_appearance_mode("dark")
set_default_color_theme("green")

w = 1000
h = 700

root.geometry(f"{w}x{h}")
root.title("Rock Paper Scissor")
root.resizable("False","False")

bg_image = CTkImage(Image.open("bg.jpg"),size=(1000,330))

rock_img = CTkImage(Image.open("rock.jpg"),size=(220,220))
paper_img = CTkImage(Image.open("paper.png"),size=(220,220))
scissor_img = CTkImage(Image.open("scissor.jpg"),size=(220,220))

rock1_img = CTkImage(Image.open("rock 2.png"),size=(220,220))
paper1_img = CTkImage(Image.open("paper2.jpg"),size=(220,220))
scissor1_img = CTkImage(Image.open("scissors 2.png"),size=(220,220))

def Main(item,user_count,comp_count,label_user,label_comp,label_res,img1,img2):

    computer = random.choice(["rock","scissor","paper"])

    if item == "rock" and computer == "rock":
        img2.configure(image=rock1_img)
        img1.configure(image=rock_img)

    elif item == "paper" and computer == "paper":
        img1.configure(image=paper_img)
        img2.configure(image=paper1_img)

    elif item == "scissor" and computer == "scissor":
        img1.configure(image=scissor_img)
        img2.configure(image=scissor1_img)



    if item == computer:
        label_res.configure(text="Match Draw !!")
    else:
        if item == "rock" and computer == "paper":
            comp_count = eval(comp_count)+1
            img1.configure(image=rock_img)
            img2.configure(image=paper1_img)
            label_comp.configure(text=str(comp_count))
            label_res.configure(text="You Lose !!")

        elif item == "rock" and computer == "scissor":
            user_count = eval(user_count)+1
            img1.configure(image=rock_img)
            img2.configure(image=scissor1_img)
            label_user.configure(text=str(user_count))
            label_res.configure(text="You Win !!")


        elif item == "paper" and computer == "rock":
            user_count = eval(user_count) + 1
            img1.configure(image=paper_img)
            img2.configure(image=rock1_img)
            label_user.configure(text=str(user_count))
            label_res.configure(text="You Win !!")


        elif item == "paper" and computer == "scissor":
            comp_count = eval(comp_count)+1
            img1.configure(image=paper_img)
            img2.configure(image=scissor1_img)
            label_comp.configure(text=str(comp_count))
            label_res.configure(text="You Lose !!")

        elif item == "scissor" and computer == "rock":
            comp_count = eval(comp_count) + 1
            img1.configure(image=scissor_img)
            img2.configure(image=rock1_img)
            label_comp.configure(text=str(comp_count))
            label_res.configure(text="You Lose !!")

        elif item == "scissor" and computer == "paper":
            user_count = eval(user_count)+1
            img1.configure(image=scissor_img)
            img2.configure(image=paper1_img)
            label_user.configure(text=str(user_count))
            label_res.configure(text="You Win !!")


def rock_paper_scissor(*windows):
    if windows != None:
        for i in windows:
            i.destroy()
    frame1 = CTkFrame(root,fg_color="#3d657d")
    frame1.place(relx=0,rely=0,relwidth=1,relheight=0.17,anchor=tkinter.NW)

    label = CTkLabel(frame1,text="Rock Paper Scissor",font=CTkFont(family="arial",weight="bold",size=35),text_color="#139ff2")
    label.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

    frame_score = CTkFrame(root,width=200,height=100,fg_color="#3d657d" ,corner_radius=10)
    frame_score.place(relx=0.85,rely=0.1,anchor=tkinter.CENTER)



    label_score_user = CTkLabel(master=frame_score, text="User Score :", text_color="#5199c4",
                           font=CTkFont(family="arial", weight="bold", size=16))
    label_score_user.place(relx=0.1, rely=0.19, anchor=tkinter.NW)

    label_count_user = CTkLabel(master=frame_score, text='0', text_color="white",font=CTkFont(family="arial", weight="bold", size=16))
    label_count_user.place(relx=0.79, rely=0.19, anchor=tkinter.NW)




    label_score_comp = CTkLabel(master=frame_score, text="Computer Score :", text_color="#5199c4",
                           font=CTkFont(family="arial", weight="bold", size=16))
    label_score_comp.place(relx=0.1, rely=0.55, anchor=tkinter.NW)

    label_count_comp = CTkLabel(master=frame_score, text='0', text_color="white",
                           font=CTkFont(family="arial", weight="bold", size=16))
    label_count_comp.place(relx=0.79, rely=0.55, anchor=tkinter.NW)



    label_Vs = CTkLabel(root,text="VS",text_color="#139ff2",font=CTkFont(family="arial",weight="bold",size=50))
    label_Vs.place(relx=0.495,rely=0.5,anchor=tkinter.CENTER)

    frame2 = CTkFrame(root,width=300,height=300,corner_radius=10,fg_color="white")
    frame2.place(relx=0.1,rely=0.3,anchor=tkinter.NW)


    label_user_img = CTkLabel(frame2,image=rock_img,text="")
    label_user_img.place(relx=0.1,rely=0.05, anchor = tkinter.NW,relwidth=0.8,relheight=0.9)

    frame3 = CTkFrame(root, width=300, height=300,corner_radius=10,fg_color="white")
    frame3.place(relx=0.6, rely=0.3, anchor=tkinter.NW)

    label_comp_img = CTkLabel(frame3, image=rock1_img, text="")
    label_comp_img.place(relx=0.1, rely=0.05, anchor=tkinter.NW, relwidth=0.8, relheight=0.9)

    label_user = CTkLabel(frame2,text="USER",text_color="black",font=CTkFont(family="arial",weight="bold",size=20))
    label_user.place(relx=0.4,rely=0.9,anchor=tkinter.NW)

    label_comp = CTkLabel(frame3,text="COMPUTER",text_color="black",font=CTkFont(family="arial",weight="bold",size=20))
    label_comp.place(relx=0.32,rely=0.9,anchor=tkinter.NW)

    label_res = CTkLabel(root,text="",font=CTkFont(family="arial",size=22,weight="bold"),text_color="#5199c4")
    label_res.place(relx=0.5,rely=0.93,anchor=tkinter.CENTER,relwidth=0.3,relheight=0.06)


    button_rock = CTkButton(root,text="Rock",width=150,height=60,corner_radius=0,text_color="white",border_color="white"
                            ,font=CTkFont(family="arial",size=15,weight="bold"),border_width=2,fg_color="blue",hover_color="#3d657d",
                            command=lambda :(Main("rock",label_count_user._text,label_count_comp._text,label_count_user,label_count_comp,label_res,label_user_img,label_comp_img)))
    button_rock.place(relx=0.35,rely=0.85,anchor=tkinter.CENTER)

    button_paper = CTkButton(root, text="Paper", width=150, height=60, corner_radius=0, text_color="white",border_color="white", border_width=2, fg_color="red"
                             ,font=CTkFont(family="arial",size=15,weight="bold"),hover_color="#3d657d",
                             command=lambda :(Main("paper",label_count_user._text,label_count_comp._text,label_count_user,label_count_comp,label_res,label_user_img,label_comp_img)))
    button_paper.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    button_scissor = CTkButton(root, text="Scissor", width=150, height=60, corner_radius=0, text_color="white",font=CTkFont(family="arial",size=15,weight="bold")
                               ,border_color="white", border_width=2, fg_color="orange",hover_color="#3d657d",
                               command=lambda :(Main("scissor",label_count_user._text,label_count_comp._text,label_count_user,label_count_comp,label_res,label_user_img,label_comp_img)))
    button_scissor.place(relx=0.65, rely=0.85, anchor=tkinter.CENTER)

    back_button = CTkButton(root, text="Back", command=lambda: back("home", back_button,frame1,frame2,frame3,frame_score,label_Vs,button_scissor,button_paper,button_rock,label_res)
                            , width=100,height=40,fg_color="#5199c4",hover_color="red",font=CTkFont(family="arial",size=15,weight="bold"),
                            border_color="white", border_width=1)
    back_button.place(relx=0.8, rely=0.9, anchor=tkinter.NW)


def home():

    bg_frame = CTkFrame(root, width=1000, height=700 ,fg_color=("#3d657d"))
    bg_frame.place(relx=0,rely=0,anchor = tkinter.NW)

    bg_label = CTkLabel(bg_frame, text="", image=bg_image)
    bg_label.pack()

    frame = CTkFrame(root, width=300, height=200 ,fg_color=("#3d657d"),border_width=1,border_color="white")
    frame.place(relx = 0.5 ,rely=0.7,anchor=tkinter.CENTER)

    button1 = CTkButton(frame, text="Play Game", width=250, height=40,fg_color="#5199c4",hover_color="#3d657d",
                        command=lambda :rock_paper_scissor(frame,bg_frame),border_color="white", border_width=1)
    button1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)



    exit_button = CTkButton(frame, text="Exit", command=lambda: root.destroy(), width=250, height=40, fg_color="#5199c4",hover_color="#3d657d",
                            border_color="white", border_width=1)
    exit_button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)


def back(page_name, *windows):
    for i in windows:           # "windows" contains all the frames of previous windows
        i.destroy()             #  destroys every frame inorder to go back
    if page_name == "home":
        home()
    elif page_name == "mainmenu":
        rock_paper_scissor()

home()
root.mainloop()