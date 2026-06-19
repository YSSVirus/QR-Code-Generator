#This is our list of imports
import qrcode
import argparse
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import tkinter as tk



#Define main argument parsing
parser = argparse.ArgumentParser(
        prog="QR Code Generator",
        description="This will make QR codes out of simple URL's",
        epilog="Created by YSSVirus")

#Define Arguments
parser.add_argument('-url', '--url', '-u', '--u', help="Website you want the URL to redirect to.")
parser.add_argument('-background', '--background', '-bg', '--bg', default="white" ,help="Background Color of the QR code (Normally white)")
parser.add_argument('-foreground', '--foreground', '-fg', '--fg', default="black", help="Foreground Color of the QRF code (Normally black)")
parser.add_argument('-file', '--file', '-f', '--f', help="Name of the file with no extension (Example: QR_Code)")
parser.add_argument('-gui', '--gui', type=bool ,default=False, help="Use this or no commands at all to launch the GUI")

args = parser.parse_args()

def create_qr_code(Website, File_Name, color_front="black", color_back="white"):
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


def app_gui():
        var_background_color = "white"
        var_foreground_color = "black"
        def action_picker_color_background():
                global var_background_color
                var_background_color_messy = colorchooser.askcolor(title = "Choose color")
                var_background_color = var_background_color_messy[1]
                print("background " + var_background_color)
        def action_picker_color_foreground():
                global var_foreground_color
                var_foreground_color_messy = colorchooser.askcolor(title = "Choose color")
                var_foreground_color = var_foreground_color_messy[1]
                print("foreground " + var_foreground_color)
                        
        def action_submit():
                global var_background_color
                global var_foreground_color
                var_website_cleaned = var_website.get()
                var_name_cleaned = var_name.get()
                print("Website " + var_website_cleaned)
                print("name " + var_name_cleaned)
                print("foreground " + var_background_color)
                print("background " + var_foreground_color)


                create_qr_code(var_website_cleaned, var_name_cleaned, var_foreground_color, var_background_color)
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        var_website = tk.StringVar()
        var_name = tk.StringVar()

        button_quit = ttk.Button(frm, text="Quit", command=root.destroy)

        label_name = ttk.Label(root, text = 'File Name')
        input_name = ttk.Entry(root,textvariable = var_name, font=('calibre',10,'normal'))

        label_website = ttk.Label(root, text = 'Website URL for QR Code')
        input_website = ttk.Entry(root,textvariable = var_website, font=('calibre',10,'normal'))

        label_color_background = ttk.Label(root, text = 'Background color for QR Code')
        picker_color_background = ttk.Button(root, text = "Select color", command = action_picker_color_background)

        label_color_foreground = ttk.Label(root, text = 'Foreground color for QR Code')
        picker_color_foreground = ttk.Button(root, text = "Select color", command = action_picker_color_foreground)

        button_website = ttk.Button(root,text = "Create QR Code", command = action_submit)

        label_name.grid(row=0, column=0)
        input_name.grid(row=0, column=1)
        label_website.grid(row=1, column=0)
        input_website.grid(row=1, column=1)
        button_website.grid(row=1, column=2)
        label_color_background.grid(row=2, column=0)
        picker_color_background.grid(row=2, column=1)

        label_color_foreground.grid(row=3, column=0)
        picker_color_foreground.grid(row=3, column=1)
        
        button_quit.grid(row=4, column=0)
        frm.grid()
        root.mainloop()


if args.url is None and args.file is None or args.gui == True:
        # GUI Launch
        app_gui()
        exit()
else:
        # Command/Interactive
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

        create_qr_code(Website, File_Name, args.foreground, args.background)
