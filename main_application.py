#!/usr/bin/env python3
import customtkinter as ctk
from timer import Timer as timer_logic
from display_timer import TimerDisplay as timer_display
from timer_input import TimerInput as timer_input

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.timer_input = timer_input(self, callback_func=self.start_timer)
        self.timer_input.pack(pady = 20, padx=10)

        self.timer_logic = timer_logic()
        self.timer_display = timer_display(self, self.timer_logic)
        self.timer_display.pack(pady=10)

    def start_timer(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.timer_logic.set_time(hours=hours, minutes=minutes, seconds=seconds)
        self.timer_logic.start()
        self.timer_display.update_timer()
        print(f"Starting timer with {hours}h {minutes}m {seconds}s ")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()

    root.geometry("600x500")
    root.title("Pomodoro-App")

    app = MainApplication(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
