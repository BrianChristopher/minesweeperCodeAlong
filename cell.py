from tkinter import Button

class Cell:
    def __init__(self, x, y, isMine = False):
        self.x = x
        self.y = y
        self.isMine = isMine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions)  # Left click
        btn.bind('<Button-3>', self.right_click_actions) # Right click
        self.cell_btn_object = btn
    
    def left_click_actions(self, event):
        print(event)
        print("I am left click!")
    
    def right_click_actions(self, event):
        print(event)
        print("I am right click!")


