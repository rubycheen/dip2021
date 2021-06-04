from PIL import Image
import sys
import random

image1 = Image.open("hf1.jpg")
image1 = image1.convert('CMYK')

image2 = Image.open("hf2.jpg")
image2 = image2.convert('CMYK')

image3 = Image.open("hf3.jpg")
image3 = image3.convert('CMYK')


share1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])
share2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])


for x in range(0, image1.size[0]):
    for y in range(0, image1.size[1]):

        pixelcolor = image1.getpixel((x, y))
        C = pixelcolor[0]+pixelcolor[1]+pixelcolor[2]
        C = 0 if C==0 else 255
        pixelcolor = image2.getpixel((x, y))
        M = pixelcolor[0]+pixelcolor[1]+pixelcolor[2]
        M = 0 if M==0 else 255
        pixelcolor = image3.getpixel((x, y))
        Y = pixelcolor[0]+pixelcolor[1]+pixelcolor[2]
        Y = 0 if Y==0 else 255

        dice = random.randint(0, 1)

        if  dice == 0:
            share1.putpixel((x * 2, y * 2), (255,0,0,0))
            share1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            share1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            if C == 0 and M == 0 and Y == 0:
                share2.putpixel((x * 2, y * 2), (255,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 0 and Y == 0:
                share2.putpixel((x * 2, y * 2), (0,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))

            elif C == 0 and M == 255 and Y == 0:
                share2.putpixel((x * 2, y * 2), (255,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))

            elif C == 0 and M == 0 and Y == 255:
                share2.putpixel((x * 2, y * 2), (255,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))

            elif C == 255 and M == 255 and Y == 0:
                share2.putpixel((x * 2, y * 2), (0,255,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 0 and M == 255 and Y == 255:
                share2.putpixel((x * 2, y * 2), (255,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 0 and Y == 255:
                share2.putpixel((x * 2, y * 2), (0,0,255,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 255 and Y == 255:
                share2.putpixel((x * 2, y * 2), (0,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))
        
        else:
            share2.putpixel((x * 2, y * 2), (255,0,0,0))
            share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            share2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            if C == 0 and M == 0 and Y == 0:
                share1.putpixel((x * 2, y * 2), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 0 and Y == 0:
                share1.putpixel((x * 2, y * 2), (0,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))

            elif C == 0 and M == 255 and Y == 0:
                share1.putpixel((x * 2, y * 2), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))

            elif C == 0 and M == 0 and Y == 255:
                share1.putpixel((x * 2, y * 2), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))

            elif C == 255 and M == 255 and Y == 0:
                share1.putpixel((x * 2, y * 2), (0,255,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 0 and M == 255 and Y == 255:
                share1.putpixel((x * 2, y * 2), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 0 and Y == 255:
                share1.putpixel((x * 2, y * 2), (0,0,255,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            elif C == 255 and M == 255 and Y == 255:
                share1.putpixel((x * 2, y * 2), (0,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))


share1.save('method2_share1.jpg')
share2.save('method2_share2.jpg')
