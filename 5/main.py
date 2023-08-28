from tkinter import *


#Define the window
class MainWindow(Tk):
    #Capture the state of the play area
    states = [[-1, -1, -1],
              [-1, -1, -1],
              [-1, -1, -1]]
    buttons = [[None, None, None],
               [None, None, None],
               [None, None, None]]
    play_area = None
    turn = 'o'

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.setUpWindow()
        self.reset()
        self.mainloop()

    #Set up window with
    def setUpWindow(self):
        Label(self, text="Tic Tac Toe", font=("Arial", 40)).pack()
        Button(self, text="Reset", font=("Arial", 20), command=self.reset).pack()
        self.play_area = Canvas(self, width=300, height=300, bg='white', name="play_area")
        self.play_area.pack(pady=10, padx=10)

    #Set up or reset the play area
    def reset(self):
        self.turn = "o"
        for i in range(3):
            for j in range(3):
                self.states[i][j] = -1
                button = Button(self.play_area, text="", font=("Arial", 50), height=2, width=4,
                                   command=lambda row=i, col=j: self.triggerGrid(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons[i][j] = button

    #Triger when button on the grid pressed
    def triggerGrid(self, x, y):
        if self.turn == 'o' and self.states[x][y] == -1:
            self.states[x][y] = 1
            self.turn = 'x'
            self.buttons[x][y].config(text='x')

        elif self.turn == 'x' and self.states[x][y] == -1:
            self.states[x][y] = 0
            self.turn = 'o'
            self.buttons[x][y].config(text='o')


#Run the program
if __name__ == '__main__':
    MainWindow()
