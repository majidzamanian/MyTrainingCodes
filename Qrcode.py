import qrcode
from os import path
from pyzbar.pyzbar import decode
from PIL import Image


def encode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=200,
        border=4,
    )
    x = input("your address or text: ")
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="black")
    img.save(x + ".png")


# decode part
def decode():
    y = input("your address or text for decode: ")
    if path.exists(y):
        result = decode(y)
        print(result)
    else:
        print("we dont have that file")


# the Q&A
s = "yes"

while s == "yes":
    Q = input("what do u want? encode or decode? \n")
    if Q == "encode":
        encode()
        s = input("do u want to repeat? yes or no ")
    elif Q == "decode":
        decode()
        s = input("do u want to repeat? yes or no ")
