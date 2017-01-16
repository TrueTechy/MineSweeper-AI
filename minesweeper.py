from tkinter import *
import random
# Dummy function for feature implementation tracking
def doNothing(feature):
    print("Feature not Implemented: " + feature)


class Field:

    board=[]
    height = 15
    width = 20
    noOfMines = 30

    def __init__(self, base):
        fieldFrame = Frame(base)
        fieldFrame.pack(side=BOTTOM)
        for row in range(0,self.height):
            self.board.append([])
            for column in range(0,self.width):
               self.board[row].append(Box(self.board, fieldFrame, row, column))

        self.plantMines()

    def plantMines(self):
        while(self.noOfMines>0):
            for row in range(0, self.height):
                for column in range(0, self.width):
                        if (random.randint(0, 100) < 2):
                            if(self.board[row][column].containsMine==False):
                                self.board[row][column].containsMine = True
                                self.noOfMines = self.noOfMines - 1
                                if(self.noOfMines==0):
                                    return


    def showMines(self):
        for row in range(0, self.height):
            for column in range(0, self.width):
                if(self.board[row][column].containsMine==True):
                    self.board[row][column].button.config(relief=SUNKEN)


class Box(Field):

    opened = False
    containsMine = False
    flagged = False
    nearbyMines = 0

    def __init__(self, field, frame, row, column):
        self.gameField = field
        self.button = Button(frame, width=2, height=1)
        self.button.config(bg="white smoke")
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column)
        self.button.bind("<Button-1>", self.openBox)
        #self.button.bind("<Button-2>", self.helper)
        self.button.bind("<Button-3>", self.flagBox)
        ## TODO: Calculate nearby mines somehow

    def openBox(self, event):
        if(self.flagged==True):
            return
        self.opened = True
        if(self.containsMine==True):
            print("Game Over")
        elif(self.nearbyMines==0):
            ## open box and scan for nearby boxes to open
            return
        else:
            ## Reveal Number
            print(self.nearbyMines)
            return

    def flagBox(self, event):
        if(self.opened==False and self.flagged==False):
            self.flagged = True
            self.button.config(bg = "red")
            return
        elif(self.opened==FALSE and self.flagged==True):
            self.flagged = False
            self.button.config(bg="white smoke")


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