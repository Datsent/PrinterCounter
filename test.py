from DataFile import read_data, create_new_data
import os
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('CD-Creator')
ws.geometry('300x200')
width = 300
height = 150
x = int(ws.winfo_screenwidth() / 2 - width / 2)
y = int(ws.winfo_screenheight() / 2 - height / 2)
ws.geometry("+{}+{}".format(x, y))
ws.config(bg='#5FB691')

def check_ping(lines):
    for line in lines[1:]:
        line_list = line.split(',')
        print(line_list[3])
        response = os.system("ping -n 1 " + line_list[3])
        if response == 0:
            print('True')
        else:
            return exit(-2)

def check_file():
    with open('Printers.csv', 'r') as file:
        # Read all the lines in the file
        lines = file.readlines()

    # Search for the string in the lines
    search_string = 'N/A\n'
    for line in lines:
        if search_string in line:
            return False
    return True
def main():
    Lines = read_data('Printers.csv')
    check_ping(Lines)
    create_new_data(Lines)
    if check_file():
        return exit(0)
    else:
        print('Wrong File')
        return exit(-1)

if __name__ == "__main__":
    main()
