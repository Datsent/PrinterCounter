from tkinter import messagebox
import tkinter
from Models import Brother, Epson, Samsung

def get_count(ip_adress, model):
    '''
    Call specific function to get data.
    '''
    if check_printer(model) == 'Brother':
        return Brother.brother(ip_adress)
    elif check_printer(model) == 'Epson':
        return Epson.epson(ip_adress)
    elif check_printer(model) == 'Sumsung':
        return Samsung.samsung(ip_adress)
    else:
        tkinter.messagebox.showerror(title=None, message=f'No program for model {model}')

def check_printer(model):
    '''
    Check kind\model of printer.
    '''
    if 'brother' in model.lower():
        return 'Brother'
    elif 'epson' in model.lower():
        return 'Epson'
    elif 'samsung' in model.lower():
        return 'Samsung'
    else:
        tkinter.messagebox.showerror(title=None, message=f'No program for model {model}')