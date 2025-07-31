import customtkinter as ctk

class Controls(ctk.CTkFrame):
    def __init__(self, parent,  timer_logic=None, input_gui=None, timer_display= None) -> None:
        super().__init__(parent, corner_radius=12, fg_color="#1f2937")
        self.timer_logic = timer_logic
        self.input_gui = input_gui
        self.timer_display = timer_display
        self.start_button_text = self._current_start_pause_text()
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="col")

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.grid(row=0, column=0, columnspan=6, sticky="we")
        btn_frame.grid_columnconfigure((0, 1), weight=1, uniform="btn")

        # Start/Pause Button
        self.start_button = ctk.CTkButton(
            btn_frame,
            command=self.on_start_pause,
            text=self.start_button_text,
            height=55,
            font=("Segoe UI Semibold", 17),
            corner_radius=10,
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )
        self.start_button.grid(row=0, column=0, padx=(0, 8), sticky="we")

        # Reset Button
        self.reset_button = ctk.CTkButton(
            btn_frame,
            command=self.on_reset,
            text="Reset",
            height=55,
            font=("Segoe UI Semibold", 17),
            corner_radius=10,
            fg_color="#374151",
            hover_color="#4b5563"
        )
        self.reset_button.grid(row=0, column=1, padx=(8, 0), sticky="we")

    def _current_start_pause_text(self) -> str:
        return "Pause" if self.timer_logic.get_running() else "Start"

    def validation(self, hours: int, minutes: int, seconds: int) -> tuple[int, int, int]:
        if not (hours.isdigit() and minutes.isdigit() and seconds.isdigit()):
            self.input_gui.error_label.configure(text="Please enter only numbers (0–59) in all fields.")
            return 0,0,0

        hours = int(hours)
        minutes= int(minutes)
        seconds = int(seconds)

        if not (0 <= minutes <= 59 and 0 <=seconds <=59):
            self.input_gui.error_label.configure(text="Minutes and seconds must be between 0 and 59.")
            return 0,0,0

        self.input_gui.error_label.configure(text="")

        return hours, minutes, seconds

    def handle_input(self) -> tuple[int, int, int]:
        hours_input = self.input_gui.hours_entry.get()
        minutes_input = self.input_gui.minutes_entry.get()
        seconds_input = self.input_gui.seconds_entry.get()

        hours, minutes, seconds= self.validation(hours=hours_input,
                                                       minutes=minutes_input,
                                                       seconds=seconds_input)
        return hours, minutes, seconds

    def on_reset(self) -> None:
        hours, minutes, seconds = self.handle_input()

        if (hours, minutes, seconds) == (0, 0, 0) and self.timer_logic.total_seconds == 0:
            return

        self.timer_logic.reset()
        self.start_button.configure(text=self._current_start_pause_text())
        if self.timer_display:
            self.after(0, self.timer_display.start_countdown)

    def on_start_pause(self) -> None:
        hours, minutes, seconds = self.handle_input()

        if (hours, minutes, seconds) == (0, 0, 0) and self.timer_logic.total_seconds == 0:
            return

        if not self.timer_logic.get_running() and self.timer_logic.total_seconds == 0:
            self.timer_logic.set_time(hours=hours, minutes=minutes, seconds=seconds)
            self.timer_logic.start_timer()
        elif not self.timer_logic.get_running():
            self.timer_logic.start_timer()
        else:
            self.timer_logic.pause_timer()

        self.start_button.configure(text=self._current_start_pause_text())
        if self.timer_display:
            self.after(0, self.timer_display.start_countdown)
