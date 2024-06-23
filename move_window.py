import tkinter as tk, random, time
from functools import partial
import solver

class Move_GUI():


    # Creates all elements in the window
    def __init__(self, parent_visualiser):

        # Reference to parent Visualiser object
        self.__parent__ = parent_visualiser

        # Colours of the centre tile of each face
        self.__colours__ = ["White", "Yellow", "Orange", "Red", "Green", "Blue"]

        # Position of each object
        positions = [(150, 10, 20, 20), (270, 100, 60, 60), (270, 165, 60, 60), (270, 230, 60, 60), (70, 100, 60, 60), (70, 165, 60, 60), (470, 100, 60, 60)]
        #            Header              Colour              Direction           Move                Number             Random             Solve

        # Creates window
        window = tk.Tk()
        window.title("")
        window.geometry("600x600")
        
        # Adds text to window
        greeting = tk.Label(text="Move Selector", font=("Arial", 30, "bold"))
        greeting.place(x=positions[0][0], y=positions[0][1])

        # Creates the colour selection button
        self.__colour_selection__ = tk.Button(window, text="White", command=lambda: self.__colour_toggle__(), background="White")
        self.__colour_selection__.place(x=positions[1][0], y=positions[1][1], height=positions[1][2], width=positions[1][3])

        # Creates the data selection button
        self.__direction__ = tk.Button(window, text="Clockwise", command=lambda: self.__direction_toggle__())
        self.__direction__.place(x=positions[2][0], y=positions[2][1], height=positions[2][2], width=positions[2][3])
        
        # Creates the confirm button
        confirm = tk.Button(window, text="Confirm", command=lambda: self.__make_move__())
        confirm.place(x=positions[3][0], y=positions[3][1], height=positions[3][2], width=positions[3][3])

        # Creates the number of random moves button
        self.__random_number__ = tk.Spinbox(window, from_=0, to=100, state="readonly", font=("Arial", 20, "normal"))
        self.__random_number__.place(x=positions[4][0], y=positions[4][1], height=positions[4][2], width=positions[4][3])

        # Creates the randomise button
        random_button = tk.Button(window, text="Confirm", command=lambda: self.__move_randomiser__())
        random_button.place(x=positions[5][0], y=positions[5][1], height=positions[5][2], width=positions[5][3])

        # Creates the cube solver button
        solver = tk.Button(window, text="Solve\nCube", command=lambda: self.__solve__())
        solver.place(x=positions[6][0], y=positions[6][1], height=positions[6][2], width=positions[6][3])

        window.mainloop()


    # Switches the text of the direction button
    def __direction_toggle__(self):
        if self.__direction__["text"] == "Clockwise":
            self.__direction__["text"] = "Anticlockwise"
        else:
            self.__direction__["text"] = "Clockwise"


    # Changes colour of selection_indicator
    def __colour_toggle__(self):

        # Colour of current selection indicator
        current_colour = self.__colour_selection__["background"]

        # Sets the new colour and text
        self.__colour_selection__["background"] = self.__colours__[(self.__colours__.index(current_colour.capitalize()) + 1) % 6]
        self.__colour_selection__["text"] = self.__colours__[(self.__colours__.index(current_colour.capitalize()) + 1) % 6].capitalize()


    # Passes the selected move to the visualiser, which passes it to the cube
    def __make_move__(self):
        
        # Collects selected colour and direction
        colour = self.__colour_selection__["background"].capitalize()
        indicator = self.__direction__["text"]

        # Clockwise or Anticlockwise
        direction = 1
        if indicator == "Anticlockwise":
            direction = -1

        # Waits if a move has already been sent to the cube
        while self.__parent__.__move_made__ != False:
            continue
        self.__parent__.__move_made__ = [self.__colours__.index(colour), direction]


    # Makes a user defined number of random moves on the cube
    def __move_randomiser__(self):

        count = int(self.__random_number__.get())

        while count > 0:
            while self.__parent__.__move_made__ != False:
                continue
            self.__parent__.__move_made__ = [int(random.random() * 6), random.choice([-1, 1])]
            count -= 1
            time.sleep(0.5)


    # Solves the rubiks cube, outputting the time taken and the number of moves
    def __solve__(self):
        solver.solve(self.__parent__.myCube.faces)