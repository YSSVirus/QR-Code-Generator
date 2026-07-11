# QR_Code_Generator
This is a small Python3 QR code generator I made, it is just prompt based and will lead you through what information it needs.

This will create the QR image in the same directory it is launched from.

I have now added arguments for this with the prompts being backup.


## GUI Addition

I added a simple gui to this using tkinter so it should work by default with alot of systems, I will be improving the UI as time goes on.

<img width="736" height="385" alt="image" src="https://github.com/user-attachments/assets/836a6cdf-1df5-4f1c-aeb9-d5aac1ae4e2c" />

<img width="775" height="967" alt="image" src="https://github.com/user-attachments/assets/418a3e1a-cc48-4ca4-8d97-89e2c9c24f3f" />




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
