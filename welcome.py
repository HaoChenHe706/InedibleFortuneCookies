import tkinter
import tkinter.messagebox as tkmb
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
import random
import pygame

pygame.mixer.init()

counter = 0

happy = ["LUCKY COOKIE", "Be mindful of your step", "Great day to adopt for a dog", "Consider saving your money today",
                  "You are illiterate","A friend might be an enemy in camouflage", "If you eat something and nobody sees you eat it, it has no calories", "Fortune doesn't favor fools"
                  "Believe it can be done!", "The fortune you seek is in another cookie","Don't let your limitations oveshadow your talents"]
             
sad = ["LUCKY COOKIE", "Ghost hug!!", "You look great today!", "You are strong enough to push through it", "Today is a great day to go out for a walk!",
              "Today's the perfect day to treat yourself!", "Someone is thinking about you right now", "A cup of hot cocoa/iced tea never hurts",
              "Be more confident! You got this", "LUCKY COOKIE"]

bored = [ "LUCKY COOKIE", "Can you lick your nose?", "Today is a great day to play tetris", "Bake something sweet!", "Put some music on and dance!",
                    "You deserve to take a break", "Clean your bedroom", "Be proud of yourself", "How long can you keep yourself from blinking?",
                    "Start a project you've always wanted to do"]
             
angry = ["LUCKY COOKIE", "Pick your battles", "Are you hungry or tired?", "Quality over quantity","Take your time", "You are doing better than you think you are", "A surprise will come for you soon",
                  "You are doing better than you think you are", "Be more gentle with yourself"]

fear = ["LUCKY COOKIE", "The first step is the hardest", "Take a break and watch your favourite movie", "Someone really wants to spend time with you today", "Don't give up sunshine!", "A perfect day to eat something sweet",
                "Something great is coming up", "You are a ray of sunshine", "A fresh start is what you need", "You can't have everything...where would you put it all?",
                 "All the effort you are making will ultimately pay off"]

default = ["LUCKY COOKIE", "Ghost hug!!", "You look great today!", "You are strong enough to push through it", "Today is a great day to go out for a walk!",
              "Today's the perfect day to treat yourself!", "Someone is thinking about you right now", "A cup of hot cocoa/iced tea never hurts",
              "Be more confident! You got this", "LUCKY COOKIE"]

moods = [happy, sad, bored, angry, fear]
moodstring = ["happy?", "sad?", "bored?", "angry?", "fear?"]

def check_mood():
    counter = 0
    MsgBox = 'no'
    while(MsgBox != "yes" and counter != 5):
        MsgBox = tk.messagebox.askquestion('Mood', 'Are you feeling :' + moodstring[counter])
        counter += 1
    if (MsgBox == "yes" or counter != 5):
        default = moods[counter-1]
    
def genRandomIndex():
    index = random.randrange(0, len(default), 1)
    return index

def genMessage():
    return default[genRandomIndex()]

def list_choice():
    check_mood()
    index = genRandomIndex()

def printMessage():
    global counter
    if (counter == 8):
        tkmb.showinfo("Max Number reached", "no more rolls for today")
        pop.destroy()
    else:
        message = genMessage()
        tkmb.showinfo("Your Fortune :)", message)
        counter += 1
    
