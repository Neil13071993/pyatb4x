from BrowserPackage.OpenBrowser import start_Browser
from BrowserPackage.CloseBrowser import close_Browser


def test_case():
    start_Browser()
    print("I am executing code TC1")
    close_Browser()

test_case()