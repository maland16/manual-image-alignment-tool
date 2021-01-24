from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog



def main():
    file_path = filedialog.askopenfilenames(title='Select images to align')

    print(file_path)

if __name__ == "__main__":
    main()