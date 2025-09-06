import customtkinter as ctk
from image_loader import Image_Loader as image_loader

class Controls(ctk.CTkFrame):
    def __init__(self, parent,  timer_logic=None, input_gui=None, timer_display= None) -> None:
        super().__init__(parent, corner_radius=12, fg_color="transparent")
        self.timer_logic = timer_logic
        self.input_gui = input_gui
        self.timer_display = timer_display
        self.start_button_text = self._current_start_pause_text()

        loader = image_loader()
        self.ctk_play_btn1, self.ctk_play_btn2 = loader.load_image("./assets/play_button.png")
        self.ctk_pause_btn1, self.ctk_pause_btn2 = loader.load_image("./assets/pause_button.png")
        self.ctk_reset_btn1, self.ctk_reset_btn2 = loader.load_image("./assets/Reset_button.png")

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="col")

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.grid(row=0, column=0, columnspan=6, sticky="we")
        btn_frame.grid_columnconfigure((0, 1), weight=1, uniform="btn")

        # Start/Pause Button
        self.start_button = ctk.CTkButton(
            btn_frame,
            image=self.ctk_play_btn1,
            text="",
            command=self.on_start_pause,
            fg_color="transparent",
            width=128,
            height=128,
            hover=False
        )
        self.start_button.bind("<Enter>", lambda e: self._handle_start_button_enter())
        self.start_button.bind("<Leave>", lambda e: self._handle_start_button_leave())

        self.start_button.grid(row=0, column=0, padx=(0, 8), sticky="we")

        # Reset Button
        self.reset_button = ctk.CTkButton(
            btn_frame,
            image=self.ctk_reset_btn1,
            command=self.on_reset,
            text="",
            fg_color="transparent",
            width=128,
            height=128,
            hover=False
        )
        self.reset_button.bind("<Enter>", lambda e: self._handle_reset_button_enter())
        self.reset_button.bind("<Leave>", lambda e: self._handle_reset_button_leave())

        self.reset_button.grid(row=0, column=1, padx=(8, 0), sticky="we")

    def _handle_start_button_enter(self) -> None:
        if self._current_start_pause_text() == "Start":
            self.start_button.configure(image=self.ctk_play_btn2)
        elif self._current_start_pause_text() == "Pause":
            self.start_button.configure(image=self.ctk_pause_btn2)

    def _handle_start_button_leave(self) -> None:
        if self._current_start_pause_text() == "Start":
            self.start_button.configure(image=self.ctk_play_btn1)
        elif self._current_start_pause_text() == "Pause":
            self.start_button.configure(image=self.ctk_pause_btn1)

    def _handle_reset_button_enter(self) -> None:
        self.reset_button.configure(image=self.ctk_reset_btn2)

    def _handle_reset_button_leave(self) -> None:
        self.reset_button.configure(image=self.ctk_reset_btn1)

    def _set_image_play_button(self) -> None:
        if self._current_start_pause_text() == "Start":
            self.start_button.configure(image=self.ctk_play_btn1)
        else:
            self.start_button.configure(image=self.ctk_pause_btn1)

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

        self.start_button.configure(image=self._set_image_play_button())
        if self.timer_display:
            self.after(0, self.timer_display.start_countdown)

    def on_reset(self) -> None:
        hours, minutes, seconds = self.handle_input()

        if (hours, minutes, seconds) == (0, 0, 0) and self.timer_logic.total_seconds == 0:
            return

        self.timer_logic.reset()
        self.start_button.configure(image=self._set_image_play_button())

        if self.timer_display:
            self.after(0, self.timer_display.start_countdown)
