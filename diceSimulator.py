import random
import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Dice Simulator')
root.geometry("300x300")

labelText = Label(root, text='', font = ("arial", 300))

def rollingTheDice():
    diceCode = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    labelText.config(text=f'{random.choice(diceCode)}')
    labelText.pack()

rollButton = Button(root, text="Roll Dice", command=rollingTheDice)
rollButton.place(x=125, y=270)

root.mainloop()
