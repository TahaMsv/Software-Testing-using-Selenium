# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from ppretty import ppretty
from selenium.common.exceptions import TimeoutException


username_err = None
short_password_err = None
long_password_err = None
weak_password_err = None
verify_pass_err = None
email_err = None
verify_email_err = None

username_inp = None
email_inp = None
verify_email_inp = None
password_inp = None
verify_password_inp = None


class Form:
    def __init__(self, username, password, verify_password, email, verify_email):
        self.username = username
        self.password = password
        self.verify_password = verify_password
        self.email = email
        self.verify_email = verify_email


class Error:
    UsernameAlreadyTaken = "user name already taken"
    WeakPassword = "password must contain at least one capital letter, number and special character"
    ShortPassword = "password must be at least 8 characters"
    LongPassword = "password must be at most 64 characters"
    PasswordMismatch = "password doesn't match"
    InvalidEmail = "email is invalid"
    EmailMismatch = "email doesn't match"


def main():
    sr = Service('D:\\uniSource\\software testing\\project\\selenium\\chromedriver-win64\\chromedriver.exe')
    options = Options()
    options.binary_location = "C:\\Users\\Hosseintrz\\Downloads\\Compressed\\chrome-win64\\chrome-win64\\chrome.exe"
    driver = webdriver.Chrome(service=sr, options=options)
    driver.implicitly_wait(1)
    driver.get("https://monkeytype.com/login")

    loaded = WebDriverWait(driver, 10, 0.5). \
        until(
        lambda x: x.find_element(By.XPATH, '//html/body/div[8]/div/div[2]/div[2]/div[2]/div[1]').
        get_attribute("class").
        __contains__('active')
    )

    if loaded:
        print("page loaded successfully")

    cookie_acc = driver.find_element(By.XPATH, '//*[@id="cookiePopup"]/div[2]/div[2]/div[1]')
    cookie_acc.click()

    global username_inp, email_inp, verify_email_inp, password_inp, verify_password_inp
    register_elem = driver.find_element(By.CSS_SELECTOR, ".register.side")
    username_inp = register_elem.find_element(By.CLASS_NAME, "usernameInput")
    email_inp = register_elem.find_element(By.CLASS_NAME, "emailInput")
    verify_email_inp = register_elem.find_element(By.CLASS_NAME, "verifyEmailInput")
    password_inp = register_elem.find_element(By.CLASS_NAME, "passwordInput")
    verify_password_inp = register_elem.find_element(By.CLASS_NAME, "verifyPasswordInput")

    global username_err, short_password_err, long_password_err, weak_password_err, verify_pass_err, email_err, verify_email_err

    username_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[1]/div/div[3]/i')
    short_password_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[4]/div/div[2]/i')
    long_password_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[4]/div/div[3]/i')
    weak_password_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[4]/div/div[4]/i')
    verify_pass_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[5]/div/div[2]/i')
    email_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[2]/div/div[2]/i')
    verify_email_err = driver.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[3]/div/div[2]/i')

    test_cases = {
        Form("hossein", "Pass1234@", "Pass1234@", "hossein@gmail.com", "hossein@gmail.com"): Error.UsernameAlreadyTaken,
        Form("hosseintrz", "Pass1234@", "Pass5@", "hossein@gmail.com", "hossein@gmail.com"): Error.PasswordMismatch,
        Form("hosseintrz", "Pas34@", "Pas34@", "hossein@gmail.com", "hossein@gmail.com"): Error.ShortPassword,
        Form("hosseintrz", "Pass1234@"*10, "Pass1234@"*10, "hossein@gmail.com", "hossein@gmail.com"): Error.LongPassword,
        Form("hosseintrz", "pass12345", "pass12345", "hossein@gmail.com", "hossein@gmail.com"): Error.WeakPassword,
        Form("hosseintrz", "Pass1234@", "Pass1234@", "hossein", "hossein"): Error.InvalidEmail,
        Form("hosseintrz", "Pass1234@", "Pass1234@", "hossein@gmail.com", "hossein@yahoo.com"): Error.EmailMismatch,

    }

    for tc, expected in test_cases.items():
        username_inp.send_keys(tc.username)
        email_inp.send_keys(tc.email)
        verify_email_inp.send_keys(tc.verify_email)
        password_inp.send_keys(tc.password)
        verify_password_inp.send_keys(tc.verify_password)

        try:
            WebDriverWait(driver, 2, 0.25). \
                until(
                lambda x: not x.find_element(By.XPATH, '//*[@id="pageLogin"]/div[2]/form/div[6]').
                    get_attribute("class").
                    __contains__('disabled')
                )
        except TimeoutException:
            pass

        result = validate_form()
        print(ppretty(tc))
        print("expected: ", expected, " - actual : ", result)
        assert expected == result

        clear_form()

    print("closing driver")
    driver.close()


def clear_form():
    username_inp.clear()
    password_inp.clear()
    verify_password_inp.clear()
    email_inp.clear()
    verify_email_inp.clear()


def validate_form():
    if username_err.is_displayed():
        return Error.UsernameAlreadyTaken
    if short_password_err.is_displayed():
        return Error.ShortPassword
    if long_password_err.is_displayed():
        return Error.LongPassword
    if weak_password_err.is_displayed():
        return Error.WeakPassword
    if verify_pass_err.is_displayed():
        return Error.PasswordMismatch
    if email_err.is_displayed():
        return Error.InvalidEmail
    if verify_email_err.is_displayed():
        return Error.EmailMismatch
    else:
        return None


def has_child(elem):
    errors = elem.find_elements(By.XPATH, './*')
    print(errors)
    return len(errors) > 0


if __name__ == '__main__':
    main()
