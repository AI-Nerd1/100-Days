#!/usr/bin/env python3
"""Convert xlsx to csv"""
#! import pandas as pd
#TODO read_file = pd.read_excel (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.xlsx')
#TODO read_file.to_csv (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.csv', index = None, header=True)

from tkinter import *
from turtle import bgcolor
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashcards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

global card_word
global card_word1
global card_meaning

#window.after(3000, func= flip_card)

"""
    Front End Modifications here
"""

canvas = Canvas(width = 800, height = 520)
data = pandas.read_csv("/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.csv")
to_learn = data.to_dict(orient ="records")
current_card = {}

def next_card():
    global current_card
        #? card front
        
    current_card = random.choice(to_learn)
    card_word = canvas.create_text(400,230,text = "", font = ("garamond", 40, "bold"))
    # card_word1 = canvas.create_text(400,150,text = "", font = ("garamond", 25, "bold"), justify= "center")
    # card_meaning = canvas.create_text(400,250,text = "meaning", font = ("Ariel", 18, "italic"), justify= "left")
    canvas.itemconfig(card_background, image = card_front_image)
    canvas.itemconfig(card_word, text = current_card["WORD"])
    canvas.itemconfig(card_word1, text = " ")
    canvas.itemconfig(card_meaning, text = " ")
    right_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command= flip_card)
    wrong_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command = flip_card)
    
    
def flip_card():
    global current_card
    canvas.delete(card_word)
    #card_word = canvas.create_text(400,230,text = "", font = ("garamond", 40, "bold"))
    canvas.itemconfig(card_word, text = "")
    canvas.grid(row=0, column=0)
    canvas.itemconfig(card_background, image = card_back_image)
    canvas.itemconfig(card_word1, text = current_card["WORD"])
    canvas.itemconfig(card_meaning, text = current_card["DEFINITION"])
    right_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command= next_card)
    wrong_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command = next_card)
    #* Front button
   
    
    



               #? card back
card_front_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/card_front.png")
card_back_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/card_back.png")
card_background = canvas.create_image(400, 261, image = card_back_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan =2)

canvas.itemconfig(card_background, image = card_front_image)
current_card = random.choice(to_learn)
card_word = canvas.create_text(400,230,text = "", font = ("garamond", 40, "bold"))
card_word1 = canvas.create_text(400,150,text = "", font = ("garamond", 25, "bold"), justify= "center")
card_meaning = canvas.create_text(400,250,text = "meaning", font = ("Ariel", 18, "italic"), justify= "left")
canvas.itemconfig(card_word, text = current_card["WORD"])
canvas.itemconfig(card_word1, text = "")
canvas.itemconfig(card_meaning, text = "")


      #* back buttons
right_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/right.png")
right_button = Button(image = right_image)
right_button.grid(row=1, column=1)
right_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command= flip_card)

wrong_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/wrong.png")
wrong_button = Button(image = wrong_image)
wrong_button.grid(row=1, column=0)
wrong_button.config(bg = BACKGROUND_COLOR,border=0, highlightthickness=0, command = flip_card)

window.mainloop()

"""
    Back End Modifications here
"""