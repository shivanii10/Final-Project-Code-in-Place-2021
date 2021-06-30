"""
This program implements a rad image filter.
"""
from simpleimage import SimpleImage
import random

DEFAULT_FILE = 'images/mt-rainier.jpg'

def main():

    filename = get_file()
    image = SimpleImage(filename)
    data(image)
    
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def codeInplace(image):
    for pixel in image:
        pixel.red=pixel.red*1.5
        pixel.blue=pixel.blue*1.5
        pixel.green=pixel.green*0.7
    return image

def grey(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg
        pixel.green=avg
        pixel.blue=avg
    return image

def red(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg*2
        pixel.green=avg*0.6
        pixel.blue=avg*0.6
    return image

def green(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg*0.1
        pixel.green=avg*1.4
        pixel.blue=avg*0.1
    return image

def classic_black(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg
        pixel.green=avg
        pixel.blue=avg*1.9
    return image

def violet(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg*0.9
        pixel.green=avg*0.1
        pixel.blue=avg*1.4
    return image

def blue(image):
    for pixel in image:
        avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=avg*0.2
        pixel.green=avg*0.9
        pixel.blue=avg*1.9
    return image

def yellow(image):
    for pixel in image:
        avg= avg=((pixel.red+pixel.blue+pixel.green)//3)
        pixel.red=pixel.red*1.3
        pixel.green=pixel.green*1.3
        pixel.blue=0
    return image


def pink(image):
    for pixel in image:
        pixel.red=pixel.red*1.8
        pixel.green=pixel.green*0.4
        pixel.blue=pixel.blue*1.3
    return image

def _random(image):
    patch = make_recolored_patch(random.random()*1.5,random.random()*1.5,random.random()*1.5)
    patch.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(DEFAULT_FILE)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.blue *= blue_scale
        pixel.green *= green_scale
    return patch

def data(image):
    print("\nhello!  Welcome to Code In place :)\n")
    while True:
        print("These are all the filters we have for you ..\n")
        print("1.codeInplace filter\t\t2.Pink filter")
        print("3.Red filter\t\t        4.Green filter")
        print("5.Yellow filter\t\t        6.Blue filter")
        print("7.Violet filter\t\t        8.Grey filter")
        print("9.Cold black filter\t\t10.Random filter\n")
        print("-------------------To exit write 0-------------------\n")
        choice=int(input("Tell the number and get the output:"))
        print()
        if choice!=0:
            image.show()
        if choice==1:
            image=codeInplace(image)
            image.show()
        if choice==2:
            image=pink(image)
            image.show()
        if choice==3:
            image=red(image)
            image.show()
        if choice==4:
            image=green(image)
            image.show()
        if choice==5:
            image=yellow(image)
            image.show()
        if choice==6:
            image=blue(image)
            image.show()
        if choice==7:
            image=violet(image)
            image.show()
        if choice==8:
            image=grey(image)
            image.show()
        if choice==9:
            image=classic_black(image)
            image.show()
        if choice==10:
            image=_random(image)
        if choice==0:
            break


if __name__ == '__main__':
    main()
