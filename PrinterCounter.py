from Utils import *
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
            messagebox.showerror('error', 'No connection to printer: ' + line_list[3])
            quit()


def myping(host):
    response = os.system("ping -n 1 " + host)

    if response == 0:
        print('True')
    else:
        print('False')
def main():
    Lines = read_data(USE_FILE_PATH)
    check_ping(Lines)
    create_new_data(Lines)

if __name__ == "__main__":
    main()
