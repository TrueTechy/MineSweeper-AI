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
                                self.board[row][column].opened = True
                                self.noOfMines = self.noOfMines - 1
                                if(self.noOfMines==0):
                                   self.calculateNearbyMines()

    def calculateNearbyMines(self):
        for row in range(0, self.height):
            for column in range(0, self.width):
                nearbyMines = 0

                #TOP
                if(row==0):
                    break
                else:
                    if(column>0):
                        if(self.board[row-1][column-1].containsMine==1):
                            nearbyMines = nearbyMines + 1
                    #CENTRE
                    if (self.board[row - 1][column].containsMine == 1):
                        nearbyMines = nearbyMines + 1
                    #RIGHT
                    if(column<self.width-1):
                        if (self.board[row - 1][column + 1].containsMine == 1):
                            nearbyMines = nearbyMines + 1

                #MIDDLE
                if(0 <  column < self.width -1):
                    #LEFT
                    if (self.board[row][column - 1].containsMine == 1):
                        nearbyMines = nearbyMines + 1
                    #RIGHT
                    if (self.board[row][column + 1].containsMine == 1):
                        nearbyMines = nearbyMines + 1

                #BOTTOM
                if (row < self.height-2):
                    if (column > 0):
                        if (self.board[row + 1][column - 1].containsMine == 1):
                            nearbyMines = nearbyMines + 1
                    # CENTRE
                    print("("+str(row)+","+str(column)+")")
                    if (self.board[row + 1][column].containsMine == 1):
                        nearbyMines = nearbyMines + 1
                    # RIGHT
                    if (column < self.width - 1):
                        if (self.board[row + 1][column + 1].containsMine == 1):
                            nearbyMines = nearbyMines + 1

                self.board[row][column].nearbyMines = nearbyMines



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
        self.button.config(relief=GROOVE)
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column)
        self.button.bind("<Button-1>", self.openBox)
        #self.button.bind("<Button-2>", self.helper)
        self.button.bind("<Button-3>", self.flagBox)
        ## TODO: Calculate nearby mines somehow

    def openBox(self, event):
        if(self.flagged==True or self.opened==True):
            return 0
        else:
            self.opened = True
            if(self.containsMine==True):
                print("Game Over")
            elif(self.nearbyMines==0):
                ## open box and scan for nearby boxes to open
                print("No nearby mines")
                return
            else:
                self.button.config(relief=SUNKEN)
                self.button.config(text=self.nearbyMines)
                self.button.config(bg="snow")
                self.button.config(state=DISABLED)
                print(self.nearbyMines)
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

