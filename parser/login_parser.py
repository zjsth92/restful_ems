from lxml import html

ERROR_BUTTON = "//div[@class='alert alert-dismissable alert-warning']/text()"
LOGIN_FAILED_ERROR = "Invalid email or password."

def parse(text):
    tree = html.fromstring(text)
    error_btn = tree.xpath(ERROR_BUTTON)
    if len(error_btn) > 0:
        error_text = error_btn[1].replace("\n", "")
        if error_text == LOGIN_FAILED_ERROR:
            return False

    return True