# Working with images in Python
# A lot of functionality
#Pip install pillow
# Docs at pillow.readthedocs.io 

from PIL import Image 
mac = Image.open('example.jpg')
type(mac)
mac.size
mac.filename
mac.format
#how to crop 
mac.crop(0,0,100,100)
pencils = Image.open('pencils.jpg')
pencils.size
# For Bottom Pencils

x = 0
y = 1100
w = 1950/3
h = 1300

pencils.crop((x,y,w,h))

mac 
mac.size (1993/1257)
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac.crop((x,y,w,h))

computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box(0,0))

mac.resize((3000,500)) # must be set in as a tuple

mac.rotate(90)

# Color Transparency
# RGBA - Red, Green, Blue, Alpha 255 = totally opaque 

red = Image.open(red_color.jpeg)
blue = Image.open(blue_color.png)

blue.putalpha(0) # This is completely transparent
blue.putalpha(128) # A lighter blue 

red.putalpha(128) # Almost pink

# Paste will put one image ontop of the other

blue.paste(im=red,box=(0,0),mask=red)
blue
# Output should be a purple box

blue.save("purple.png") # You can also add the full filepath before the file name
Purple = Image.open("purple.png")
Purple



