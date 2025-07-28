#!/usr/bin/env python3
import button_controls
import customtkinter as ctk
from timer import Timer as timer_logic
from display_timer import TimerDisplay as timer_display
from timer_input import TimerInput as timer_gui
from button_controls import ButtonControls as controls

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.timer_gui= timer_gui(self)
        self.timer_gui.pack(pady = 20, padx=10)

        self.timer_logic = timer_logic()
        self.timer_display = timer_display(self, self.timer_logic)
        self.timer_display.pack(pady=10)

        self.button_controls = controls(self,
                                        input_gui=self.timer_gui,
                                        timer_logic=self.timer_logic,
                                        timer_display=self.timer_display)
        self.button_controls.pack(pady=10)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()

    root.geometry("600x500")
    root.title("Pomodoro-App")

    app = MainApplication(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
