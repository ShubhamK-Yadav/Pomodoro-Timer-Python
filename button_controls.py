import customtkinter as ctk

class ButtonControls(ctk.CTkFrame):
    def __init__(self, parent, start_func=None, ) -> None:
        super().__init__(parent)
        self.start_func = start_func
        # Start/Pause Button
        self.start_button = ctk.CTkButton(
            self,
            command=self.submit,
            text=self.button_state(),
            height=55,
            width=160,
            font=("Segoe UI Semibold", 18),
            corner_radius=10
        )
        self.start_button.grid(row=3, column=0, columnspan=5, pady=(20, 10))

    def button_state(self):
        if self.start_func:
            return "Start"
        else:
            return "Pause"
