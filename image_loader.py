from PIL import Image
import customtkinter as ctk

class Image_Loader():
    def load_image(self, path: str) -> tuple[ctk.CTkImage, ctk.CTkImage]:
        im = Image.open(path)

        frame1 = im.crop((0,0,256,256))
        frame2 = im.crop((256,0,512,256))

        # ctk.CTkImage needed for the buttons
        ctk_play_btn1 = ctk.CTkImage(light_image=frame1, size=(128,128))
        ctk_play_btn2 = ctk.CTkImage(light_image=frame2, size=(128,128))
        return ctk_play_btn1, ctk_play_btn2
