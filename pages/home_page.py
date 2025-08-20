from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self,page:Page):
        self.page = Page
        self.upgrade_button = page.get_by_role("button", name="+ Add new project")

    def is_upgrade_button_vsible(self):
        expect(self.upgrade_button).is_visible()

