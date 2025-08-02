from notifypy import Notify
import chime
import threading

class Notification():
    def __init__(self, title: str, text: str, desktop_notif: bool, play_sound: bool):
        self.notif_title = title
        self.notif_text = text
        chime.theme('zelda')
        self.desktop_notif_flag = desktop_notif
        self.play_sound_flag = play_sound

    def desktop_notif(self):
        if not self.desktop_notif_flag:
            return
        try:
            notification = Notify()
            notification.title = self.notif_title
            notification.message = self.notif_text
            notification.send()
        except Exception as e:
            print(f"[Notification] Desktop notification failed: {e}")

    def play_sound_notif(self):
        if not self.play_sound_flag:
            return
        try:
            threading.Thread(target=chime.success, daemon=True).start()
        except Exception as e:
            print(f"[Notification] Failed to play sound {e}")

    def notify(self):
        self.desktop_notif()
        self.play_sound_notif()
