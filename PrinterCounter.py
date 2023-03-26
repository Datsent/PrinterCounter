from Utils import *
from DataFile import read_data, create_new_data
import os
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import date

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
            send_err_mail(line_list[3], line_list[1])
            quit()

def send_err_mail(ip_print, n_print):
    # Email details
    sender_email = SMTP_USER
    receiver_email = ADMIN_MAIL
    subject = 'No connection to Printer'
    body = ip_print + ' ' + n_print

    # Office 365 SMTP settings
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = SMTP_USER
    smtp_password = SMTP_PASS

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))
    '''
    # Add attachment to email
    with open("C:\\Users\\dima\\Desktop\\PrinterCounter\\Archive\\Printers_2023-02-27.csv", 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name="Printers_2023-02-27.csv")
        part['Content-Disposition'] = f'attachment; filename="Printers_2023-02-27.csv"'
        message.attach(part)
    '''
    # Create a SMTP session
    smtp_session = smtplib.SMTP(smtp_server, smtp_port)
    smtp_session.starttls()
    smtp_session.login(smtp_username, smtp_password)

    # Send the email
    smtp_session.sendmail(sender_email, receiver_email, message.as_string())

    # Close the SMTP session
    smtp_session.quit()

def send_mail():
    # Email details
    sender_email = SMTP_USER
    receiver_email = RECEIVER_MAIL
    subject = 'UNI Printer Count'
    body = "Printers Count File"

    # Office 365 SMTP settings
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = SMTP_USER
    smtp_password = SMTP_PASS

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['CC'] = ADMIN_MAIL
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Add attachment to email
    with open(USE_FILE_PATH, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=f"Printers_{str(date.today())}.csv")
        part['Content-Disposition'] = f'attachment; filename=f"Printers_{str(date.today())}.csv"'
        message.attach(part)

    # Create a SMTP session
    smtp_session = smtplib.SMTP(smtp_server, smtp_port)
    smtp_session.starttls()
    smtp_session.login(smtp_username, smtp_password)

    # Send the email
    smtp_session.sendmail(sender_email, [receiver_email, ADMIN_MAIL], message.as_string())

    # Close the SMTP session
    smtp_session.quit()

def myping(host):
    response = os.system("ping -n 1 " + host)

    if response == 0:
        print('True')
    else:
        print('False')

def check_file():
    with open(USE_FILE_PATH, 'r') as file:
        # Read all the lines in the file
        lines = file.readlines()

    # Search for the string in the lines
    search_string = 'N/A\n'
    for line in lines:
        if search_string in line:
            return False
    return True
def main():
    Lines = read_data(USE_FILE_PATH)
    check_ping(Lines)
    create_new_data(Lines)
    if check_file():
        send_mail()
    else:
        print('Wrong File')
        send_err_mail('See','File')

if __name__ == "__main__":
    main()
