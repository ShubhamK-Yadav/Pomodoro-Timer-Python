#!/usr/bin/env python3
from PIL import Image
import customtkinter as ctk
import tkextrafont as custom_font

from timer import Timer as timer_logic
from display_timer import TimerDisplay as timer_display
from timer_input import TimerInput as timer_gui
from controls import Controls as controls
from notification import Notification as notification

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, fg_color="transparent")
        self.parent = parent
        self.notif_title = "Pomodoro Completed!!"
        self.notif_text = "Time for a break!"

        # --- Font ---
        my_font = custom_font.Font(file="./assets/fonts/BoldPixels.ttf", family="BoldPixels")

        # --- Background Image ---
        bg_image = ctk.CTkImage(
            light_image=Image.open("./assets/images/Background.png"),
            dark_image=Image.open("./assets/images/Background.png"),
            size=(640, 540)
        )

        bg_label = ctk.CTkLabel(parent, image=bg_image, text="")
        bg_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- Background Container Shadow ---
        # Slightly larger, darker, and offset behind the main container
        shadow_offset_x = 15
        shadow_offset_y = 10
        shadow_width = 320# adjust based on your container size
        shadow_height = 370# adjust based on your container size

        background_cont = ctk.CTkFrame(
            parent,
            fg_color="#0d3618",  # darker than main container
            width=shadow_width,
            height=shadow_height
        )

        background_cont.place(
            relx=0.5, rely=0.5,
            x=shadow_offset_x, y=shadow_offset_y,  # offset for shadow
            anchor="center",
        )

        # --- Main Container ---
        container = ctk.CTkFrame(
            parent,
            fg_color="#6e9945",
            corner_radius=0,
            width=shadow_width,
            height=shadow_height
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        # --- Timer Notification ---
        self.notification = notification(
            title=self.notif_title,
            text=self.notif_text,
            desktop_notif=True,
            play_sound=True
        )

        # --- Timer Logic ---
        self.timer_logic = timer_logic(notification=self.notification)

        # --- Timer Input GUI ---
        self.timer_gui = timer_gui(container, font_prop="BoldPixels")

        # --- Timer Display ---
        self.timer_display = timer_display(container, self.timer_logic, font_prop="BoldPixels")

        # --- Controls ---
        self.button_controls = controls(
            container,
            input_gui=self.timer_gui,
            timer_logic=self.timer_logic,
            timer_display=self.timer_display
        )

        # --- Pack widgets inside container ---
        self.timer_gui.pack(pady=(10, 5), padx=5)
        self.timer_display.pack(pady=(5, 5), padx=5)
        self.button_controls.pack(pady=(5, 10), padx=5)

        # --- Keyboard shortcuts ---
        parent.bind("<space>", lambda e: self.button_controls.on_start_pause())
        parent.bind("r", lambda e: self.button_controls.on_reset())
        parent.bind("<Return>", lambda e: self.button_controls.on_start_pause())

        # --- Focus initial input ---
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

    root = ctk.CTk()
    root.title("Pomodoro App")
    root.configure(fg_color="#0d3618", corner_radius=20)
    center_window(root, 640, 540)

    app = MainApplication(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
