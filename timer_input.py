# Make this the input class. Handles taking in input and processing it. How GUI tho?
import customtkinter as ctk

class TimerInput(ctk.CTkFrame):
    def __init__(self, parent, callback_func=None) -> None:
        super().__init__(parent)
        self.callback_func = callback_func

        self.hours_var = ctk.StringVar(value="00")
        self.minutes_var = ctk.StringVar(value="00")
        self.seconds_var = ctk.StringVar(value="00")

        # Title Label
        title = ctk.CTkLabel(
            self,
            text="Pomodoro Timer",
            font=("Segoe UI Bold", 28)
        )
        title.grid(row=0, column=0, columnspan=5, pady=(0, 20))

        # Error label
        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="red",
            font=("Segoe UI", 14)
        )
        self.error_label.grid(row=1, column=0, columnspan=5, pady=(0, 10))

        # Time input fields
        time_font = ("Segoe UI", 28)
        entry_kwargs = {"height": 50, "width": 80, "font": time_font, "corner_radius": 8}

        self.hours_entry = ctk.CTkEntry(self, textvariable=self.hours_var, placeholder_text="HH", **entry_kwargs)
        self.hours_entry.grid(row=2, column=0, padx=(10, 5), pady=5)

        colon1 = ctk.CTkLabel(self, text=":", font=time_font)
        colon1.grid(row=2, column=1, padx=5)

        self.minutes_entry = ctk.CTkEntry(self, textvariable=self.minutes_var, placeholder_text="MM", **entry_kwargs)
        self.minutes_entry.grid(row=2, column=2, padx=5, pady=5)

        colon2 = ctk.CTkLabel(self, text=":", font=time_font)
        colon2.grid(row=2, column=3, padx=5)

        self.seconds_entry = ctk.CTkEntry(self, textvariable=self.seconds_var, placeholder_text="SS", **entry_kwargs)
        self.seconds_entry.grid(row=2, column=4, padx=(5, 10), pady=5)

        self.start_button = ctk.CTkButton(
            self,
            command=self.submit,
            text="Start",
            height=55,
            width=160,
            font=("Segoe UI Semibold", 18),
            corner_radius=10
        )
        self.start_button.grid(row=3, column=0, columnspan=5, pady=(20, 10))


    def submit(self) -> None:
        hours_input = self.hours_entry.get()
        minutes_input = self.minutes_entry.get()
        seconds_input = self.seconds_entry.get()

        hours, mins, secs= self.validation(hours=hours_input, mins=minutes_input, secs=seconds_input)

        if (hours, mins, secs) != (0,0,0):
            self.callback_func(hours, mins, secs)
        else:
            return

    def validation(self, hours, mins, secs) -> tuple[int, int, int]:
        if not (hours.isdigit() and mins.isdigit() and secs.isdigit()):
            self.error_label.configure(text="Please enter only numbers (0–59) in all fields.")
            return 0,0,0

        hours = int(hours)
        mins = int(mins)
        secs = int(secs)

        if not (0 <= mins <= 59 and 0 <=secs <=59):
            self.error_label.configure(text="Minutes and seconds must be between 0 and 59.")
            return 0,0,0

        self.error_label.configure(text="")

        return hours, mins, secs
    # Validation
    # 1. Time params (for hours, mins and secs)
    # 2. Validating the actual input with helpful messages.
    #
    # Passing the validated time to the display_timer
