from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
current_card={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:    
    original_data=pandas.read_csv("data/english_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    try:
        current_card=random.choice(to_learn)
    except IndexError:
        empty_list=messagebox.showinfo(title="congratulations", message="Congratulations! You've mastered all the flashcards in this deck!")
        return
    
    flash_card.itemconfig(card_background,image= front_img)
    flash_card.itemconfig(word_text,text=current_card["English"], fill="black")
    flash_card.itemconfig(language_text,text="English", fill="black")
    flip_timer=window.after(3000,flip_card)

def flip_card():
    global current_card

    flash_card.itemconfig(language_text,text="Italian", fill="white")
    flash_card.itemconfig(word_text,text=current_card["Italian"], fill="white" )
    flash_card.itemconfig(card_background,image= back_img)

def remove_word():
    global current_card

    to_learn.remove(current_card)
    new_data=pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    
    next_card()

#------------------------- windows -------------------------#

window= Tk()
window.config(background= BACKGROUND_COLOR, padx= 50, pady= 50)
window.title("Flash Card")
flip_timer=window.after(3000,flip_card)

#------------------------- Flash card -------------------------#

flash_card= Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
flash_card.grid(column= 0, row= 0 ,columnspan= 2)

front_img= PhotoImage(file="images/card_front.png")
back_img= PhotoImage(file="images/card_back.png")

card_background=flash_card.create_image(400, 263, image= front_img)
language_text=flash_card.create_text(400, 150, font= ("Ariel", 40, "italic"))
word_text=flash_card.create_text(400, 263, font= ("Ariel", 60, "bold"))


#------------------------- buttons -------------------------#
check_image= PhotoImage(file= "images/right.png")
known_button= Button(image=check_image, highlightthickness= 0,command=remove_word)
known_button.grid(column= 1, row= 1)

cross_image= PhotoImage(file= "images/wrong.png")
unlnown_button= Button(image= cross_image, highlightthickness= 0,command=next_card)
unlnown_button.grid(column= 0, row= 1)

next_card()


window.mainloop()
