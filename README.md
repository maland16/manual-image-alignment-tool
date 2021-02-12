# Manual Image Alignment Tool
Easily resize/align/rotate muliple images to a standard 4K video resolution
## Why?
I built this program to allow me to easily create a timelapse video from a bunch (~300) of photos of my car I had taken over 2 years: 
[![Das Video](https://img.youtube.com/vi/1gZ3UAODakE/0.jpg)](https://www.youtube.com/watch?v=1gZ3UAODakE)

I was looking for a program that allowed me to overlay one translucent photo over another, align them, and export the aligned photo easily. I couldn't find a free program to do that, so I created this one.
## Disclaimer
I am an embedded firmware developer by trade, so python is really not my strong suit. This program is incredibly barebones, and probably would make a real python dev cry.
## What this program does
This program allows you to select a bunch of images (.jpg's only), align them one by one using the keyboard, and export them as 4K resolution frames (.png's only). 
## What this program does not do
Literally anything else.
## How to use
Set START_IMAGE_NUM to the file name of the first output image you'd like: {START_IMAGE_NUM}.jpg  
Create a seed image. This image must be 3840 by 2160 pixels (4K resolution), and is already aligned how you'd like.  
In my case this was a photo with my car in the center.  
When you run the program select this image and all the others you'd like to align, with the file names dictating the order.  
  For example my seed image was 0.jpg, and the next image in the sequence was 1.jpg, etc.  
Select an output folder.  
The program will load up the seed photo and overlay the first frame you'd like to align as a transparent layer.  
* For fine alignment, use W, A, S, D  
* For course alignment, use I, J, K, L  
* For fine scaling, use Q & E (out & in repsectively)  
* For course scaling, use U & O  
* To rotate, use R  
When you're done aligning the photo, use SPACE to save the aligned photo and load the next.  
That's it! When the program is out of photos, it will exit. The program saves the photo as soon as you move on to the next, so if you have to quit early or the program crashes your progress is (kinda) saved.
## Known Issues
* Perfomance degrades when you zoom really far in
