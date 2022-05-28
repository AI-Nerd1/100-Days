#!/usr/bin/env python3
"""Convert xlsx to csv"""
#! import pandas as pd
#TODO read_file = pd.read_excel (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.xlsx')
#TODO read_file.to_csv (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.csv', index = None, header=True)

from tkinter import *
from turtle import bgcolor

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

"""
    Front End Modifications here
"""

front_canvas = Canvas(width = 800, height = 500)
           #? card front
front_canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
front_canvas.grid(row=0, column=0)
card_front_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/card_front.png")
front_canvas.create_image(400, 263, image = card_front_image)

    #* Should be backend
front_canvas.create_text(400,150,text = "word", font = ("garamond", 40))
 
    #* Front button
flip_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/flip(1).png")
flip_button = Button(image = flip_image)
flip_button.grid(row=1, column=0)
flip_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0)



back_canvas = Canvas(width = 800, height = 500)
               #? card back
card_back_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/card_back.png")
back_canvas.create_image(400, 263, image = card_back_image)
back_canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
back_canvas.grid(row=0, column=0, columnspan = 2)

    #* Should be backend
back_canvas.create_text(400,50,text = "word", font = ("garamond", 40))
back_canvas.create_text(100,150,text = "meaning", font = ("Ariel", 14, "italic"))

      #* back buttons
right_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/right.png")
wrong_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/wrong.png")
right_button = Button(image = right_image)
wrong_button = Button(image = wrong_image)

right_button.grid(row=1, column=0)
right_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0)

wrong_button.grid(row=1, column=2)
wrong_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0)



window.mainloop()

"""
    Back End Modifications here
"""