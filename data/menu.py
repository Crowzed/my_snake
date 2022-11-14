#create two button start and exit
#start button will start the game
#exit button will exit the game

from tkinter import Tk, ttk
from tkinter import Label
from tkinter import Button
#creating a window
window = Tk()
window.title("Snake Game")
window.geometry("400x400")
window.configure(background = "light green")
#creating a label
lbl = Label(window, text = "Centrico's snake, pls no kill", font = ("Arial Bold", 20))
lbl.grid(column = 0, row = 0)
#creating a function
def start():
    window.destroy()
    import snake
def exit():
    window.destroy()
#creating a button
btn = Button(window, text = "Start", bg = "orange", fg = "red", command = start)
btn.grid(column = 0, row = 1)
btn = Button(window, text = "Exit", bg = "orange", fg = "red", command = exit)
btn.grid(column = 0, row = 2)
window.mainloop()
