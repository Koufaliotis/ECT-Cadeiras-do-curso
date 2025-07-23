from PIL import Image
from PIL import ExifTags
import sys
import os.path

def PorcentageOfProcess(x,final):
    if x == int(final/4):
        print("25%")
    elif x == int(final/2):
        print("50%")
    elif x == int((final*3)/4):
        print("75%")
    elif x == final:
        print("100%")
    elif x == 0:
        print("1%")
def ImageData(file):
    myImage = Image.open(file)

    width , hight = myImage.size

    print(f" largura {width}")
    print(f"altura {hight}")

    tags = myImage._getexif() #doesnt work for every file tipe only on jpg
    for k ,v in tags.items():
        print(str(ExifTags.TAGS[k]) + " : " + str(v))

def imageFileCreator(fName):
    im = Image.open(fName)
    width, hight = im.size

    for x in [0.2,12]:
        dimencions = (int(width*x),int(hight*x))
        print(int(width*x),int(hight*x))
        new_im = im.resize(dimencions,Image.NEAREST)
        endfile = f"-Edited-ImageX {x}.jpg"
        new_im.save(fName + endfile)

def ImageBler(fname):
    im = Image.open(fname)
    for i in [1,10,20,30,40,50,60,70,80,90,100]:
        im.save(fname+f"-quality{i}.jpg",quality = i)

def ImageMode():
    myFileList = []
    myDir = os.getcwd()
    files = os.walk(myDir)
    for file in files:
        
        if file[0] == myDir +"/Imagens-suporte":
           myFileList = file[2]
        print(file[0])
    for imageFile in myFileList:
        im = Image.open("Imagens-suporte/"+imageFile)
        print(imageFile +": "+im.mode)
        

def PixelEditor():
    myFileList = []
    myDir = os.getcwd()
    files = os.walk(myDir)
    for file in files:
        
        if file[0] == myDir +"/Imagens-suporte":
           myFileList = file[2]
        print(file[0])
        
    for imageFile in myFileList:
        im = Image.open("Imagens-suporte/"+imageFile)
        
        print(imageFile +": "+im.mode)
        width , hight = im.size
        
        for x in range(width):
            PorcentageOfProcess(x,width)
            for y in range(hight):
                pixel = im.getpixel((x,y))
                if im.mode == "RGB":
                    r = pixel[1] & 0b10101000
                    g = pixel[0] & 0b01001010 
                    b = pixel[2] & 0b11110000
                    im.putpixel((x,y),(r,g,b))
                if im.mode == "RGBA":
                    r = pixel[0] & 0b01001010
                    g = pixel[1] & 0b10101000
                    b = pixel[2] & 0b11110000
                    im.putpixel((x,y),(r,g,b))
                if im.mode == "P":
                    p = pixel & 0b11110000
                    im.putpixel((x,y),(p))
                
        if im.mode == "RGB":
            im.save(imageFile + "-4bits.jpg")
        elif(im.mode == "P"):
            im.save(imageFile + "-4bits.gif")
        elif im.mode == "RGBA":
            im.save(imageFile + "-4bits.png")
        print("image saved")
def TonsDecinza():
    myFileList = []
    myDir = os.getcwd()
    files = os.walk(myDir)
    for file in files:
        
        if file[0] == myDir +"/Imagens-suporte":
           myFileList = file[2]
        print(file[0])
        
    for imageFile in myFileList:
        im = Image.open("Imagens-suporte/"+imageFile)
        new_im = im.convert("L")

        if im.mode == "RGB":
            new_im.save(imageFile + "-L.jpg")
        elif(im.mode == "P"):
            new_im.save(imageFile + "-L.gif")
        elif im.mode == "RGBA":
            new_im.save(imageFile + "-L.png")
        print("image saved")
def effect_gray(file):
    im =Image.open(file)
    width, height = im.size
    new_im = Image.new("L", im.size)
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            l = int(p[0]*0.299 + p[1]*0.537 + p[2]*0.144) #for high quality
            new_im.putpixel( (x,y), (l) )
    new_im.save("grayimage.jpeg")

def effect_intensity(imageFile, f):
    im =  Image.open(imageFile)
    new_im = im.convert("YCbCr")
    width, height = im.size
    for x in range(width):
        for y in range(height):
            p = new_im.getpixel( (x,y) )
            py = p[0]
            pb = min(255,int((p[1] - 128) * f) + 128)
            pr = min(255,int((p[2] - 128) * f) + 128)
            #py = min(255, int(pixel[0] * f))
            # [0] is the Y channel
            #new_im.putpixel( (x,y), (py, pixel[1], pixel[2]) )
            new_im.putpixel( (x,y),(py,pb,pr))
    new_im.save("brightImage.jpg")

def watermark(ImgeFile1,ImgeFile2,startx,starty,f):
    im1 = Image.open(ImgeFile1)
    im2 = Image.open(ImgeFile2)
    width, hight = im1.size
    
    for x in range(width):
        PorcentageOfProcess(x,width)
        for y in range(hight):
            try:
                p1 = im1.getpixel( (x+startx, y+starty) )
                p2 = im2.getpixel( (x,y) )
        
                r = int(p1[0]*(1-f)+p2[0]*f)
                g = int(p1[1]*(1-f)+p2[1]*f)
                b = int(p1[2]*(1-f)+p2[2]*f)

                im1.putpixel((x,y),(r,g,b))
            except:
                print("passed a pixel")
    im1.save("watermarkImage.jpg")

#ImageData("Imagens-suporte/southpark.png")
#imageFileCreator("Imagens-suporte/southpark.png")
#ImageBler("Imagens-suporte/southpark.png")
#ImageMode()
#PixelEditor()
#TonsDecinza()
#effect_gray("Imagens-suporte/flor.jpg")
effect_intensity("Imagens-suporte/flor.jpg",0.01) # limit 0 to 2 recomended
#watermark("Imagens-suporte/ua.jpg","sword.png",100,200,0.8)