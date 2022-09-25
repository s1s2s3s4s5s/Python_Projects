import qrcode

name = input("Enter qr-code name: ")
link = input("Enter qr-code link: ")

img = qrcode.make(f"{link}")
img.save(f"{name}.png")