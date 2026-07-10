# QR_Code_Generator
This is a small Python3 QR code generator I made, it is just prompt based and will lead you through what information it needs.

This will create the QR image in the same directory it is launched from.

I have now added arguments for this with the prompts being backup.


## GUI Addition

I added a simple gui to this using tkinter so it should work by default with alot of systems, I will be improving the UI as time goes on.

<img width="425" height="251" alt="image" src="https://github.com/user-attachments/assets/bb9b4c1a-4042-45bf-98f1-644e5ce9b5e9" />

<img width="428" height="669" alt="image" src="https://github.com/user-attachments/assets/d1020c3f-5349-4e1d-a2b7-6adefa0339e8" />




## Installation Commands
git clone https://github.com/YSSVirus/QR-Code-Generator.git

cd QR-Code-Generator

python -r requirments.txt


# Execution Commands
- Interactive Prompts

python QR-Generator.py

- Get Help

python QR-Generator.py --help

- Example with arguments

python QR_Code_Generator.py -url "https://ysslabs.com" -bg "black" -fg "white" -f "test"

- Launch GUI

python QR_Code_Generator.py
