from selenium.webdriver.common.by import By


class SignUp_class:
    click_SignUp_XPATH = "//a[normalize-space()='Sign Up']"
    Text_Username_Xpath = "//input[@id='username']"
    Text_Email_Xpath = "//input[@id='email']"
    Text_Phone_Xpath = "//input[@id='phone']"
    Button_CreateUser_XPATH = "//button[@type='submit']"


    def __init__(self, driver):
        self.click_CreateUser_XPATH = None
        self.Text_Password_Xpath = None
        self.driver = driver

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.click_SignUp_XPATH).click()

    def enterusername(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_Xpath).send_keys(username)

    def enterpassword(self, Password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(Password)
    
    def enteremail(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(email)

    def enterphone(self, phone):
        self.driver.find_element(By.XPATH, self.Text_Phone_Xpath).send_keys(phone)

    def click_createuser_button(self):
        self.driver.find_element(By.XPATH, self.Button_CreateUser_XPATH).click()




