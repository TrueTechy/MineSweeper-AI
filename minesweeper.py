from tkinter import *
import random
# Dummy function for feature implementation tracking
def doNothing(feature):
    print("Feature not Implemented: " + feature)


class Field:

    board=[]
    height = 5
    width = 5
    noOfMines = 20

    def __init__(self, base):
        fieldFrame = Frame(base)
        fieldFrame.pack(side=BOTTOM)
        for row in range(0,self.height):
            self.board.append([])
            for column in range(0,self.width):
               self.board[row].append(Box(self.board, fieldFrame, row, column))

        self.plantMines()
        self.showMines()

    def plantMines(self):
        while(self.noOfMines>0):
            for row in range(0, self.height):
                for column in range(0, self.width):
                        if (random.randint(0, 100) < 2):
                            if(self.board[row][column].containsMine==False):
                                self.board[row][column].containsMine = True
                                self.board[row][column].opened = True
                                self.noOfMines = self.noOfMines - 1

    def showMines(self):
        for row in range(0, self.height):
            for column in range(0, self.width):
                if(self.board[row][column].containsMine==True):
                    self.board[row][column].button.config(bg="blue")


class Box(Field):

    opened = False
    containsMine = False
    flagged = False
    nearbyMines = 0

    def __init__(self, field, frame, row, column):
        self.gameField = field
        self.button = Button(frame, width=2, height=1)
        self.button.config(bg="white smoke")
        self.button.config(relief=GROOVE)
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column)
        self.button.bind("<Button-1>", self.openBox)
        #self.button.bind("<Button-2>", self.helper)
        self.button.bind("<Button-3>", self.flagBox)
        ## TODO: Calculate nearby mines somehow

    def number_mines(self):
        total = []

        #top
        for i in [0, 1, -1]:
            try:
                total.append(Field.board[self.row - 1][self.column + i].containsMine)
            except IndexError:
                pass

        #bottom
        for i in [0, 1, -1]:
            try:
                total.append(Field.board[self.row + 1][self.column + i].containsMine)
            except IndexError:
                pass

        #left
        if self.column > 0: total.append(Field.board[self.row][self.column - 1].containsMine)

        #right
        if self.column < Field.width - 1: total.append(Field.board[self.row][self.column + 1].containsMine)

        total = sum(total)
        print("Total Number of Mines: {}".format(total))
        return total

    def openBox(self, event):
        x = self.number_mines()
        print(self.row, self.column)
        if(self.flagged==True or self.opened==True):
            return 0
        else:
            self.opened = True
            if(self.containsMine==True):
                print("Game Over")
            elif(not x):
                ## open box and scan for nearby boxes to open
                print("No nearby mines")
                return
            else:
                x = self.number_mines()
                self.button.config(relief=SUNKEN)
                self.button.config(text=x)
                self.button.config(bg="snow")
                self.button.config(state=DISABLED)
                return

    def flagBox(self, event):
        if(self.opened==True):
            return 0
        else:
            if(self.flagged==False):
                self.flagged = True
                self.button.config(bg = "red")
                self.button.config(state=DISABLED)
                return
            elif(self.flagged==True):
                self.flagged = False
                self.button.config(bg="white smoke")
                self.button.config(state=NORMAL)


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
gameField.showMines()

base.mainloop()
