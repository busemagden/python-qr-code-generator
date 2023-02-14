# -*- coding: utf-8 -*-
"""python-qr-code-generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/busemagden/03abf9fa71c80e7529d38d6af7150704/python-qr-code-generator.ipynb
"""

pip install image



pip install qrcode

#Encoding Data into Quick Response Code (QR Code)
import qrcode
 
# Data to encode
data = input('Enter the Data: ')
 
version=int(input('Enter the version (complexity): '))  #maxvalue  15
box_size=int(input('Enter the Box size: '))  # max value 10
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version ,box_size,border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',back_color = 'white')
 
f=input("name it as: ")     #image name
 
img.save(f'{f}.png')
 
print('qr code generated and saved in the gallery')