#!/usr/bin/env python3
import customtkinter as ctk
from timer import Timer as timer_logic
from display_timer import TimerDisplay as timer_display
from timer_input import TimerInput as timer_input

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.timer_logic = timer_logic(minutes=25)
        self.timer_display = timer_display(self, self.timer_logic)
        self.timer_display.pack(pady=10)
        self.timer_input = timer_input(self)
        self.timer_input.pack(pady = 20)
        self.submit_button = ctk.CTkButton(self, text="Submit", command = self.timer_input.submit())
        self. submit_button.pack(pady=5)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()

    root.geometry("600x500")
    root.title("Pomodoro-App")

    app = MainApplication(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
