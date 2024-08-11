from Pageobjects.SignUp_Page import SignUp_class


class Test_BankApp_SignUp:
    def __init__(self):
        self.log = None

    def test_signup_001(self, setup):
        self.log.info("test_SignUp_001 testcase is started")
        self.driver = setup
        self.su = SignUp_class(self.driver)
        self.su.click_SignUp_XPATH()
        self.su.enterusername("Demo12345")
        self.su.enterpassword("Demo@12345")
        self.su.enteremail("Demo@credence.in")
        self.su.enterphone("9860279024")
        self.su.click_createuser_button()
        if self.driver.title == "Login":
            assert True
        else:
            assert False




