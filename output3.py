from method3 import Y_new
from PIL import Image
import sys

infile1 = Image.open("method3_share1.jpg")
infile2 = Image.open("method3_share2.jpg")

outfile = Image.new('CMYK', infile1.size)

for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        C = (infile1.getpixel((x, y))[0]+infile2.getpixel((x, y))[0])
        M = (infile1.getpixel((x, y))[1]+infile2.getpixel((x, y))[1])
        Y = (infile1.getpixel((x, y))[2]+infile2.getpixel((x, y))[2])
        C_new = 0 if C < 255 else 255
        M_new = 0 if M < 255 else 255
        Y_new = 0 if Y < 255 else 255
        outfile.putpixel((x, y), (C,M,Y,0))

outfile.save("final3.jpg")

