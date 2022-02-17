from Utils import *
from DataFile import read_data, create_new_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, ssl, urllib.request


def main():
    Lines = read_data(USE_FILE_PATH)
    create_new_data(Lines)


'''def get_count(ip_adress, model):
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
        tkinter.messagebox.showerror(title=None, message=f'No plrogram for model {model}')'''

'''def get_html_brother (ip_adress):

    my_request = urllib.request.urlopen("http://%s/general/information.html?kind=item" %ip_adress )
    my_HTML = my_request.read().decode()
    return get_counter_brother(my_HTML)'''
'''def get_html_brother_pass(ip_adress):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    WebDriver = webdriver.Chrome(options=options)      #options=options
    WebDriver.get("http://%s/general/status.html" %ip_adress)
    WebDriver.find_element(By.ID,"LogBox").send_keys("initpass")
    WebDriver.find_element(By.ID, "LogBox").send_keys(Keys.RETURN)
    WebDriver.get("http://%s/general/information.html?kind=item" %ip_adress)
    my_HTML = WebDriver.page_source
    WebDriver.close()
    #get_counter_brother(my_HTML)
    return get_counter_brother(my_HTML)'''
'''def get_html_samsung(ip_adress):
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
    return html[x:x + y].split('">')[2]'''


'''def get_counter_brother(html):
    x = html.find("Counter")
    y = html[x:].find("</dd>")
    return html[x:x + y].split('</dt><dd>')[1]'''
'''def get_counter_epson(html):
    x = html.find("Total Number of Pages&nbsp")
    y = html[x:].find("</div>")
    return html[x:x + y].split('">')[2]
def get_html_epson(ip_adress):
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen("https://%s/PRESENTATION/ADVANCED/INFO_MENTINFO/TOP" %ip_adress,
                  context=context)
    my_HTML = res.read().decode()
    return get_counter_epson(my_HTML)'''

if __name__ == "__main__":
    main()
