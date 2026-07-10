# Package Imports
from PIL import ImageTk, Image, ImageDraw
from tkinter import Label, Tk, ttk, colorchooser
import tkinter as tk
import qrcode.image.styledpil as styledpil
import qrcode.image.styles.colormasks as colormasks
import qrcode
import argparse
import os
from ttkbootstrap import Window
from ttkbootstrap.constants import *



# Initial Variable Definitions
arg_parser = argparse.ArgumentParser(
        prog="QR Code Generator",
        description="This will make QR codes out of simple URL's",
        epilog="Created by YSSVirus"
)

arg_parser.add_argument('-url', '--url', '-u', '--u', help="website you want the URL to redirect to.")
arg_parser.add_argument('-background', '--background', '-bg', '--bg', default="white" ,help="Background Color of the QR code (Normally white)")
arg_parser.add_argument('-foreground', '--foreground', '-fg', '--fg', default="black", help="Foreground Color of the QRF code (Normally black)")
arg_parser.add_argument('-file', '--file', '-f', '--f', help="Name of the file with no extension (Example: QR_Code)")
arg_parser.add_argument('-gui', '--gui', type=bool ,default=False, help="Use this or no commands at all to launch the GUI")

arg_items = arg_parser.parse_args()



# Core Functions
def create_qr_code(website, file_fullname, color_front=(255, 255, 255), color_back=(1, 0, 0), color_pattern_selected="SolidFillColorMask"):
        qr = qrcode.QRCode(
                error_correction=qrcode.ERROR_CORRECT_H,
                image_factory=styledpil.StyledPilImage
        )

        qr.add_data(website)
        qr.make(fit=True)
        
        if color_pattern_selected == "SolidFillColorMask":
                img = qr.make_image(color_mask=colormasks.SolidFillColorMask(back_color=color_back, front_color=color_front))
        elif color_pattern_selected == "HorizontalGradiantColorMask":
                img = qr.make_image(color_mask=colormasks.HorizontalGradiantColorMask(back_color=color_back, left_color=color_front, right_color=color_right))
        elif color_pattern_selected == "VerticalGradiantColorMask":
                img = qr.make_image(color_mask=colormasks.VerticalGradiantColorMask(back_color=color_back, top_color=color_front, bottom_color=color_bottom))
        else:
                img = qr.make_image(color_mask=colormasks.RadialGradiantColorMask(back_color=color_back, center_color=color_front, edge_color=color_edge))

        img.save(file_fullname)

