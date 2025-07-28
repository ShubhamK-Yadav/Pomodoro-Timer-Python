import customtkinter as ctk
import display_timer

class ButtonControls(ctk.CTkFrame):
    def __init__(self, parent,  timer_logic=None, input_gui=None, timer_display= None) -> None:
        super().__init__(parent)
        self.timer_logic = timer_logic
        self.input_gui = input_gui
        self.timer_display = timer_display

        self.button_text = self.set_button_text()
        # Start/Pause Button
        self.start_button = ctk.CTkButton(
            self,
            command=self.submit,
            text=self.button_text,
            height=55,
            width=160,
            font=("Segoe UI Semibold", 18),
            corner_radius=10
        )
        self.start_button.grid(row=0, column=1, columnspan=5, pady=(20, 10))

    def set_button_text(self):
        timer_state = self.timer_logic.get_running_state()
        print(f"Timer state: {timer_state}")
        if timer_state:
            return "Pause"
        else:
            return "Start"

    def validation(self, hours, mins, secs) -> tuple[int, int, int]:
        if not (hours.isdigit() and mins.isdigit() and secs.isdigit()):
            self.error_label.configure(text="Please enter only numbers (0–59) in all fields.")
            return 0,0,0

        hours = int(hours)
        mins = int(mins)
        secs = int(secs)

        if not (0 <= mins <= 59 and 0 <=secs <=59):
            self.input_gui.error_label.configure(text="Minutes and seconds must be between 0 and 59.")
            return 0,0,0

        self.input_gui.error_label.configure(text="")

        return hours, mins, secs

    def submit(self) -> None:
        hours_input = self.input_gui.hours_entry.get()
        minutes_input = self.input_gui.minutes_entry.get()
        seconds_input = self.input_gui.seconds_entry.get()

        hours, mins, secs= self.validation(hours=hours_input,
                                                       mins=minutes_input,
                                                       secs=seconds_input)

        if (hours, mins, secs) != (0,0,0):
            self.timer_logic.set_time(hours=hours, minutes=mins, seconds=secs)
            self.change_state()
            self.start_button.configure(text=self.set_button_text())
        else:
            return

    def change_state(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        current_running_state = self.timer_logic.get_running_state()

        if not current_running_state:
            self.timer_logic.start_timer()
        else:
            self.timer_logic.pause_timer()

        self.start_button.configure(text=self.set_button_text())
        self.timer_display.start_countdown()
