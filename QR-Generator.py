#This is our list of imports
from PIL import ImageTk, Image
from tkinter import Label, Tk, ttk, colorchooser
import tkinter as tk
import qrcode
import argparse
import os



#Define main argument parsing
arg_parser = argparse.ArgumentParser(
        prog="QR Code Generator",
        description="This will make QR codes out of simple URL's",
        epilog="Created by YSSVirus")

#Define Arguments
arg_parser.add_argument('-url', '--url', '-u', '--u', help="website you want the URL to redirect to.")
arg_parser.add_argument('-background', '--background', '-bg', '--bg', default="white" ,help="Background Color of the QR code (Normally white)")
arg_parser.add_argument('-foreground', '--foreground', '-fg', '--fg', default="black", help="Foreground Color of the QRF code (Normally black)")
arg_parser.add_argument('-file', '--file', '-f', '--f', help="Name of the file with no extension (Example: QR_Code)")
arg_parser.add_argument('-gui', '--gui', type=bool ,default=False, help="Use this or no commands at all to launch the GUI")

arg_items = arg_parser.parse_args()

def create_qr_code(website, file_fullname, color_front="black", color_back="white"):
        #This where the qr code physicly gets generated with our module
        qr = qrcode.QRCode(#The following function is strictly about the size of the qr code
                version=1,
                box_size=10,
                border=5)

        qr.add_data(website) #This is where the url is assigned to the qr code
        qr.make(fit=True)
        img = qr.make_image(fill_color=color_front, back_color=color_back) #This is about the color of it

        img.save(file_fullname)


def app_gui():
        global color_background
        global color_foreground
        global file_qr_code

        def action_picker_color_background():
                global color_background
                color_background_choice = colorchooser.askcolor(title = "Choose color")
                color_background = color_background_choice[1]
                print("background " + color_background)
        def action_picker_color_foreground():
                global color_foreground
                color_foreground_choice = colorchooser.askcolor(title = "Choose color")
                color_foreground = color_foreground_choice[1]
                print("foreground " + color_foreground)
                        
        def action_submit():
                global color_background
                global color_foreground
                global file_qr_code
                website_cleaned = website.get()
                file_name_cleaned = file_name.get()
                file_ext = ".png"
                file_fullname = file_name_cleaned + file_ext

                create_qr_code(website_cleaned, file_fullname, color_foreground, color_background)
                
                file_qr_code = ImageTk.PhotoImage(Image.open(file_fullname))
                label_image = Label(root, image = file_qr_code)
                label_image.grid(row=4, column=0)

        root = Tk()

        website = tk.StringVar()
        file_name = tk.StringVar()
        file_qr_code = ""
        color_background = "white"
        color_foreground = "black"

        frm = ttk.Frame(root, padding=10)

        button_quit = ttk.Button(frm, text="Quit", command=root.destroy)

        label_name = ttk.Label(root, text = 'File Name')
        input_name = ttk.Entry(root,textvariable = file_name, font=('calibre',10,'normal'))

        label_website = ttk.Label(root, text = 'website URL for QR Code')
        input_website = ttk.Entry(root,textvariable = website, font=('calibre',10,'normal'))

        label_color_background = ttk.Label(root, text = 'Background color for QR Code')
        button_color_background = ttk.Button(root, text = "Select color", command = action_picker_color_background)

        label_color_foreground = ttk.Label(root, text = 'Foreground color for QR Code')
        button_color_foreground = ttk.Button(root, text = "Select color", command = action_picker_color_foreground)

        button_submit = ttk.Button(root,text = "Create QR Code", command = action_submit)

        label_name.grid(row=0, column=0)
        input_name.grid(row=0, column=1)
        label_website.grid(row=1, column=0)
        input_website.grid(row=1, column=1)
        button_submit.grid(row=1, column=2)
        label_color_background.grid(row=2, column=0)
        button_color_background.grid(row=2, column=1)

        label_color_foreground.grid(row=3, column=0)
        button_color_foreground.grid(row=3, column=1)
        
        button_quit.grid(row=5, column=0)
        frm.grid()
        root.mainloop()

if arg_items.url is None and arg_items.file is None or arg_items.gui == True:
        # GUI Launch
        app_gui()
        exit()
else:
        # Command/Interactive
        if arg_items.url is None:
                # Link for website
                website = input("What website would you like attatched with the url?: ")
        else:
                website = arg_items.url
 
        if arg_items.file is None:
                #This is where the filename gets assigned
                file_name = input("What should the file name be? (No extension): ")
        else:
                file_name = arg_items.file

        create_qr_code(website, file_name, arg_items.foreground, arg_items.background)
