
class Input:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds
