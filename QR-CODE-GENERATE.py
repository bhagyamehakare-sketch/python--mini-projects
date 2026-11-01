'''
we are going to use a python library like qrcode and convert url to qr code
'''
import qrcode
url=input("enter your url:")
filename=input("filename you want to save it as :")
if not(filename.endswith(".png")):
    filename=filename+".png"

img=qrcode.make(url)
img.save(filename)