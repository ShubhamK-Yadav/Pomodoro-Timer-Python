# Make this the input class. Handles taking in input and processing it. How GUI tho?
import customtkinter as ctk

class TimerInput(ctk.CTkEntry):
    def __init__(self, parent) -> None:
        self.time_var = ctk.IntVar()
        super().__init__(parent, textvariable=self.time_var, placeholder_text="Enter time")

    def submit(self):
        self.input_time = self.time_var.get()
        print(f"Input was: {self.input_time}")
