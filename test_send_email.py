import send_email
mail = send_email.send_email(
    "swayamgavankar007@gmail.com",
    [
        "swayamgavankar007@gmail.com",
        "swayamgavankar007@gmail.com",
    ],
    "Test",
    "Test was successful",
)
# design.create_draft()
# _path = r"D:\Programming\Python\Python_Scripts\My_Design1_24.05.jpg"
# file = "My_Design1_24.05.jpg"

def test_create_draft():
    assert mail.create_draft() == True


def test_send():
    assert mail.send("swayam2008") == True
