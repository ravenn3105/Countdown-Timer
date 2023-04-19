# Import the time module
import time
import tkinter
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *

# Creating a CountDown Class
class CountDown:
    def __init__(self, root):
        self.window = root
        self.window.geometry("480x320+0+0")
        self.window.title('CountDown Timer')

        # Tkinter window background color
        self.window.configure(bg='gray35')

        # Fixing the Window length constant
        self.window.resizable(width=False, \
                              height=False)

        # Declaring a variable to pause the
        # countdown time
        self.pause = False

        # The Start and Pause buttons are placed
        # inside this frame
        self.button_frame = Frame(self.window, \
                                  bg="gray35", width=240, height=40)

        self.button_frame.place(x=230, y=150)

        # This frame is used to show the countdown
        # time label
        self.time_frame = Frame(self.window, bg="gray35", \
                                width=480, height=120).place(x=0, y=210)

        # Tkinter Labels
        time_label = Label(self.window, text="Set Time", \
                           font=("times new roman", 20, "bold"), \
                           bg='gray35', fg='white')

        time_label.place(x=180, y=30)

        hour_label = Label(self.window, text="Hour",
                           font=("times new roman", 15), bg='gray35', fg='white')
        hour_label.place(x=50, y=70)

        minute_label = Label(self.window, text="Minute",
                             font=("times new roman", 15), bg='gray35', fg='white')
        minute_label.place(x=200, y=70)

        second_label = Label(self.window, text="Second",
                             font=("times new roman", 15), bg='gray35', fg='white')
        second_label.place(x=350, y=70)
        # ===========================================

        # entry box for hours
        self.hour = IntVar()
        self.time_hour= tkinter.Entry(font=("Helvetica", 10), textvariable=self.hour)
        self.time_hour.grid(row=3,column=0, columnspan=1, padx=5, pady=110)

        # entry box for minutes
        self.minute = IntVar()
        self.time_mins= tkinter.Entry(font=("Helvetica", 10), textvariable=self.minute)
        self.time_mins.grid(row=3, column=1, columnspan=1, padx=5, pady=110)

        # entry box for seconds
        self.second = IntVar()
        self.time_sec= tkinter.Entry(font=("Helvetica", 10), textvariable=self.second)
        self.time_sec.grid(row=3, column=2, columnspan=1, padx=5, pady=110)
        # ==========================================='''

        # Tkinter Buttons
        # Cancel button
        cancel_button = Button(self.window, text='Cancel',
                               font=('Helvetica', 12), bg="white", fg="black",
                               command=self.Cancel)
        cancel_button.place(x=70, y=150)

        # Set Time Button
        # When the user will press this button
        # the 'Start' and 'Pause' button will
        # show inside the 'self.button_frame' frame
        set_button = Button(self.window, text='Set',
                            font=('Helvetica', 12), bg="white", fg="black",
                            command=self.Get_Time)
        set_button.place(x=160, y=150)

    # It will destroy the window
    def Cancel(self):
        self.pause = True
        self.window.destroy()

    # When the set button is pressed, this
    # function gets called
    def Get_Time(self):
        self.time_display = Label(self.time_frame,
                                  font=('Helvetica', 20, "bold"),
                                  bg='gray35', fg='yellow')
        self.time_display.place(x=50, y=250)



        try:

            # Total amount of time in seconds
            h = (int(self.time_hour.get()) * 3600)
            m = (int(self.time_mins.get()) * 60)
            s = (int(self.time_sec.get()))
            self.time_left = h + m + s

            # time(0:0:0) then a warning message will display
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!','Please select a right time to set')
            else:
                # Start Button
                start_button = Button(self.button_frame, \
                                      text='Start', font=('Helvetica', 12), \
                                      bg="green", fg="white", \
                                      command=self.Threading)

                start_button.place(x=20, y=0)

                # Pause Button
                pause_button = Button(self.button_frame, \
                                      text='Pause', font=('Helvetica', 12), \
                                      bg="red", fg="white", command=self.pause_time)

                pause_button.place(x=100, y=0)
        except Exception as es:
            messagebox.showerror("Error!", \
                                 f"Error due to {es}")

    # Creating a thread to run the show_time function
    def Threading(self):
        # Killing a thread through "daemon=True" isn't a
        # good idea
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    # It wil clear all the widgets inside the
    # 'self.button_frame' frame(Start and Pause buttons)
    def Clear_Screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def pause_time(self):
        self.pause = True

        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            # hour minute
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"Time Left: \
        {hours:02}: {mins:02}: {secs:02}")

        self.time_display.update()

    # When the Start button will be pressed then,
    # this "show_time" function will get called.
    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)

            hours = 0
            if mins > 60:
                # hour minute
                hours, mins = divmod(mins, 60)

            self.time_display.config(text=f"Time Left: \
            {hours:02}: {mins:02}: {secs:02}")

            self.time_display.update()

            # sleep function: for 1 second
            time.sleep(1)

            self.time_left = self.time_left - 1

            # When the time is over, a piece of music will
            # play in the background
            if self.time_left <= 0:
                process = multiprocessing.Process(target=playsound, \
                                                  args=('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\alarm-clock-short-6402.mp3',))  #enter the location of the audio file

                process.start()

                messagebox.showinfo('Time Over', \
                                    'Please ENTER to stop playing')

                process.terminate()
                # Clearing the 'self.button_frame' frame
                self.Clear_Screen()
            # if the pause button is pressed,
            # the while loop will break
            if self.pause == True:
                break


if __name__ == "__main__":
    root = Tk()
    # Creating a CountDown class object
    obj = CountDown(root)
    root.mainloop()
