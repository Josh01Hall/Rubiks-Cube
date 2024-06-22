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

        # Creates window
        window = tk.Tk()
        window.title("")
        window.geometry("600x600")
        
        # Adds text to window
        greeting = tk.Label(text="Move Selector", font=("Arial", 30, "bold"))
        greeting.pack()

        # Creates the colour selection button
        self.__colour_selection__ = tk.Button(window, text="White", command=lambda: self.__colour_toggle__(), height=2, width=10, background="White")
        self.__colour_selection__.pack()

        # Creates the data selection button
        self.__direction__ = tk.Button(window, text="Clockwise", command=lambda: self.__direction_toggle__(), height=2, width=10)
        self.__direction__.pack()
        
        # Creates the confirm button
        confirm = tk.Button(window, text="Confirm", command=lambda: self.__make_move__(), height=2, width=10)
        confirm.pack()

        # Creates the number of random moves button
        self.__random_number__ = tk.Spinbox(window, from_=0, to=100, width=10, state="readonly")
        self.__random_number__.pack()

        # Creates the randomise button
        random_button = tk.Button(window, text="Confirm", command=lambda: self.__move_randomiser__(), height=2, width=10)
        random_button.pack()

        # Creates the cube solver button
        solver = tk.Button(window, text="Solve Cube", command=lambda: self.__solve__(), height=2, width=10)
        solver.pack()

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
            time.sleep(0.75)


    # Solves the rubiks cube, outputting the time taken and the number of moves
    def __solve__(self):
        solver.solve(self.__parent__.myCube.faces)