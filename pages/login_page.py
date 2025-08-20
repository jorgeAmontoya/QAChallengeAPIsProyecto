from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Sign In")

    def enter_Username(self,username:str):
        self.username_input.fill(username)

    def enter_password(self,password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.Click()

    def login(self, username:str, password:str):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()


