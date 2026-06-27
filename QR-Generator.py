#This is our list of imports
from PIL import ImageTk, Image
from tkinter import Label, Tk, ttk, colorchooser
import tkinter as tk
import qrcode
import argparse
import os
from ttkbootstrap import Window
from ttkbootstrap.constants import *



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
        global theme_mode
        global theme_icon

        def action_toggle_theme():
                global theme_mode
                global theme_icon
                root.style.theme_use(
                        "litera" if root.style.theme.name == "darkly" else "darkly"
                )
                if theme_mode == "dark":
                        theme_mode = "light"
                        button_theme.config(text="☾")
                else:
                        theme_mode = "dark"
                        button_theme.config(text="☀")
                        pass

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

                if website_cleaned == "" or website_cleaned == None:
                        win = tk.Toplevel(root)
                        win.title("ERROR!")
                        win.geometry("225x50")
                        win.resizable(False, False)

                        ttk.Label(win, text="A Url is REQUIRED!").pack(expand=True)

                        win.after(2500, win.destroy)
                        return

                create_qr_code(website_cleaned, file_fullname, color_foreground, color_background)
                
                file_qr_code = ImageTk.PhotoImage(Image.open(file_fullname))
                label_image = Label(root, image = file_qr_code)
                label_image.grid(row=5, column=0)

        # Main App Variables and Assignments 
        root = Window(themename="darkly")
        website = tk.StringVar()
        file_name = tk.StringVar()
        file_qr_code = ""
        color_background = "white"
        color_foreground = "black"

        # Theme and Style
        root.title("QR Code Generator")
        frm = ttk.Frame(root, padding=10)
        theme_mode = "dark"
        theme_icon = "☀"


        # Inputs
        button_theme = ttk.Button(root, text = theme_icon, command = action_toggle_theme)

        label_name = ttk.Label(root, text = 'File Name')
        input_name = ttk.Entry(root,textvariable = file_name, font=('calibre',10,'normal'))

        label_website = ttk.Label(root, text = 'website URL for QR Code')
        input_website = ttk.Entry(root,textvariable = website, font=('calibre',10,'normal'))

        button_color_background = ttk.Button(root, text = "Select Background color", command = action_picker_color_background)
        button_color_foreground = ttk.Button(root, text = "Select Foreground color", command = action_picker_color_foreground)

        button_submit = ttk.Button(root,text = "Create QR Code", command = action_submit)


        # Build GUI
        button_theme.grid(row=0, column=2)
        label_name.grid(row=1, column=0)
        input_name.grid(row=1, column=1)
        label_website.grid(row=2, column=0)
        input_website.grid(row=2, column=1)
        button_color_background.grid(row=3, column=0)
        button_color_foreground.grid(row=3, column=1)
        button_submit.grid(row=4, column=1)

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