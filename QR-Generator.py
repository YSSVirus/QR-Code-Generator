# Package Imports
from PIL import ImageTk, Image, ImageDraw
from tkinter import Label, Tk, ttk, colorchooser, filedialog
import tkinter as tk
import qrcode.image.styledpil as styledpil
import qrcode.image.styles.colormasks as colormasks
import qrcode.image.styles.moduledrawers as moduledrawers
import qrcode
import argparse
import os
from ttkbootstrap import Window
from ttkbootstrap.constants import *



# Initial Variable Definitions
global script_path
global color_pattern_path
global color_shape_path

script_dir = os.path.dirname(os.path.abspath(__file__))
if os.name == 'nt':
        script_path = script_dir + "\\"
        color_pattern_path = script_path + "images\\color_patterns\\"
        color_shape_path = script_path + "images\\shape_patterns\\"
else:
        script_path = script_dir + "/"
        color_pattern_path = script_path + "images/color_patterns/"
        color_shape_path = script_path + "images/shape_patterns/"

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
def create_qr_code(url, file_path_qr):
                
                qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, image_factory=styledpil.StyledPilImage)
                qr.add_data(url)
                qr.make(fit=True)
                
                # Prevent the library blending bug on pure black backgrounds
                render_bg = color_background
                if render_bg == (0, 0, 0):
                        render_bg = (1, 0, 0)
                
                if color_pattern_selected == "SolidFillColorMask":
                        color_mask = colormasks.SolidFillColorMask(back_color=render_bg, front_color=color_foreground)
                elif color_pattern_selected == "HorizontalGradiantColorMask":
                        color_mask = colormasks.HorizontalGradiantColorMask(back_color=render_bg, left_color=color_left, right_color=color_right)
                elif color_pattern_selected == "VerticalGradiantColorMask":
                        color_mask = colormasks.VerticalGradiantColorMask(back_color=render_bg, top_color=color_top, bottom_color=color_bottom)
                else:
                        color_mask = colormasks.RadialGradiantColorMask(back_color=render_bg, center_color=color_center, edge_color=color_edge)

                if image_center_path == None:
                        img = qr.make_image(color_mask=color_mask, module_drawer=shape_pattern_selected)
                else:
                        img = qr.make_image(color_mask=color_mask, module_drawer=shape_pattern_selected, embeded_image_path=image_center_path)

                img.save(file_path_qr)

