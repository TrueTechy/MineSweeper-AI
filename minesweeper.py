from tkinter import *

# Dummy function for feature implementation tracking
def doNothing(feature):
    print("Feature not Implemented: " + feature)


class Field:

    board=[]

    def __init__(self, base):
        fieldFrame = Frame(base)
        fieldFrame.pack(side=BOTTOM)
        for row in range(0,15):
            self.board.append([])
            for column in range(0,20):
                self.board[row].append(Box(self.board, fieldFrame, row, column))




class Box(Field):

    opened = False
    containsMine = True
    flagged = False

    def __init__(self, field, frame, row, column):
        self.gameField = field
        self.button = Button(frame, width=2, height=1)
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column)
        self.button.bind("<Button-1>", self.openBox())

## Running function on startup
    def openBox(self):
        self.opened = True
        if(self.containsMine==True):
            print("Game Over")


# Create base window
base = Tk()
menu = Menu(base)
base.config(menu=menu)
gameMenu = Menu(menu)
menu.add_cascade(label="Game", menu=gameMenu)
gameMenu.add_command(label="Options", command=lambda doNothing=doNothing: doNothing("Game Settings"))
gameMenu.add_separator()
gameMenu.add_command(label="Exit", command=base.quit)


gameField = Field(base)


base.mainloop()