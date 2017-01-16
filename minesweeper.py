#!/usr/bin/env python3
from tkinter import *
from random import randint

class Field:
    def __init__(self, base):
        self.board = []
        fieldFrame = Frame(base)
        fieldFrame.pack(side=BOTTOM)

        for row in range(15):
            self.board.append([])
            for col in range(20):
                self.board[row].append(Box(self.board, fieldFrame, row, col))

class Box(Field):
    def __init__(self, field, frame, row, column):
        self.opened = False
        self.containsMine = True if randint(1, 10) % 10 == 0 else False
        self.flagged = False

        self.gameField = field
        self.button = Button(frame, width=2, height=1)
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column)
        self.button.bind("<Button-1>", self.open_box)

    def open_box(self, x):
        self.opened = True
        if self.containsMine: print("Game Over")

def do_nothing(feature):
    print("Feature not Implemented yet: {}".format(feature))

base = Tk()
menu = Menu(base)
base.config(menu=menu)
gameMenu = Menu(menu)
menu.add_cascade(label="Game", menu=gameMenu)
gameMenu.add_command(label="Options", command=lambda doNothing=do_nothing: do_nothing("Game Settings"))
gameMenu.add_separator()
gameMenu.add_command(label="Exit", command=base.quit)

gameField = Field(base)

base.mainloop()