def app_gui():
        global color_pattern_selected
        global shape_pattern_selected
        global color_background
        global color_foreground
        global color_top
        global color_bottom
        global color_left
        global color_right
        global color_center
        global color_edge
        global theme_mode
        global theme_icon
        global shape_pattern
        global image_center_path


        
        color_bottom = (255, 255, 255)
        color_left = (1, 0, 0)
        color_right = (255, 255, 255)
        color_center = (1, 0, 0)
        color_edge = (255, 255, 255)
        
        image_center_path = None
        
        color_pattern_selected = "SolidFillColorMask"
        root = Window(themename="darkly")

        website = tk.StringVar()
        file_name = tk.StringVar()

        shape_pattern_selected = moduledrawers.SquareModuleDrawer()
        
        options_list_color_pattern = {
            "Solid": (
                "SolidFillColorMask",
                "solid.png"
            ),
            "Radial Gradiant": (
                "RadialGradiantColorMask",
                "radial-gradiant.png"
            ),
            "Square Gradiant": (
                "RadialGradiantColorMask",
                "square-gradiant.png"
            ),
            "Horizontal Gradiant": (
                "HorizontalGradiantColorMask",
                "horizontal-gradiant.png"
            ),
            "Vertical Gradiant": (
                "VerticalGradiantColorMask",
                "vertical-gradiant.png"
            )
        }

        options_list_shape_pattern = {
            "Squares": (
                moduledrawers.SquareModuleDrawer(),
                "squares.png"
            ),
            "Small Squares": (
                moduledrawers.GappedSquareModuleDrawer(),
                "small-squares.png"
            ),
            "Rounded Squares": (
                moduledrawers.RoundedModuleDrawer(),
                "rounded_squares.png"
            ),
            "Circles": (
                moduledrawers.CircleModuleDrawer(),
                "circles.png"
            ),
            "Horizontal Bars": (
                moduledrawers.HorizontalBarsDrawer(),
                "horizontal-bars.png"
            ),
            "Vertical Bars": (
                moduledrawers.VerticalBarsDrawer(),
                "vertical-bars.png"
            )
        }

        options_color_pattern = list(options_list_color_pattern.keys())
        options_shape_pattern = list(options_list_shape_pattern.keys())



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
                color_background = (1, 0, 0)
                color_background_choice = colorchooser.askcolor(title = "Choose color")
                if color_background_choice[0]:
                        color_background = tuple(int(c) for c in color_background_choice[0])

        def action_picker_color_foreground():
                global color_foreground
                color_foreground = (255, 255, 255)
                color_foreground_choice = colorchooser.askcolor(title = "Choose color")
                if color_foreground_choice[0]:
                        color_foreground = tuple(int(c) for c in color_foreground_choice[0])

        def action_picker_color_top():
                global color_top
                color_top = (1, 0, 0)
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

        def action_select_image_prompt():
                def load_image(path, size=(50, 50)):
                    img = Image.open(path)
                    img.thumbnail(size)
                    return ImageTk.PhotoImage(img)
                global image_center_path
                image_center_path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
                center_image = load_image(image_center_path)
                label_center_image = Label(root, image = center_image)
                label_center_image.image = center_image
                label_center_image.grid(row=9, column=0, columnspan=3, pady=10)

        def create_pattern_image(file_path, text, size=(100, 100)):
                img = Image.open(file_path)
                img = img.resize(size, Image.Resampling.LANCZOS)
                draw = ImageDraw.Draw(img)
                width, height = img.size
                draw.rectangle([0, 0, width - 1, height - 1], outline="black")
                return ImageTk.PhotoImage(img)

        def on_select(item_name, item_image, mask_class_name, selection_type):
                global color_pattern_selected
                global shape_pattern_selected
                if selection_type == "pattern_color":
                        color_pattern_selected = mask_class_name
                        button_dropdown_color_pattern.config(text=f"  {item_name}", image=item_image)
                elif selection_type == "pattern_shape":
                        shape_pattern_selected = mask_class_name
                        button_dropdown_shape_pattern.config(text=f"  {item_name}", image=item_image)
                
                button_color_foreground.grid_forget()
                button_color_top.grid_forget()
                button_color_bottom.grid_forget()
                button_color_left.grid_forget()
                button_color_right.grid_forget()
                button_color_center.grid_forget()
                button_color_edge.grid_forget()
                label_pattern_choices.grid_forget()
                button_dropdown_color_pattern.grid_forget()
                button_dropdown_shape_pattern.grid_forget()
                button_center_image.grid_forget()

                if color_pattern_selected == "SolidFillColorMask":
                        button_color_foreground.grid(row=3, column=0, pady=10)
                        label_pattern_choices.grid(row=4, column=0, pady=10)
                        button_dropdown_color_pattern.grid(row=5, column=0, pady=10)
                        button_dropdown_shape_pattern.grid(row=6, column=0, pady=10)
                        button_center_image.grid(row=7, column=0, pady=10)
                elif color_pattern_selected == "HorizontalGradiantColorMask":
                        button_color_left.grid(row=3, column=0, pady=10)
                        button_color_right.grid(row=4, column=0, pady=10)
                        label_pattern_choices.grid(row=5, column=0, pady=10)
                        button_dropdown_color_pattern.grid(row=6, column=0, pady=10)
                        button_dropdown_shape_pattern.grid(row=7, column=0, pady=10)
                        button_center_image.grid(row=8, column=0, pady=10)
                elif color_pattern_selected == "VerticalGradiantColorMask":
                        button_color_top.grid(row=3, column=0, pady=10)
                        button_color_bottom.grid(row=4, column=0, pady=10)
                        label_pattern_choices.grid(row=5, column=0, pady=10)
                        button_dropdown_color_pattern.grid(row=6, column=0, pady=10)
                        button_dropdown_shape_pattern.grid(row=7, column=0, pady=10)
                        button_center_image.grid(row=8, column=0, pady=10)
                else:
                        button_color_center.grid(row=3, column=0, pady=10)
                        button_color_edge.grid(row=4, column=0, pady=10)
                        label_pattern_choices.grid(row=5, column=0, pady=10)
                        button_dropdown_color_pattern.grid(row=6, column=0, pady=10)
                        button_dropdown_shape_pattern.grid(row=7, column=0, pady=10)
                        button_center_image.grid(row=8, column=0, pady=10)
                                                
        def action_submit():
                global file_qr_code
                file_qr_code = ""
                website_cleaned = website.get()
                file_name_cleaned = file_name.get()
                file_ext = ".png"
                file_fullname = script_path + file_name_cleaned + file_ext

                if not website_cleaned:
                        win = tk.Toplevel(root)
                        win.title("ERROR!")
                        win.geometry("225x50")
                        win.resizable(False, False)
                        ttk.Label(win, text="A Url is REQUIRED!").pack(expand=True)
                        win.after(2500, win.destroy)
                        return
                
                create_qr_code(website_cleaned, file_fullname)
                file_qr_code = ImageTk.PhotoImage(Image.open(file_fullname).resize((350, 350)))
                label_image = Label(root, image = file_qr_code)
                label_image.grid(row=9, column=0, columnspan=5, pady=10)



        mask_color_pattern_mappings = {
            name: mask
            for name, (mask, _) in options_list_color_pattern.items()
        }
        mask_shape_pattern_mappings = {
            name: mask
            for name, (mask, _) in options_list_shape_pattern.items()
        }

        color_pattern = {
            name: create_pattern_image(
                color_pattern_path + image,
                mask
            )
            for name, (mask, image) in options_list_color_pattern.items()
        }
        shape_pattern = {
            name: create_pattern_image(
                color_shape_path + image,
                mask
            )
            for name, (mask, image) in options_list_shape_pattern.items()
        }


        root.title("QR Code Generator")
        frm = ttk.Frame(root, padding=10)
        theme_mode = "dark"
        theme_icon = "☀ Light Mode"

        

        label_required_fields = ttk.Label(root, text = "fields marked with * are REQUIRED", font=('calibre',8,'normal'))

        button_theme = tk.Button(root, text = theme_icon, command = action_toggle_theme)
        label_name = ttk.Label(root, text = 'File Name', font=('calibre',10,'normal'))
        input_name = ttk.Entry(root,textvariable = file_name, font=('calibre',10,'normal'))

        label_website = ttk.Label(root, text = '* Website URL or data for QR Code ', font=('calibre',10,'normal'))
        input_website = ttk.Entry(root,textvariable = website, font=('calibre',10,'normal'))

        label_color_choices = ttk.Label(root, text = 'Color Choices', font=('calibre',12,'normal'))
        button_color_background = ttk.Button(root, text = "Select Background color", command = action_picker_color_background)
        button_color_foreground = ttk.Button(root, text = "Select Foreground color", command = action_picker_color_foreground)
        button_color_top = ttk.Button(root, text = "Select Top color", command = action_picker_color_top)
        button_color_bottom = ttk.Button(root, text = "Select Bottom color", command = action_picker_color_bottom)
        button_color_left = ttk.Button(root, text = "Select Left color", command = action_picker_color_left)
        button_color_right = ttk.Button(root, text = "Select Right color", command = action_picker_color_right)
        button_color_center = ttk.Button(root, text = "Select Center color", command = action_picker_color_center)
        button_color_edge = ttk.Button(root, text = "Select Edge color", command = action_picker_color_edge)

        label_pattern_choices = ttk.Label(root, text = 'Pattern Choices', font=('calibre',12,'normal'))
        button_dropdown_color_pattern = tk.Menubutton(
                root, 
                text="Select a Pattern Color", 
                compound="left", 
                relief="raised"
        )

        dropdown_menu_color_pattern = tk.Menu(button_dropdown_color_pattern, tearoff=0)
        button_dropdown_color_pattern["menu"] = dropdown_menu_color_pattern

        for name in options_color_pattern:
                dropdown_menu_color_pattern.add_command(
                        label=name,
                        image=color_pattern[name],
                        compound="left",
                        command=lambda n=name: on_select(n, color_pattern[n], mask_color_pattern_mappings[n], "pattern_color")
                )

        button_dropdown_shape_pattern = tk.Menubutton(
                root, 
                text="Select a Pattern Shape ", 
                compound="left", 
                relief="raised"
        )

        dropdown_menu_shape_pattern = tk.Menu(button_dropdown_shape_pattern, tearoff=0)
        button_dropdown_shape_pattern["menu"] = dropdown_menu_shape_pattern

        for name in options_shape_pattern:
                dropdown_menu_shape_pattern.add_command(
                        label=name,
                        image=shape_pattern[name],
                        compound="left",
                        command=lambda n=name: on_select(n, shape_pattern[n], mask_shape_pattern_mappings[n], "pattern_shape")
                )



        button_center_image = tk.Button(root, text = "Select Center Image", command = action_select_image_prompt)

        button_submit = ttk.Button(root,text = "Create QR Code", command = action_submit)

        label_required_fields.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        button_theme.grid(row=0, column=4, pady=10, padx=10, sticky="e")

        label_name.grid(row=1, column=1, sticky="e")
        input_name.grid(row=1, column=2, sticky="ew", padx=(5, 10))

        label_website.grid(row=2, column=1, pady=10, sticky="e")
        input_website.grid(row=2, column=2, sticky="ew", padx=(5, 10))

        label_color_choices.grid(row=1, column=0, pady=10)

        button_color_background.grid(row=2, column=0)

        button_color_foreground.grid(row=3, column=0)

        label_pattern_choices.grid(row=4, column=0, pady=10)

        button_dropdown_color_pattern.grid(row=5, column=0, pady=10)

        button_dropdown_shape_pattern.grid(row=6, column=0, pady=10)

        button_center_image.grid(row=7, column=0, pady=10)

        button_submit.grid(row=8, column=2, sticky="e", padx=(0, 10))

        root.columnconfigure(2, weight=1)
        root.columnconfigure(4, weight=2)
        root.rowconfigure(9, weight=1)

        frm.grid()
        root.resizable(True, True)
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
