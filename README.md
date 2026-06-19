# QR_Code_Generator
This is a small Python3 QR code generator I made, it is just prompt based and will lead you through what information it needs.

This will create the QR image in the same directory it is launched from.

I have now added arguments for this with the prompts being backup.


## GUI Addition

I added a simple gui to this using tkinter so it should work by default with alot of systems, I will be improving the UI as time goes on.

<img width="448" height="501" alt="image" src="https://github.com/user-attachments/assets/7b695a23-1ca4-42dd-858b-eb015875d1c9" />



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
