#!/usr/bin/env python3
import customtkinter as ctk
from timer import Timer as timer_logic
from display_timer import TimerDisplay as timer_display
from timer_input import TimerInput as timer_gui
from controls import Controls as controls

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, corner_radius=12, fg_color="#1f2937")
        self.parent = parent

        # container for padding
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)
        self.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        # Timer logic / display / input
        self.timer_logic = timer_logic()
        self.timer_gui = timer_gui(content)
        self.timer_display = timer_display(content, self.timer_logic)
        self.button_controls = controls(
            content,
            input_gui=self.timer_gui,
            timer_logic=self.timer_logic,
            timer_display=self.timer_display
        )

        # Layout using grid for fine control
        self.timer_gui.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        self.timer_display.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        self.button_controls.grid(row=2, column=0, sticky="ew")

        # Keyboard shortcuts
        parent.bind("<space>", lambda e: self.button_controls.on_start_pause())
        parent.bind("r", lambda e: self.button_controls.on_reset())
        parent.bind("<Return>", lambda e: self.button_controls.on_start_pause())

        # Focus initial input
        self.timer_gui.hours_entry.focus_set()

def center_window(win, width=600, height=500):
    win.update_idletasks()
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.minsize(500, 420)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Pomodoro App")
    center_window(root, 640, 540)

    app = MainApplication(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
