import PIL
from PIL import ImageTk, Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import time
import math

# This is the number of the first output photo
START_IMAGE_NUM = 114
x_offset = 0
y_offset = 0
scale_factor = 0
rotation = 0
next_image = False
unhandled_key_press = False

# This function gets called when, you guessed it, a key is pressed
def onKeyPress(event):
    global x_offset
    global y_offset
    global scale_factor
    global next_image
    global rotation

    if event.char == 'w':
        y_offset -= 10 # Up
    elif event.char == 's':
        y_offset += 10 # Down
    elif event.char == 'a':
        x_offset -= 10 # Left
    elif event.char == 'd':
        x_offset += 10 # Right
    elif event.char == 'i':
        y_offset -= 100 # Quite Up
    elif event.char == 'k':
        y_offset += 100 # Quite Down
    elif event.char == 'j':
        x_offset -= 100 # Quite Left
    elif event.char == 'l':
        x_offset += 100 # Hmm, Quite Right
    elif event.char == 'e':
        scale_factor += 1 # In
    elif event.char == 'q':
        scale_factor -= 1 # Out
    elif event.char == 'o':
        scale_factor += 5 # Quite In
    elif event.char == 'u':
        scale_factor -= 5 # Quite Out
    elif event.char == 'r':
        rotation += 90 
        if rotation >= 360:
            rotation = 0
    elif event.char == ' ':
        next_image = True 

    # Enforce minimum scale factor
    scale_factor = max(scale_factor, 10)

def main():
    # Set up the TKinter window
    window_dimensions = (1280,720)
    window = tk.Tk()
    window.title("Manual Image Alignment Tool")
    # I don't like this next line of code very much...
    window.geometry(str(window_dimensions[0])+"x"+str(window_dimensions[1]))
    window.configure(background='grey')

    # Set up a key press to trigger a callback
    window.bind('<KeyPress>', onKeyPress)

    # Ask the user to select images
    image_paths = filedialog.askopenfilenames(title='Select images to align...')

    # Super primative error checking
    if len(image_paths) < 2:
        exit("Error: Select at least two images")
    for path in image_paths:
        if (path[-4:] != ".jpg") & (path[-4:] != ".JPG"):
            print(path)
            exit("Error: Only .jpg is supported. Sorry :(")

    # Ask the user for a destination directory
    output_folder = filedialog.askdirectory(title='Select output folder...')

    # I don't know how variable context works in python...
    global x_offset
    global y_offset
    global scale_factor
    global rotation
    global next_image
    global unhandled_key_press

    # Loop through all the input images
    for image_num in range(len(image_paths)-1):
        if image_num == 0:
            # If first, pull from image path
            img1 = PIL.Image.open(image_paths[image_num]).convert("RGBA")
        else:
            # Otherwise pull the last image we made
            img1 = PIL.Image.open(output_folder+"/"+str(image_num + START_IMAGE_NUM)+".png")
        # Open the image to rescale
        img2 = PIL.Image.open(image_paths[image_num+1]).convert("RGBA")

        # reset modifiers
        x_offset = 0
        y_offset = 0
        scale_factor = 100
        rotation = 0
        next_image = False

        # While loop to line up the images. This loop just keeps printing the pictures with 
        # the set parameters while the user modifies the parameters using the keyboard 
        # (see onKeyPress above). The loop breaks when the user presses the keyboard
        while(not next_image):
            # copy the background image so we can do transparency
            temp_img1 = img1.copy()
            temp_img2 = img2.copy()
            # Scale both images to fit the window
            temp_img1 = temp_img1.resize(window_dimensions)
            
            # Scale 
            width, height = temp_img2.size
            width = math.floor(width * (scale_factor / 100))
            height = math.floor(height * (scale_factor / 100))
            temp_img2 = temp_img2.resize((width,height))
            
            # Rotate
            temp_img2 = temp_img2.rotate(rotation)

            # Create transparency (65%)
            paste_mask = temp_img2.split()[3].point(lambda i: i * 65 / 100.)
            # Paste the transparent image
            temp_img1.paste(temp_img2,(x_offset,y_offset),mask=paste_mask)
            # This magic prints the image to the window
            tk_image = ImageTk.PhotoImage(temp_img1)
            panel = tk.Label(window, image = tk_image)
            panel.pack(side = "top", fill = "both", expand = "yes")
            window.update()
            panel.pack_forget()

        # Save the adjusted image
        # Open a fresh backdrop
        backdrop = PIL.Image.open("backdrop.jpg").convert("RGBA")
        # Debug info (image parameters)
        print("Img #" + str(image_num + 1 + START_IMAGE_NUM) + ": Scale factor: "+str(scale_factor) +" x_off: "+str(x_offset) + " y_off: "+str(y_offset) + " rotation: " + str(rotation))

        # Scale 
        width, height = img2.size
        width = math.floor(width * (scale_factor / 100)) * 3
        height = math.floor(height * (scale_factor / 100)) * 3
        img2 = img2.resize((width,height))

        # Rotate
        img2 = img2.rotate(rotation)

        # Paste the current image on the backdrop with the chosen offset
        backdrop.paste( img2, (x_offset*3, y_offset*3), mask=img2) # ( 0, 0), mask=img2)
        #save the output image
        out_file = output_folder+"/"+str(image_num + 1 + START_IMAGE_NUM)+".png"
        backdrop.save(out_file,format = "png")

    # Once we break out of the image path loop we're done
    exit()

if __name__ == "__main__":
    main()