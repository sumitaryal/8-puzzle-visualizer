import tkinter as tk
from tkinter import ttk
import time
from bfs import bfs
from dfs import dfs
from greedy import greedy
from astar import a_star
# Create initial and goal states
INITIAL_STATE = [[7, 2, 6], [3, 8, 4], [1, 5, None]]
# INITIAL_STATE = [[1, 2, 3], [4, 5, 6], [7, None, 8]]
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

class PuzzleSolverVisualizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.algorithm = tk.StringVar()
        self.speed = tk.DoubleVar()
        self.speed.set(0.5) # set default speed
        self.grid(row=0, column=0)
        self.create_widgets()

    def create_widgets(self):
        # Create label and option menu for choosing algorithm
        algorithm_label = ttk.Label(self, text="Choose algorithm:")
        algorithm_label.grid(row=0, column=0)
        algorithm_menu = ttk.OptionMenu(self, self.algorithm, "BFS", "BFS", "DFS", "Greedy", "A*")
        algorithm_menu.grid(row=0, column=1)

        # Create label and scale for adjusting speed
        speed_label = ttk.Label(self, text="Adjust speed:")
        speed_label.grid(row=1, column=0)
        speed_scale = ttk.Scale(self, variable=self.speed, from_=0.1, to=1.0, orient=tk.HORIZONTAL, length=200)
        speed_scale.grid(row=1, column=1)

        # Create button for starting the solver
        start_button = ttk.Button(self, text="Start", command=self.start_solver)
        start_button.grid(row=2, column=0, columnspan=2)

        # Create canvas for displaying the puzzle
        self.canvas = tk.Canvas(self, width=300, height=300, borderwidth=2, relief=tk.GROOVE)
        self.canvas.grid(row=3, column=0, columnspan=2)

        # Define box dimensions
        box_width = 100
        box_height = 100

        # Loop through the puzzle state and create a rectangle for each number or None value
        for i in range(3):
            for j in range(3):
                x1 = j * box_width
                y1 = i * box_height
                x2 = x1 + box_width
                y2 = y1 + box_height
                number = INITIAL_STATE[i][j]
                if number is not None:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
                    self.canvas.create_text(x1 + box_width//2, y1 + box_height//2, text=str(number))
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray', outline='black')

    def start_solver(self):
        # Get the chosen algorithm and speed
        algorithm = self.algorithm.get()
        speed = self.speed.get()

        # Solve the puzzle using the chosen algorithm
        if algorithm == "BFS":
            path = bfs(INITIAL_STATE, GOAL_STATE)
        elif algorithm == "DFS":
            path = dfs(INITIAL_STATE, GOAL_STATE)
        elif algorithm == "Greedy":
            path = greedy(INITIAL_STATE, GOAL_STATE)
        elif algorithm == "A*":
            path = a_star(INITIAL_STATE, GOAL_STATE)

        print(path)

        # Display the path on the canvas
        if path is not None:
            self.display_path(path)
        else:
            print("No solution found.") 

    def display_path(self, path):
        # Define box dimensions
        box_width = 100
        box_height = 100
    
        # Copy the initial state
        state = [row[:] for row in INITIAL_STATE]
    
        # Loop through each action in the path and apply it to the state
        for action in path:
            if action == "Up":
                row, col = self.find_blank(state)
                if row > 0:
                    state[row][col], state[row-1][col] = state[row-1][col], state[row][col]
            elif action == "Down":
                row, col = self.find_blank(state)
                if row < 2:
                    state[row][col], state[row+1][col] = state[row+1][col], state[row][col]
            elif action == "Left":
                row, col = self.find_blank(state)
                if col > 0:
                    state[row][col], state[row][col-1] = state[row][col-1], state[row][col]
            elif action == "Right":
                row, col = self.find_blank(state)
                if col < 2:
                    state[row][col], state[row][col+1] = state[row][col+1], state[row][col]
    
            # Clear the canvas
            self.canvas.delete("all")
    
            # Loop through the puzzle state and create a rectangle for each number or None value
            for row in range(3):
                for col in range(3):
                    x1 = col * box_width
                    y1 = row * box_height
                    x2 = x1 + box_width
                    y2 = y1 + box_height
                    number = state[row][col]
                    if number is not None:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
                        self.canvas.create_text(x1 + box_width//2, y1 + box_height//2, text=str(number))
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray', outline='black')
    
            # Update the canvas
            self.canvas.update()
    
            # Sleep to slow down the animation based on the selected speed
            time.sleep(1 - self.speed.get())
    
    def find_blank(self, state):
        # Find the row and column of the blank tile
        for row in range(3):
            for col in range(3):
                if state[row][col] is None:
                    return row, col
    

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleSolverVisualizer(master=root)
    app.mainloop()