import re
from playwright.async_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_page_search(page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    page.goto("http://128.85.27.33:3000")
    login_page.login("candidato_qa_01@gmail.com","Prueba1!")
    page.pause()
    home_page.is_upgrade_button_vsible()

    



