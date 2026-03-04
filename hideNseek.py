import tkinter as tk
from tkinter import filedialog
import pil



class img():

    def __init__(self):
        self.path = self.getimg()

    def getimg(self):
        root = tk.Tk()
        root.withdraw()

        filepath = filedialog.askopenfilename(
            title="Select an image",
            filetypes= [("Image files","*.png *.jpg *.jpeg")])

        if filepath:
            print("File selected successfully.")

        else:
            print("File selection cancelled.")
        
        return filepath
