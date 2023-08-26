from tkinter import *
from datetime import datetime
from pytz import timezone


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.location = StringVar(self)
        self.location.set("Europe/Zurich")
        self.configure(bg="black")
        self.title("Clock")
        self.addClock("Europe/Zurich", "Zürich")
        self.addClock("US/Hawaii", "Hawaii")
        self.mainloop()

    def addClock(self, location, title):
        Label(self, text=title, font=("Century Gothic", 60), bg="black", fg="white").pack()

        frame = Frame(self, bg="black")
        frame.pack(padx=50, pady=20)

        time_label = Label(frame, font=("Century Gothic", 50), bg="black", fg="white")
        time_label.grid(column=0, row=1)
        self.time(location, time_label)

        Label(frame, font=('Century Gothic', 50), bg='black', fg='white', text=' | ').grid(column=1, row=1)

        Label(frame, font=('Century Gothic', 50), bg='black', fg='white', text=datetime.now(timezone(location)).strftime('%a')).grid(column=2, row=1)

    def time(self, location, label):
        time = datetime.now(timezone(location)).strftime("%H : %M : %S")
        label.config(text=time)
        label.after(1000, lambda: self.time(location, label))


if __name__ == '__main__':
    MainWindow()