def app_gui():
        global color_pattern_selected
        global color_background
        global color_foreground
        global color_top
        global color_bottom
        global color_left
        global color_right
        global color_center
        global color_edge
        global file_qr_code
        global theme_mode
        global theme_icon

        color_top = (1, 0, 0)
        color_bottom = (255, 255, 255)
        color_left = (1, 0, 0)
        color_right = (255, 255, 255)
        color_center = (1, 0, 0)
        color_edge = (255, 255, 255)

        def action_toggle_theme():
                global theme_mode
                global theme_icon
                root.style.theme_use(
                        "litera" if root.style.theme.name == "darkly" else "darkly"
                )
                if theme_mode == "dark":
                        theme_mode = "light"
                        button_theme.config(text="☾ Dark Mode")
                else:
                        theme_mode = "dark"
                        button_theme.config(text="☀ Light Mode")

        def action_picker_color_background():
                global color_background
                color_background_choice = colorchooser.askcolor(title = "Choose color")
                if color_background_choice[0]:
                        color_background = tuple(int(c) for c in color_background_choice[0])

        def action_picker_color_foreground():
                global color_foreground
                color_foreground_choice = colorchooser.askcolor(title = "Choose color")
                if color_foreground_choice[0]:
                        color_foreground = tuple(int(c) for c in color_foreground_choice[0])

        def action_picker_color_top():
                global color_top
                choice = colorchooser.askcolor(title="Choose Top Color")
                if choice[0]:
                        color_top = tuple(int(c) for c in choice[0])

        def action_picker_color_bottom():
                global color_bottom
                choice = colorchooser.askcolor(title="Choose Bottom Color")
                if choice[0]:
                        color_bottom = tuple(int(c) for c in choice[0])

        def action_picker_color_left():
                global color_left
                choice = colorchooser.askcolor(title="Choose Left Color")
                if choice[0]:
                        color_left = tuple(int(c) for c in choice[0])

        def action_picker_color_right():
                global color_right
                choice = colorchooser.askcolor(title="Choose Right Color")
                if choice[0]:
                        color_right = tuple(int(c) for c in choice[0])

        def action_picker_color_center():
                global color_center
                choice = colorchooser.askcolor(title="Choose Center Color")
                if choice[0]:
                        color_center = tuple(int(c) for c in choice[0])

        def action_picker_color_edge():
                global color_edge
                choice = colorchooser.askcolor(title="Choose Edge Color")
                if choice[0]:
                        color_edge = tuple(int(c) for c in choice[0])

        def create_color_pattern_image(file_fullname, text, size=(50, 50)):
                img = Image.open(file_fullname)
                img = img.resize(size, Image.Resampling.LANCZOS)
                draw = ImageDraw.Draw(img)
                width, height = img.size
                draw.rectangle([0, 0, width - 1, height - 1], outline="black")
                return ImageTk.PhotoImage(img)

        def on_select(item_name, item_image, mask_class_name):
                global color_pattern_selected
                color_pattern_selected = mask_class_name
                button_dropdown_color_pattern.config(text=f"  {item_name}", image=item_image)
                
                button_color_foreground.grid_forget()
                button_color_top.grid_forget()
                button_color_bottom.grid_forget()
                button_color_left.grid_forget()
                button_color_right.grid_forget()
                button_color_center.grid_forget()
                button_color_edge.grid_forget()

                if color_pattern_selected == "SolidFillColorMask":
                        button_color_foreground.grid(row=3, column=1)
                elif color_pattern_selected == "HorizontalGradiantColorMask":
                        button_color_left.grid(row=3, column=1)
                        button_color_right.grid(row=3, column=2)
                elif color_pattern_selected == "VerticalGradiantColorMask":
                        button_color_top.grid(row=3, column=1)
                        button_color_bottom.grid(row=3, column=2)
                else:
                        button_color_center.grid(row=3, column=1)
                        button_color_edge.grid(row=3, column=2)
                                                
        def action_submit():
                global color_background
                global color_foreground
                global color_pattern
                global file_qr_code
                
                website_cleaned = website.get()
                file_name_cleaned = file_name.get()
                file_ext = ".png"
                file_fullname = file_name_cleaned + file_ext

                if not website_cleaned:
                        win = tk.Toplevel(root)
                        win.title("ERROR!")
                        win.geometry("225x50")
                        win.resizable(False, False)
                        ttk.Label(win, text="A Url is REQUIRED!").pack(expand=True)
                        win.after(2500, win.destroy)
                        return

                qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, image_factory=styledpil.StyledPilImage)
                qr.add_data(website_cleaned)
                qr.make(fit=True)
                
                # Prevent the library blending bug on pure black backgrounds
                render_bg = color_background
                if render_bg == (0, 0, 0):
                        render_bg = (1, 0, 0)
                
                if color_pattern_selected == "SolidFillColorMask":
                        img = qr.make_image(color_mask=colormasks.SolidFillColorMask(back_color=render_bg, front_color=color_foreground))
                elif color_pattern_selected == "HorizontalGradiantColorMask":
                        img = qr.make_image(color_mask=colormasks.HorizontalGradiantColorMask(back_color=render_bg, left_color=color_left, right_color=color_right))
                elif color_pattern_selected == "VerticalGradiantColorMask":
                        img = qr.make_image(color_mask=colormasks.VerticalGradiantColorMask(back_color=render_bg, top_color=color_top, bottom_color=color_bottom))
                else:
                        img = qr.make_image(color_mask=colormasks.RadialGradiantColorMask(back_color=render_bg, center_color=color_center, edge_color=color_edge))

                img.save(file_fullname)
                
                file_qr_code = ImageTk.PhotoImage(Image.open(file_fullname))
                label_image = Label(root, image = file_qr_code)
                label_image.grid(row=6, column=0, columnspan=3, pady=10)

        root = Window(themename="darkly")
        website = tk.StringVar()
        file_name = tk.StringVar()
        file_qr_code = ""
        color_background = (1, 0, 0)
        color_foreground = (255, 255, 255)
        color_pattern_selected = "SolidFillColorMask"
        
        options = ["Solid", "Radial Gradiant", "Square Gradiant", "Horizontal Gradiant", "Vertical Gradiant"]
        
        mask_mappings = {
                "Solid": "SolidFillColorMask",
                "Radial Gradiant": "RadialGradiantColorMask",
                "Square Gradiant": "RadialGradiantColorMask",
                "Horizontal Gradiant": "HorizontalGradiantColorMask",
                "Vertical Gradiant": "VerticalGradiantColorMask"
        }

        color_pattern = {
                "Solid": create_color_pattern_image("images/color_patterns/pattern_solid_pattern.png", "SolidFillColorMask"),
                "Radial Gradiant": create_color_pattern_image("images/color_patterns/pattern_radial-gradiant.png", "RadialGradiantColorMask"),
                "Square Gradiant": create_color_pattern_image("images/color_patterns/pattern_square-gradiant.png", "RadialGradiantColorMask"),
                "Horizontal Gradiant": create_color_pattern_image("images/color_patterns/pattern_horizontal-gradiant.png", "HorizontalGradiantColorMask"),
                "Vertical Gradiant": create_color_pattern_image("images/color_patterns/pattern_vertical-gradiant.png", "VerticalGradiantColorMask")
        }

        root.title("QR Code Generator")
        frm = ttk.Frame(root, padding=10)
        theme_mode = "dark"
        theme_icon = "☀ Light Mode"

        button_theme = tk.Button(root, text = theme_icon, command = action_toggle_theme)
        label_name = ttk.Label(root, text = 'File Name')
        input_name = ttk.Entry(root,textvariable = file_name, font=('calibre',10,'normal'))

        label_website = ttk.Label(root, text = 'website URL for QR Code')
        input_website = ttk.Entry(root,textvariable = website, font=('calibre',10,'normal'))

        button_color_background = ttk.Button(root, text = "Select Background color", command = action_picker_color_background)
        button_color_foreground = ttk.Button(root, text = "Select Foreground color", command = action_picker_color_foreground)
        
        button_color_top = ttk.Button(root, text = "Select Top color", command = action_picker_color_top)
        button_color_bottom = ttk.Button(root, text = "Select Bottom color", command = action_picker_color_bottom)
        button_color_left = ttk.Button(root, text = "Select Left color", command = action_picker_color_left)
        button_color_right = ttk.Button(root, text = "Select Right color", command = action_picker_color_right)
        button_color_center = ttk.Button(root, text = "Select Center color", command = action_picker_color_center)
        button_color_edge = ttk.Button(root, text = "Select Edge color", command = action_picker_color_edge)

        button_dropdown_color_pattern = tk.Menubutton(
                root, 
                text="  Select a Color Pattern", 
                compound="left", 
                relief="raised"
        )

        dropdown_menu_color_pattern = tk.Menu(button_dropdown_color_pattern, tearoff=0)
        button_dropdown_color_pattern["menu"] = dropdown_menu_color_pattern

        for name in options:
                dropdown_menu_color_pattern.add_command(
                        label=name,
                        image=color_pattern[name],
                        compound="left",
                        command=lambda n=name: on_select(n, color_pattern[n], mask_mappings[n])
                )

        button_submit = ttk.Button(root,text = "Create QR Code", command = action_submit)

        button_theme.grid(row=0, column=2, pady=10)
        label_name.grid(row=1, column=0)
        input_name.grid(row=1, column=1)
        label_website.grid(row=2, column=0, pady=10)
        input_website.grid(row=2, column=1)
        button_color_background.grid(row=3, column=0)
        button_color_foreground.grid(row=3, column=1)
        button_dropdown_color_pattern.grid(row=4, column=0, pady=10)
        button_submit.grid(row=5, column=2)

        frm.grid()
        root.mainloop()



# GUI Wrapper
if (arg_items.url is None and arg_items.file is None) or arg_items.gui == True:
        app_gui()
        exit()
else:
        if arg_items.url is None:
                website = input("What website would you like attatched with the url?: ")
        else:
                website = arg_items.url
 
        if arg_items.file is None:
                file_name = input("What should the file name be? (No extension): ")
        else:
                file_name = arg_items.file

        create_qr_code(website, file_name)
