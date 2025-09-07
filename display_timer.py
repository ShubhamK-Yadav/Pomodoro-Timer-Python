#!/usr/bin/env python3
import customtkinter as ctk

class TimerDisplay(ctk.CTkLabel):
    def __init__(self, parent, timer_logic, font_prop: str):
        self.timer = timer_logic
        super().__init__(
            parent,
            text=self.timer.formatted_time(),
            font=(font_prop, 48),
            fg_color="transparent"
        )
        self._is_running = False

    def start_countdown(self) -> None:
        if not self._is_running:
            self._is_running = True
            self.update_timer()

    def get_is_running(self) -> bool:
        return self._is_running

    def set_is_running(self, state: bool) -> None:
        self._is_running = state

    def update_timer(self) -> None:
        if self.timer.tick():
            print("Timer up!")
            self._is_running = False
        self.configure(text= self.timer.formatted_time())
        # Do not pass () with update_timer, only reference passed
        # Telling it what to call essentially instead of calling it right now
        self.after(1000, self.update_timer)
