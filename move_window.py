import tkinter as tk

class Move_GUI():
    
    def __init__(self):

        colour_labels = ["W", "Y", "O", "R", "G", "B"]

        window = tk.Tk()
        window.title("")
        window.geometry("600x600")
        
        greeting = tk.Label(text="Move Selector", font=("Arial", 30, "bold"))
        greeting.pack()
        greeting = tk.Label(text="In the box below, enter the face you want to move\n(W for White, Y for Yellow, O for Orange, R for Red,\nG for Green, B for Blue), followed by an apostrophe\n for anti-clockwise, and seperate each move with a comma", font=("Arial", 15))
        greeting.pack()

        input_box = tk.Text(window, height=10, width=40, font=("Arial", 8))
        input_box.pack()

        button = tk.Button(window, text="Move", command=lambda: self.__button_press__(input_box.get(1.0, "end-1c")))
        button.pack()

        window.mainloop()



    def __button_press__(self, text):
    
        formatted_moves = []

        try:
            moves = (text.upper).split(',')
        except:
            error = tk.Tk()
            error.title("Error")

        for move in moves:
            print()

window = Move_GUI()