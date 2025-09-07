import customtkinter as ctk

class TimerInput(ctk.CTkFrame):
    def __init__(self, parent, font_prop: str) -> None:
        super().__init__(parent, corner_radius=12, fg_color="transparent")
        # StringVars
        self.hours_var = ctk.StringVar(value="00")
        self.minutes_var = ctk.StringVar(value="00")
        self.seconds_var = ctk.StringVar(value="00")

        # Layout config
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="col")

        # Title
        title = ctk.CTkLabel(
            self,
            text="Pomodoro Timer",
            font=(font_prop, 48),
            anchor="center"
        )
        title.grid(row=0, column=0, columnspan=5, pady=(0, 12), sticky="we")

        # Error label (managed here but empty initially)
        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#f87171",
            font=(font_prop, 16),
            anchor="w"
        )
        self.error_label.grid(row=1, column=0, columnspan=5, sticky="we", pady=(0, 8))

        # Time inputs
        inputs_frame = ctk.CTkFrame(self, fg_color="transparent")
        inputs_frame.grid(row=2, column=0, columnspan=5, sticky="we")
        inputs_frame.grid_columnconfigure((0, 2, 4), weight=1)
        inputs_frame.grid_columnconfigure((1, 3), weight=0)

        time_font = (font_prop, 36)
        entry_kwargs = {
            "height": 50,
            "width": 80,
            "font": time_font,
            "corner_radius": 8,
            "justify": "center",
            "border_color": "white",
            "fg_color" : "#2b302e"
        }

        self.hours_entry = ctk.CTkEntry(
            inputs_frame,
            textvariable=self.hours_var,
            placeholder_text="HH",
            **entry_kwargs
        )
        self.hours_entry.grid(row=0, column=0, padx=(0, 4), pady=5, sticky="we")

        colon1 = ctk.CTkLabel(inputs_frame, text=":", font=time_font)
        colon1.grid(row=0, column=1, padx=2)

        self.minutes_entry = ctk.CTkEntry(
            inputs_frame,
            textvariable=self.minutes_var,
            placeholder_text="MM",
            **entry_kwargs
        )
        self.minutes_entry.grid(row=0, column=2, padx=4, pady=5, sticky="we")

        colon2 = ctk.CTkLabel(inputs_frame, text=":", font=time_font)
        colon2.grid(row=0, column=3, padx=2)

        self.seconds_entry = ctk.CTkEntry(
            inputs_frame,
            textvariable=self.seconds_var,
            placeholder_text="SS",
            **entry_kwargs)
        self.seconds_entry.grid(row=0, column=4, padx=(4, 0), pady=5, sticky="we")

        self.hours_entry.focus_set()
