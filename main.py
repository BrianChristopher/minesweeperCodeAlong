from tkinter import *
import settings

# Override the settings of the window
root = Tk()
root.configure(bg='black')
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title('Minesweeper Game')  # FIXME This is not showing up; check other machines
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'red', # FIXME change to black later
    width = '1440',
    height = '180'
)
top_frame.place(x = 0, y = 0)

left_frame = Frame(
    root,
    bg = 'blue', # FIXME change to black later
    width = '360',
    height = '540'
)
left_frame.place(x = 0, y = 180)

# Run the window
root.mainloop()
