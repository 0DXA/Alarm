import tkinter as tk
import alarm as al
import random
import playsound
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.title("Alarm")
        self.scale_frame = tk.Frame(self.frame)
        self.scale_label = tk.Label(self.scale_frame, text="Probability")
        self.scale = tk.Scale(self.scale_frame, length=300, orient=tk.HORIZONTAL, from_=0, to=100, tickinterval=50)
        self.minsize(350, 250)

        self.inc_buttons_frame = tk.Frame(self.frame)
        self.hour_inc_button = tk.Button(self.inc_buttons_frame, text="+", font=20)
        self.minute_inc_button = tk.Button(self.inc_buttons_frame, text="+", font=20)

        self.dec_buttons_frame = tk.Frame(self.frame)
        self.hour_dec_button = tk.Button(self.dec_buttons_frame, text="-", font=20)
        self.minute_dec_button = tk.Button(self.dec_buttons_frame, text="-", font=20)

        self.clock_frame = tk.Frame(self.frame)
        self.clock = tk.Label(self.clock_frame, text="00:00", font="arial 100")
        self.alarm = al.Alarm("Alarm")

        self.frame.pack(fill="both", expand=True)

        self.inc_buttons_frame.pack(fill="x", expand=True)
        self.hour_inc_button.pack(side="left", fill="x", expand=True)
        self.minute_inc_button.pack(side="right", fill="x", expand=True)

        self.clock_frame.pack(fill="both", expand=True)
        self.clock.pack(fill="both", expand=True)

        self.dec_buttons_frame.pack(fill="x", expand=True)
        self.hour_dec_button.pack(side="left", fill="x", expand=True)
        self.minute_dec_button.pack(side="right", fill="x", expand=True)

        self.scale_frame.pack(side="bottom", fill="x", expand=True)
        self.scale.pack(side="right")
        self.scale_label.pack(side="right")
        self.hour_inc_button.bind("<Button-1>", lambda x: self.hour_edit(True))
        self.hour_dec_button.bind("<Button-1>", lambda x: self.hour_edit(False))
        self.minute_inc_button.bind("<Button-1>", lambda x: self.minute_edit(True))
        self.minute_dec_button.bind("<Button-1>", lambda x: self.minute_edit(False))

    def minute_edit(self, inc=True):
        if inc:
            minute = self.alarm.get_minute() + 1
        else:
            minute = self.alarm.get_minute() - 1
        self.alarm.set_minute(minute)
        self.update()

    def hour_edit(self, inc=True):
        if inc:
            hour = self.alarm.get_hour() + 1
        else:
            hour = self.alarm.get_hour() - 1
        self.alarm.set_hour(hour)
        self.update()


    def update(self):
        self.clock.config(text=time.strftime("%H:%M",time.strptime("%d:%d" % (self.alarm.get_hour(),
                                                                              self.alarm.get_minute()),"%H:%M")))
        self.clock.update()

    def tick(self):
        if random.random() <= (self.scale.get() / 100):
            ring = self.alarm.tick()
            print(ring)
            if ring == "RING":
                playsound.playsound("alarm.wav")


if __name__ == "__main__":
    app = App()
    app.wm_geometry("400x300")


    def tick():
        app.tick()
        app.after(60000, tick)
    app.update()
    app.after(1000, tick)
    app.mainloop()
