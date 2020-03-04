from PIL import Image  
import os

filename = "royal-delivery.png"
im = Image.open(filename)

width, height = im.size  
 
newsize = (int(width/4), int(height/4))
im1 = im.resize(newsize)
im1.save(filename)