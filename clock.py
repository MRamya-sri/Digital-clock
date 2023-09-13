from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Creative Clock")

# Function to update the time
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create a label with custom styling
label = Label(root, font=("Helvetica", 100), background="black", foreground="cyan")
label.pack(anchor='center')

# Function to change text color randomly
def change_text_color():
    import random
    colors = ["cyan", "red", "green", "blue", "yellow", "magenta", "white"]
    random_color = random.choice(colors)
    label.config(foreground=random_color)
    label.after(2000, change_text_color)  # Change color every 2 seconds

# Create a button to change text color
color_button = Button(root, text="Change Color", command=change_text_color)
color_button.pack()

# Create a quit button
quit_button = Button(root, text="Quit", command=root.quit)
quit_button.pack()

time()  # Start the clock
change_text_color()  # Start changing text color

mainloop()




