#This is our list of imports
import qrcode
import argparse



#Define main argument parsing
parser = argparse.ArgumentParser(
        prog="QR Code Generator",
        description="This will make QR codes out of simple URL's",
        epilog="Created by YSSVirus")

#Define Arguments
parser.add_argument('-url', '--url', '-u', '--u', help="Website you want the URL to redirect to.")
parser.add_argument('-background', '--background', '-bg', '--bg', help="Background Color of the QR code (Normally white)")
parser.add_argument('-foreground', '--foreground', '-fg', '--fg', help="Foreground Color of the QRF code (Normally black)")
parser.add_argument('-file', '--file', '-f', '--f', help="Name of the file with no extension (Example: QR_Code)")

args = parser.parse_args()



if args.url is None:
        # Link for website
        Website = input("What website would you like attatched with the url?: ")
else:
        Website = args.url

if args.file is None:
        #This is where the filename gets assigned
        File_Name = input("What should the file name be? (No extension): ")
else:
        File_Name = args.file

if args.foreground is None:
        print()
        print("Example: white")
        print("if color not available will default to white")
        color_front = input("what should the foreground be? (Normally white): ")
else:
        color_front = args.foreground

if args.background is None:
        #Getting the optional color
        print()
        print("Example: black")
        print("if color not available will default to black")
        color_back = input("What should the backround be? (Normally black): ")
else:
        color_back = args.background



#This is where the .png attatchment gets added I had to add it through the variable. I still think that this was better to avoid confusion.
ext = ".png"
File = File_Name + ext

#This where the qr code physicly gets generated with our module
qr = qrcode.QRCode(#The following function is strictly about the size of the qr code
        version=1,
        box_size=10,
        border=5)

qr.add_data(Website) #This is where the url is assigned to the qr code
qr.make(fit=True)
img = qr.make_image(fill_color=color_front, back_color=color_back) #This is about the color of it

img.save(File)
