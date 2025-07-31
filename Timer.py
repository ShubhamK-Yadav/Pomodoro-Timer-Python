#!/usr/bin/env python3
import time as time
import datetime
from typing import Tuple

class Timer:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds
        self._duration = (hours * 3600) + (minutes * 60) + seconds
        self._running = False

    def start_timer(self) -> bool:
        self._running = True
        return self._running

    def pause_timer(self) -> bool:
        self._running = False
        return self._running

    def reset(self) -> None:
        self.total_seconds = self._duration
        self._running = False

    def done(self) -> None:
        self._completed = True

    def tick(self) -> bool:
        if self._running and self.total_seconds > 0:
            self.total_seconds -= 1

        elif self.total_seconds == 0:
            self._completed = True
            self._running = False
            return True

        return False

    def get_running(self) -> bool:
        return self._running

    def set_running(self, state: bool) -> None:
        self._running = state

    def get_time(self) -> Tuple[int, int]:
        return divmod(self.total_seconds, 60)

    def set_time(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds
        self._duration = (hours * 3600) + (minutes * 60) + seconds
        self._running = False

    def formatted_time(self) -> str:
        return str(datetime.timedelta(seconds=self.total_seconds))
