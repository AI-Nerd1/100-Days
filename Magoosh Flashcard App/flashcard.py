#!/usr/bin/env python3
"""Convert xlsx to csv"""
#! import pandas as pd
#TODO read_file = pd.read_excel (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.xlsx')
#TODO read_file.to_csv (r'/home/logan/github/100-Days/Magoosh Flashcard App/wordlist.csv', index = None, header=True)

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width = 800, height = 500)
card_front_image = PhotoImage(file ="/home/logan/github/100-Days/Magoosh Flashcard App/images/card_front.png")
canvas.create_image(400, 263, image = card_front_image)
canvas.grid(row=0, column=0)
window.mainloop()

