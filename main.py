from tkinter import *

# Override the settings of the window
root = Tk()
root.configure(bg='black')
root.geometry('1140x720')
root.title('Minesweeper Game')  # FIXME This is not showing up; check other machines
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'red', # FIXME change to black later
    width = '1440',
    height = '180'
)
top_frame.place(x=0, y=0)

# Run the window
root.mainloop()
