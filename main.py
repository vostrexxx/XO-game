from tkinter import *
import random


def next_turn():
    pass


def check_winner():
    pass


def empty_spaces():
    pass


def new_game():
    pass


window = Tk()
window.title("XO GAME")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text= player + " turn", font=("consolas", 40))
label.pack(side="top")

window.mainloop()
