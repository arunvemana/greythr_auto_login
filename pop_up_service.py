from tkinter import *
# selenium script
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json


def alert_popup(title, message, path):
    """Generate a pop-up window to accept the login or cancel."""

    def chrome():
        """
        login and logout with selenium package.
        :return:
        """
        try:
            with open('data\\details.json', 'r') as f:
                data = json.load(f)
            browser = webdriver.Chrome(data['driver_path'])
            browser.get(data['url'])
        except EXCEPTION as e:
            print("failed to find details.json")

        delay = 2
        # try block for the home screen
        try:
            # with out wait functionality
            # username = browser.find_element_by_name("username")
            # password = browser.find_element_by_name("password")
            # login_button = browser.find_element_by_tag_name("button")
            username = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, "username")))
            password = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, "password")))
            login_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        except TimeoutException:
            print("taking too much time to load")
        username.click()
        username.send_keys(data['username'])
        password.click()
        password.send_keys(data['password'])
        login_button.click()
        delay = 4
        try:
            # with out delay
            # attendance = browser.find_element_by_link_text("Attendance")
            # signIn = browser.find_element_by_xpath('//*[@id="home-dashboard-3"]/section/div/div/div/div[1]/div/div[1]/div[3]')
            # logout = browser.find_element_by_class_name("empSignOut")

            # with delay
            attendance = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Attendance")))
            attendance.click()
            time.sleep(1)  # wait un-till time load
            signIn_singOut = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "markAttendancePanel")))
            logout = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "empSignOut")))
        except TimeoutException:
            print("taking too much time to load")
        # time.sleep(1)
        # signIn.click()
        signIn_singOut.click()
        time.sleep(4)
        logout.click()
        browser.close()
        root.destroy()

    root = Tk()
    root.title(title)
    w = 400  # popup window width
    h = 300  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="Login", command=chrome, width=10)
    b1 = Button(root, text="Holiday", command=quit, width=20)
    b.pack()
    b1.pack()

    mainloop()


# code excution
alert_popup("Reminder", "Don't forget to ", "login")
