import send_email
from termcolor import colored, cprint


class tester:
    def __init__(self, condition, message):
        if condition is True:
            self.condition = True
        elif condition is False:
            self.condition = False
        self.message = message

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def printer(self):
        if self.condition is True:
            cprint(f"{self.message}: Passed", 'green')
        if self.condition is False:
            cprint(f"{self.message}: Failed", 'red')

mail=send_email.send_email(
    "swayamgavankar007@gmail.com",
    [
        "swayamgavankar007@gmail.com",
        "swayamgavankar007@gmail.com",
    ],
    "Test",
    "Test was successful",
)

test1=tester((mail.create_draft() is True), "Test 1")
test1.printer()

test2=tester((mail.send("swayam2008") is True), "Test 2")
test2.printer()
