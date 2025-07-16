#!/usr/bin/env python3
import customtkinter as ctk

class MainApplication(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()

    root.geometry("600x500")
    root.title("Pomodoro-App")
    app = MainApplication(root)
    root.mainloop()
