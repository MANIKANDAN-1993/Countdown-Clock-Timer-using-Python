import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from threading import Timer
import winsound
from win10toast import ToastNotifier

# Creating a window
window = Tk()
window.geometry('600x600')
window.title('PythonGeeks')

head = Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))
head.pack(pady=20)

hour = StringVar()  # Define hour variable
minus = StringVar()  # Define minus variable
secon = StringVar()  # Define secon variable
check = BooleanVar()  # Define check variable

Label(window, text="Enter time in HH:MM:SS", font='bold').pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minus, width=30).pack()
Entry(window, textvariable=secon, width=30).pack()

Checkbutton(text='Check for Music', onvalue=True, variable=check).pack()

def countdown():
    # Get the time from user inputs
    hours = int(hour.get()) if hour.get().isdigit() else 0
    minutes = int(minus.get()) if minus.get().isdigit() else 0
    seconds = int(secon.get()) if secon.get().isdigit() else 0

    # Calculate the total time in seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds:
        # Calculate the minutes and seconds from the total seconds
        mins, secs = divmod(total_seconds, 60)
        # Format the display time
        display = '{:02d}:{:02d}'.format(mins, secs)
        # Update the label with the display time
        countdown_label.config(text=display)
        # Decrement the total seconds
        total_seconds -= 1
        # Sleep for 1 second
        time.sleep(1)

    # Display "Time-Up" when the countdown is finished
    countdown_label.config(text="Time-Up", font=('bold', 20))

    # Check if the checkbox is selected
    if check.get():
        winsound.Beep(440, 1000)  # Beep sound

    # Display notification on desktop
    toast = ToastNotifier()
    toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)


Button(window, text="Set Countdown", command=countdown, bg='yellow').place(x=260, y=230)

# Create a label to display the countdown
countdown_label = Label(window, text="", font=('bold'))
countdown_label.pack()

# To print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

window.mainloop()
