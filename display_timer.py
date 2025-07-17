#!/usr/bin/env python3
import customtkinter as ctk

class TimerDisplay(ctk.CTkLabel):
    def __init__(self, parent, timer_logic):
        self.timer = timer_logic
        super().__init__(parent, text=self.timer.formatted_time(), font=("Comic Sans MS", 36))
        self.update_timer()

    def update_timer(self):
        self.configure(text= self.timer.formatted_time())
        # Do not pass () with update_timer, only reference passed
        # Telling it what to call essentially instead of calling it right now
        self.after(1000, self.update_timer)
