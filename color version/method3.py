from PIL import Image
import random
import sys
import numpy as np
import time

image1 = Image.open("hf1.jpg")
image1 = image1.convert('CMYK')

image2 = Image.open("hf2.jpg")
image2 = image2.convert('CMYK')

image3 = Image.open("hf3.jpg")
image3 = image3.convert('CMYK')

begin = time.time()

share1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])
share2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])

shareC1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])
shareC2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])
shareM1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])
shareM2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])
shareY1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])
shareY2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])

for x in range(0, image1.size[0]):
    for y in range(0, image1.size[1]):
        pixelcolor = image1.getpixel((x, y))
        C = pixelcolor[0]
        pixelcolor = image2.getpixel((x, y))
        M = pixelcolor[1]
        pixelcolor = image3.getpixel((x, y))
        Y = pixelcolor[2]

        # chanel C
        if C < 128:
            shareC1.putpixel((x * 2, y * 2), (0,0,0,0))
            shareC1.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
            shareC1.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
            shareC1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
            shareC2.putpixel((x * 2, y * 2), (0,0,0,0))
            shareC2.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
            shareC2.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
            shareC2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
        else:
            dice = random.randint(0, 1)
            if dice == 0:
                shareC1.putpixel((x * 2, y * 2), (0,0,0,0))
                shareC1.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
                shareC1.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
                shareC1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
                shareC2.putpixel((x * 2, y * 2), (255,0,0,0))
                shareC2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareC2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareC2.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))
            else:
                shareC1.putpixel((x * 2, y * 2), (255,0,0,0))
                shareC1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareC1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareC1.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))
                shareC2.putpixel((x * 2, y * 2), (0,0,0,0))
                shareC2.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
                shareC2.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
                shareC2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))


        # chanel M
        if M < 128:
            shareM1.putpixel((x * 2, y * 2), (0,0,0,0))
            shareM1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            shareM1.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
            shareM1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
            shareM2.putpixel((x * 2, y * 2), (0,0,0,0))
            shareM2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            shareM2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
            shareM2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
        else:
            dice = random.randint(0, 1)
            if dice == 0:
                shareM1.putpixel((x * 2, y * 2), (0,0,0,0))
                shareM1.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                shareM1.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                shareM1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
                shareM2.putpixel((x * 2, y * 2), (0,255,0,0))
                shareM2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareM2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareM2.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))
            else:
                shareM1.putpixel((x * 2, y * 2), (0,255,0,0))
                shareM1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareM1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareM1.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))
                shareM2.putpixel((x * 2, y * 2), (0,0,0,0))
                shareM2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                shareM2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                shareM2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
                
        # chanel Y
        if Y < 128:
            shareY1.putpixel((x * 2, y * 2), (0,0,0,0))
            shareY1.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
            shareY1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            shareY1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
            shareY2.putpixel((x * 2, y * 2), (0,0,0,0))
            shareY2.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
            shareY2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            shareY2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
        else:
            dice = random.randint(0, 1)
            if dice == 0:
                shareY1.putpixel((x * 2, y * 2), (0,0,0,0))
                shareY1.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                shareY1.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                shareY1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))
                shareY2.putpixel((x * 2, y * 2), (0,0,255,0))
                shareY2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareY2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareY2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))      
            else:
                shareY1.putpixel((x * 2, y * 2), (0,0,255,0))
                shareY1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                shareY1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                shareY1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))
                shareY2.putpixel((x * 2, y * 2), (0,0,0,0))
                shareY2.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                shareY2.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                shareY2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

        ## share1
        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC1.getpixel((x*2, y*2))[i]+shareM1.getpixel((x*2, y*2))[i]+shareY1.getpixel((x*2, y*2))[i])//3
        # share1.putpixel((x * 2, y * 2), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC1.getpixel((x*2+1, y*2))[i]+shareM1.getpixel((x*2+1, y*2))[i]+shareY1.getpixel((x*2+1, y*2))[i])//3
        # share1.putpixel((x*2+1, y*2), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC1.getpixel((x*2, y*2+1))[i]+shareM1.getpixel((x*2, y*2+1))[i]+shareY1.getpixel((x*2, y*2+1))[i])//3
        # share1.putpixel((x*2, y*2+1), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC1.getpixel((x*2+1, y*2+1))[i]+shareM1.getpixel((x*2+1, y*2+1))[i]+shareY1.getpixel((x*2+1, y*2+1))[i])//3
        # share1.putpixel((x*2+1, y*2+1), tuple(tmp))
for i in range(0, share1.size[0]):
    for j in range(0, share1.size[1]):
        C_new = shareC1.getpixel((i, j))[0]
        M_new = shareM1.getpixel((i, j))[1]
        Y_new = shareY1.getpixel((i, j))[2]
        share1.putpixel((i, j), (C_new,M_new,Y_new,0))

        ## share2
        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC2.getpixel((x*2, y*2))[i]+shareM2.getpixel((x*2, y*2))[i]+shareY2.getpixel((x*2, y*2))[i])//3
        # share2.putpixel((x*2, y*2), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC2.getpixel((x*2+1, y*2))[i]+shareM2.getpixel((x*2+1, y*2))[i]+shareY2.getpixel((x*2+1, y*2))[i])//3
        # share2.putpixel((x*2+1, y*2), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC2.getpixel((x*2, y*2+1))[i]+shareM2.getpixel((x*2, y*2+1))[i]+shareY2.getpixel((x*2, y*2+1))[i])//3
        # share2.putpixel((x*2, y*2+1), tuple(tmp))

        # tmp=[0,0,0,0]
        # for i in range(4):
        #     tmp[i]=(shareC2.getpixel((x*2+1, y*2+1))[i]+shareM2.getpixel((x*2+1, y*2+1))[i]+shareY2.getpixel((x*2+1, y*2+1))[i])//3
        # share2.putpixel((x*2+1, y*2+1), tuple(tmp))
for i in range(0, share2.size[0]):
    for j in range(0, share2.size[1]):
        C_new = shareC2.getpixel((i, j))[0]
        M_new = shareM2.getpixel((i, j))[1]
        Y_new = shareY2.getpixel((i, j))[2]
        share2.putpixel((i, j), (C_new,M_new,Y_new,0))

final = time.time()

print('Spend:', final-begin, 'secs.')

shareC1.save('shareC1.jpg')
shareC2.save('shareC2.jpg')
shareM1.save('shareM1.jpg')
shareM2.save('shareM2.jpg')
shareY1.save('shareY1.jpg')
shareY2.save('shareY2.jpg')
share1.save('method3_share1.jpg')
share2.save('method3_share2.jpg')