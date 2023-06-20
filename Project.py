from tkinter import *
from time import *


window = Tk()


def update_time():
    CLOCK = strftime('%H:%M:%S')
    label.config(text=CLOCK)
    window.after(1000, update_time)

DATE = strftime('%a     %b      %d')
label = Label(
    window,
    fg='#00FF00',
    bg='black',
    font=('Arial', 30),
    height=2
)

label_date = Label(
    window,
    text=DATE,
    fg='black',
    bg='yellow',
    compound='bottom',
    height=3,
    font=('Comic Sans MS',15)
)

label.pack()
label_date.pack()

update_time()

window.mainloop()