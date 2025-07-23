import PIL
from PIL import Image
from PIL import ExifTags
import os.path
import math


def main(fileName):
    myImage = Image.open(fileName)

    width, height = myImage.size
    print("Largura: %dpx" % width)
    print("Altura: %dpx" % height)
    print("Formato: %s" % myImage.format)

    tags = myImage.getexif()

    for k,v in tags.items():
        print(str(ExifTags.TAGS[k])+" : "+str(v))

def main2(fileName):
    im = Image.open(fileName)
    for i in [1,10,20,30,43,50,60,70,80,90,100]:
        im.save(fileName + "-test-%i.jpg" % i, quality=i)

def main3(fileName):
    im = Image.open(fileName)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            r = p[0] & 0b10100000
            g = p[1] & 0b00001010
            b = p[2] & 0b00001010
            im.putpixel( (x,y), (r,g,b) )

    im.save(fileName+"-4bits.jpg")
    #add rgb num to pixel rgb to change the color of the entire image
    #check here
    #https://www.google.com/search?q=rgb+color+picker&sca_esv=d2276530c3132d30&sxsrf=AHTn8zrEu1HD00N22I4gD3vJWgGZ4mPZ7g%3A1747908366915&ei=DvcuaOnSN9Lp7_UPvbbHGQ&oq=rgb+color&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXJnYiBjb2xvcioCCAAyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyDRAAGIAEGLADGEMYigVIgglQAFgAcAF4AZABAJgBAKABAKoBALgBAcgBAJgCAaACBZgDAIgGAZAGCpIHATGgBwCyBwC4BwDCBwMyLTHIBwQ&sclient=gws-wiz-serp
def main4 (fileName):
    im = Image.open(fileName)
    width, height = im.size
    new_im = Image.new(im.mode, im.size)
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            r = p[0]
            g = p[2]
            b = p[1]
            new_im.putpixel((x,y), (r, g, b) )
    
    new_im.save(fileName + "-4bits.jpg")
    #im.save(fileName+"-4bits.jpg")

def main5(fileName):
    def effect_gray(im):
        width, height = im.size
        new_im = Image.new("L", im.size)
        for x in range(width):
            for y in range(height):
                p = im.getpixel( (x,y) )
                l = int(p[0]*0.299 + p[1]*0.587 + p[2]*0.144)
                new_im.putpixel( (x,y), (l) )
        return new_im
    im = Image.open(fileName)
    new_im = effect_gray(im)
    new_im.save(fileName + "-4bits.jpg")

def main6(fileName):
    
    def is_edge(im, x, y, diff, bw):
        width, height = im.size
        p = im.getpixel((x, y))

        if 0 < x < width - 1 and 0 < y < height - 1:
        # Check vertical neighbors
            for vy in [-1, 1]:
                px = im.getpixel((x, y + vy))
                if abs(p[0] - px[0]) > diff:
                    return (0, 0, 0) #(0, 128, 128)

        # Check horizontal neighbors
            for vx in [-1, 1]:
                px = im.getpixel((x + vx, y))
                if abs(p[0] - px[0]) > diff:
                    return (0, 0, 0) #(0, 128, 128)

        return (255, 128, 128) if bw else p  # Return edge pixel or original

    def process_image(fileName):
        im = Image.open(fileName).convert("RGB")
        width, height = im.size
        new_im = Image.new("RGB", (width, height))
        #important structure
        for x in range(width):
            for y in range(height):
                new_pixel = is_edge(im, x, y, diff=30, bw=1)
                new_im.putpixel((x, y), new_pixel)

        new_im.save(fileName + "-4bits.jpg")

# Example usage:
    process_image(fileName)
    
def main7(fileName):
    def get_factor(x, y, xref, yref, width, height):
        distance = math.sqrt(pow(x - xref, 2) + pow(y - yref, 2))
        max_distance = math.sqrt(pow(width, 2) + pow(height, 2))  # Max distance for scaling
        return (1 - (distance / max_distance))  # Convert to valid pixel intensity (0-255)

    def process_image(fileName):
        im = Image.open(fileName).convert("RGB")
        width, height = im.size
        new_im = Image.new("RGB", (width, height))

        for x in range(width):
            for y in range(height):
                intensity = get_factor(x, y, xref=width//2, yref=height//2, width=width, height=height)
                new_im.putpixel((x, y), (intensity, intensity, intensity))  # Apply grayscale effect

        output_name = fileName.rsplit(".", 1)[0] + "-processed.jpg"
        new_im.save(output_name)

# Example usage:
    process_image(fileName)
    
    
#mydir = os.getcwd()
#print(mydir)
#myFiles = os.walk(mydir)
#print(myFiles)
#i = 0
#for file in myFiles:
#    print(file)
#    if i == 1:
#      myfile = file[0] + "/" + file[2][0]
    
#"sala-jpeg-multiplas-streams/sala-original.JPG"
main5("Imagens-suporte/vasos.jpg")
main("Imagens-suporte/vasos.jpg")
