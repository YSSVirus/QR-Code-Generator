#This is our list of imports
import qrcode

# Link for website
Website = input("What website would you like attatched with the url?: ")
#Note for later I should make this dependant on the correct number of variables and if it doesnt have enough it goes through with only user input. I should also allow a -h argument for help
#This is where the filename gets assigned
File_Name = input("What should the file name be? (No extension): ")

#This is where the .png attatchment gets added I had to add it through the variable. I still think that this was better to avoid confusion.
PNG = ".png"
File = File_Name + PNG

#Getting the optional color
print()
print("Example: black")
print("if color not available will default to black")
color_back = input("What should the backround be? (Normally black): ")
print()
print("Example: white")
print("if color not available will default to white")
color_front = input("what should the foreground be? (Normally white): ")

#This where the qr code physicly gets generated with our module
qr = qrcode.QRCode(#The following function is strictly about the size of the qr code
        version=1,
        box_size=10,
        border=5)

qr.add_data(Website) #This is where the url is assigned to the qr code
qr.make(fit=True)
img = qr.make_image(fill_color=color_front, back_color=color_back) #This is about the color of it

img.save(File)
