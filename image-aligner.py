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

    if len(image_paths) < 2:
        exit("Error: Select at least two images")

    output_folder = filedialog.askdirectory(title='Select output folder')


    # for image_num in range(len(image_paths-1)):
    img1 = PIL.Image.open(image_paths[0]).convert("RGBA")
    img2 = PIL.Image.open(image_paths[1]).convert("RGBA")

    # reset modifiers
    x_offset = 0
    y_offset = 0
    scale_factor = 100
    
    # Open a fresh backdrop
    backdrop = PIL.Image.open("backdrop.jpg").convert("RGBA")
    # Paste the current image on the backdrop with the chosen offset
    backdrop.paste(imageObj,(x_offset,y_offset),imageObj)

    #save the output image
    out_file = output_folder+"/"+str(1)+".png"
    backdrop.save(out_file,format = "png")



    # edges = imageObj.filter(ImageFilter.FIND_EDGES)

    # img1 = ImageTk.PhotoImage(edges)
    # panel = tk.Label(window, image = img1)
    # panel.pack(side = "top", fill = "both", expand = "yes")
    # window.mainloop()

if __name__ == "__main__":
    main()