import PIL
from PIL import ImageTk, Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import time



def main():
    window = tk.Tk()
    window.title("Manual Image Alignment Tool")
    window.geometry("800x800")
    window.configure(background='grey')


    image_paths = filedialog.askopenfilenames(title='Select images to align')
    output_folder = filedialog.askdirectory(title='Select output folder')

    img1 = ImageTk.PhotoImage(PIL.Image.open(image_paths[0]))
    panel = tk.Label(window, image = img1)
    panel.pack(side = "top", fill = "both", expand = "yes")
    window.mainloop()

if __name__ == "__main__":
    main()