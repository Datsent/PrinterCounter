import urllib.request
import ssl
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import tkinter
from tkinter import messagebox

def main():
    '''
    with open(os.path.join(sys.path[0], "Printers.txt"), "r") as file_printers:
        file_data = file_printers.read()
        file_splitted_lines = file_data.split("\n")
    for i in file_splitted_lines:
        if i.split(": ")[0] == "MFC-J5330DW":
            print(get_html_brother_pass(i.split(": ")[1]))
        elif i.split(": ")[0] == "WF-M5799":
            print(get_html_epson(i.split(": ")[1]))
        elif i.split(": ")[0] == "MFC-L2710DN" or i.split(": ")[0] == "MFC-L5750DW" or i.split(": ")[0] == "MFC-8950DW":
            print(get_html_brother(i.split(": ")[1]))
        else:
            print(get_html_samsung(i.split(": ")[1]))
    '''
    file_printers = open(os.path.join(sys.path[0], "Printers.csv"), "r")
    Lines = file_printers.readlines()
    new_list = ['#,Model,Serial,IP Adress,Supply Date,Begin Count,Last Count,Count,Total Pages\n']
    for line in Lines[1:]:
        line_list = line.split(',')
        print(f'Calculating Model: {line_list[1]}...')
        line_list[6] = line_list[7]
        try:
            line_list[7] = get_count(line_list[3], line_list[1] )
            line_list[8] = str(int(line_list[7]) - int(line_list[6])) + '\n'
            new_list.append(','.join(line_list))
        except BaseException:
            print(f"No connection with {line_list[3]}")
            line_list[7] = 'N/A'
            line_list[8] = 'N/A\n'
            new_list.append(','.join(line_list))
        print(f'Finished Model: {line_list[1]}...')
    file_printers.close()
    file = open(os.path.join(sys.path[0], f"Printers_{str(date.today())}.csv"), 'w')
    file.write(''.join(new_list))
    file.close()
    print('FINISHED')

def get_count(ip_adress, model):
    if 'brother' in model.lower():
        my_request = urllib.request.urlopen("http://%s/general/information.html?kind=item" % ip_adress)
        my_HTML = my_request.read().decode()
        if 'Counter' in my_HTML:
            return get_html_brother(ip_adress)
        else:
            return get_html_brother_pass(ip_adress)
    elif 'epson' in model.lower():
        return get_html_epson(ip_adress)
    elif 'samsung' in model.lower():
        return get_html_samsung(ip_adress)
    else:
        tkinter.messagebox.showerror(title=None, message=f'No plrogram for model {model}')

def get_html_brother (ip_adress):

    my_request = urllib.request.urlopen("http://%s/general/information.html?kind=item" %ip_adress )
    my_HTML = my_request.read().decode()
    return get_counter_brother(my_HTML)
def get_html_brother_pass(ip_adress):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    WebDriver = webdriver.Chrome()      #options=options
    WebDriver.get("http://%s/general/status.html" %ip_adress)
    WebDriver.find_element(By.ID,"LogBox").send_keys("initpass")
    WebDriver.find_element(By.ID, "LogBox").send_keys(Keys.RETURN)
    WebDriver.get("http://%s/general/information.html?kind=item" %ip_adress)
    my_HTML = WebDriver.page_source
    WebDriver.close()
    #get_counter_brother(my_HTML)
    return get_counter_brother(my_HTML)
def get_html_samsung(ip_adress):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    WebDriver = webdriver.Chrome(options=options)
    WebDriver.get("http://%s/sws/index.html" %ip_adress)
    time.sleep(5)
    WebDriver.find_element(By.ID, "Tab_Information").click()
    time.sleep(5)
    WebDriver.find_element(By.XPATH,
        '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/'
        'ul/div/li/ul/li[3]').click()
    time.sleep(2)
    html = WebDriver.page_source
    x = html.replace("x-grid3-cell-inner x-grid3-col-5", "xxx", 2).find("x-grid3-cell-inner x-grid3-col-5")
    y = html[x:].find("</div>")
    WebDriver.close()
    return html[x:x + y].split('">')[2]


def get_counter_brother(html):
    x = html.find("Counter")
    y = html[x:].find("</dd>")
    return html[x:x + y].split('</dt><dd>')[1]
def get_counter_epson(html):
    x = html.find("Total Number of Pages&nbsp")
    y = html[x:].find("</div>")
    return html[x:x + y].split('">')[2]
def get_html_epson(ip_adress):
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen("https://%s/PRESENTATION/ADVANCED/INFO_MENTINFO/TOP" %ip_adress,
                  context=context)
    my_HTML = res.read().decode()
    return get_counter_epson(my_HTML)

if __name__ == "__main__":
    main()
#get_html_brother('10.1.1.223')
#get_count_epson('10.1.1.122')