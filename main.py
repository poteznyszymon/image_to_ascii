from PIL import Image, ImageOps
import sys

grey_chars = ['@  ','%  ', '#  ','*  ','+  ','"  ', '=  ', '-  ', ':  ','.  ']
grey_values = []

def turn_into_grey(image):
    return ImageOps.grayscale(image)


def get_pixel_greyscale(photo, width, height):
    for _ in range(width):
        grey_values.append([0] * height)
    
    for i in range(width):
        for j in range(height):
            pixel = photo.getpixel((i,j))
            grey_values[j][i] = pixel
            

def make_ascii(width, height):
    for i in range(width):
        for j in range(height):
            if grey_values[i][j] < 20:
                print(grey_chars[0], end='')
            elif grey_values[i][j] < 40:
                print(grey_chars[1], end='')
            elif grey_values[i][j] < 60:
                print(grey_chars[2], end='')
            elif grey_values[i][j] < 80:
                print(grey_chars[3], end='')
            elif grey_values[i][j] < 100:
                print(grey_chars[4], end='')
            elif grey_values[i][j] < 120:
                print(grey_chars[5], end='')
            elif grey_values[i][j] < 140:
                print(grey_chars[6], end='')
            elif grey_values[i][j] < 160:
                print(grey_chars[7], end='')
            elif grey_values[i][j] < 180:
                print(grey_chars[8], end='')
            else: print(grey_chars[9], end='')
        print('\n')


def main():
    if sys.argv[1] == 'konon':
        photo = Image.open('konon.jpg')
    elif sys.argv[1] == 'mona':
        photo = Image.open('mona.jpg')
    elif sys.argv[1] == 'jasper':
        photo = Image.open('jasper.jpg')
    elif sys.argv[1] == 'pudzian':
        photo = Image.open('pudzian.jpg')
    photo = turn_into_grey(photo)
    width = photo.size[0]
    height = photo.size[1]
    print(width, height)
    get_pixel_greyscale(photo,width,height)
    make_ascii(width, height)


if __name__=='__main__':
    main()