def rollCookies():
    check_mood()

    welcome_bg.delete(welcome_txt_id)
    welcome_bg.delete(welcome_pic_id)
    button_start.destroy()
    button_help.destroy()
    
    global welcome_pic_id2
    #background for fortune cookies
    welcome_pic_id2 = welcome_bg.create_image(0,0,image=bg2,anchor="nw")

    global photo
    photo = PhotoImage(file = "fortuneCookie.png")
    global photoimage
    photoimage = photo.subsample(4,4) #resize photo
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,button_back



    c1 = Button(welcome, text = "cookie", bg= '#c5d3de', fg='#c5d3de', command = printMessage, image = photoimage,bd=0.2)
    c1.place(relx = 0.18, rely=0.16, width = 73, height = 58)

    c2 = Button(welcome, text = "cookie", bg= '#cbd5de', fg='#c5d3de', command = printMessage, image = photoimage,bd=0.2)
    c2.place(relx = 0.51, rely=0.40, width = 73, height = 58)

    c3 = Button(welcome, text = "cookie", bg= '#cedbe4', fg='#cedbe4', command = printMessage, image = photoimage,bd=0.2)
    c3.place(relx = 0.65, rely=0.25, width = 73, height = 58)

    c4 = Button(welcome, text = "cookie", bg= '#c4d1da', fg='#c4d1da', command = printMessage, image = photoimage,bd=0.2)
    c4.place(relx = 0.8, rely=0.8, width = 73, height = 58)

    c5 = Button(welcome, text = "cookie", bg= '#cedbe4', fg='#cedbe4', command = printMessage, image = photoimage,bd=0.2)
    c5.place(relx = 0.7, rely=0.2, width = 73, height = 58)

    c6 = Button(welcome, text = "cookie", bg= '#c4d1da', fg='#c4d1da', command = printMessage, image = photoimage,bd=0.2)
    c6.place(relx = 0.1, rely=0.3, width = 73, height = 58)

    c7 = Button(welcome, text = "cookie", bg= '#c7d3df', fg='#c7d3df', command = printMessage, image = photoimage,bd=0.2)
    c7.place(relx = 0.9, rely=0.5, width = 73, height = 58)

    c8 = Button(welcome, text = "cookie", bg= '#c4d1da', fg='#c4d1da', command = printMessage, image = photoimage,bd=0.2)
    c8.place(relx = 0.85, rely=0.75, width = 73, height = 58)

    c9 = Button(welcome, text = "cookie", bg= '#d1dbe4', fg='#d1dbe4', command = printMessage, image = photoimage,bd=0.2)
    c9.place(relx = 0.55, rely=0.15, width = 73, height = 58)

    c10 = Button(welcome, text = "cookie", bg= '#c2cfd8', fg='#c2cfd8', command = printMessage, image = photoimage,bd=0.2)
    c10.place(relx = 0.8, rely=0.9, width = 73, height = 58)
    
    c11 = Button(welcome, text = "cookie", bg= '#cdd9e5', fg='#cdd9e5', command = printMessage, image = photoimage,bd=0.2)
    c11.place(relx = 0.72, rely=0.33, width = 73, height = 58)

    c12 = Button(welcome, text = "cookie", bg= '#c8d4e0', fg='white', command = printMessage, image = photoimage,bd=0.2)
    c12.place(relx = 0.78, rely=0.48, width = 73, height = 58)

    c13 = Button(welcome, text = "cookie", bg= '#c0cdd6', fg='#c0cdd6', command = printMessage, image = photoimage,bd=0.2)
    c13.place(relx = 0.92, rely=0.91, width = 73, height = 58)

    c14 = Button(welcome, text = "cookie", bg= '#ccd9e2', fg='#ccd9e2', command = printMessage, image = photoimage,bd=0.2)
    c14.place(relx = 0.88, rely=0.25, width = 73, height = 58)

    c15 = Button(welcome, text = "cookie", bg= '#e0ecea', fg='#e0ecea', command = printMessage, image = photoimage,bd=0.2)
    c15.place(relx = 0.48, rely=0.72, width = 73, height = 58)

    c16 = Button(welcome, text = "cookie", bg= '#bfccd5', fg='#bfccd5', command = printMessage, image = photoimage,bd=0.2)
    c16.place(relx = 0.03, rely=0.37, width = 73, height = 58)

    c17 = Button(welcome, text = "cookie", bg= '#f7fdfd', fg='#f7fdfd', command = printMessage, image = photoimage,bd=0.2)
    c17.place(relx = 0.4, rely=0.5, width = 73, height = 58)

    c18 = Button(welcome, text = "cookie", bg= '#cfd9e2', fg='#cfd9e2', command = printMessage, image = photoimage,bd=0.2)
    c18.place(relx = 0.4, rely=0.06, width = 73, height = 58)

    c19 = Button(welcome, text = "cookie", bg= '#d1dbe4', fg='#d1dbe4', command = printMessage, image = photoimage,bd=0.2)
    c19.place(relx = 0.72, rely=0.07, width = 73, height = 58)

    c20 = Button(welcome, text = "cookie", bg= '#c0cdd6', fg='#c0cdd6', command = printMessage, image = photoimage,bd=0.2)
    c20.place(relx = 0.15, rely=0.38, width = 73, height = 58)


    button_back = Button(welcome, text="Back", font=("Times New Roman", 15), command=not_first_time)
    button_back.place(relx=0.1, rely=0.1,anchor=NW)

def music():
    pygame.mixer.music.load("sound.mp3") #credit to www.bensound.com
    pygame.mixer.music.play(loops=5)
def music_off():
    pygame.mixer.music.stop()

def not_first_time():
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()
    c5.destroy()
    c6.destroy()
    c7.destroy()
    c8.destroy()
    c9.destroy()
    c10.destroy()
    c11.destroy()
    c12.destroy()
    c13.destroy()
    c14.destroy()
    c15.destroy()
    c16.destroy()
    c17.destroy()
    c18.destroy()
    c19.destroy()
    c20.destroy()
    button_back.destroy()
    welcome_bg.delete(welcome_pic_id2)
    front_page()

def front_page():

    #front_page_background
    global welcome_pic_id
    welcome_pic_id = welcome_bg.create_image(0,0,image=bg1,anchor="nw")

    #Welcome text
    global welcome_txt_id
    welcome_txt_id = welcome_bg.create_text(630,150,text="Welcome!", font=("Times New Roman", 50), fill="white", anchor=CENTER)

    #Buttons 
    global button_start, button_achievement, button_help

    button_start = Button(welcome, text="Play", font=("Times New Roman", 15), command=rollCookies)
    button_help = Button(welcome, text="Help", font=("Times New Roman", 15), command=instructions)
    button_start.place(relx=0.5,rely=0.55,anchor=CENTER)
    button_help.place(relx=0.5,rely=0.65,anchor=CENTER)

    button_music_on = Button(welcome, image=play_button, command=music)
    button_music_off = Button(welcome, image=stop_button, command=music_off)
    button_music_on.place(relx=0.9,rely=0.1,anchor=CENTER)
    button_music_off.place(relx=0.95,rely=0.1,anchor=CENTER)

def back():
    pop.destroy()

def instructions():
    global bg3
    global pop
    bg3 = PhotoImage(file="crystal-ball.png")
    pop = Toplevel(welcome)
    pop.title("Help")
    pop.geometry("705x414")
    help_bg = tk.Label(pop, image=bg3)
    help_bg.place(x=0,y=0,relwidth=1,relheight=1)
    help_txt = Button(pop, text="Click on a cookie to \n get your fortune", font=("Times New Roman", 15), command=back, bd=0, bg="white")
    help_txt.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    

welcome = Tk()
welcome.title("Inedible Fortune Cookies")
welcome.state("zoomed")

#Images
bg1 = PhotoImage(file="wood.png")
bg2 = PhotoImage(file="fortune.png")

play_button = PhotoImage(file="playing.png")
stop_button = PhotoImage(file="mute.png")

#Canvas + Background Image
welcome_bg = Canvas(welcome, highlightthickness=0, width=1200,height=500)
welcome_bg.pack(fill="both", expand=True)

front_page()

welcome.mainloop()
