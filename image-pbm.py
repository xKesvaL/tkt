from random import randint
from PIL import Image, ImageOps
import numpy as np

def matrix(w,h):
    m = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        b = True
        for j in range(w): 
            if (j)%20 == 0:
                if b == True:
                    b = False
                else: 
                    b = True
            m[i][j] = 0 if b == True else 1
    return m

def getMatrixFromFile(fileName):
    f = open(f"{fileName}.pbm")
    l = f.read().split("\n")
    f.close()
    m = [[0 for j in range(int(l[2].split(" ")[0]))] for i in range(int(l[2].split(" ")[1]))]
    l = l[3:]
    for i, line in enumerate(l):
        values = line.split()
        for j, val in enumerate(values):
            m[i][j] = val
    return m

def file(matrx, name):
    i = f"P1\n# Exercise image\n{str(len(matrx[0]))} {str(len(matrx))}\n"
    for l in matrx:
        for n in l:
            i += f"{str(n)} "
        i += "\n"
    f = open(f"{name}", "w")
    f.write(i)
    f.close()

def random(w, h):
    m = [[0 for j in range(w)] for i in range(h)]
    for i in range(h): # h is the image height
        b = True
        for j in range(w): # w is the image width
            m[i][j] = randint(0, 1)
    return m

def crypt(image, imageCle):
    m = [[0 for j in range(len(imageCle[0]))] for i in range(len(imageCle))]
    for i in range(len(imageCle)):
        for j in range(len(imageCle[0])):
            m[i][j] = image[i][j] ^ imageCle[i][j]
    return m

def convertImage(imageWithExt, imageToWrite):
    img = Image.open(imageWithExt) # Image used before in the year
    img0=img.convert("1")
    img0=ImageOps.invert(img0)

    na = np.array(img0)
    h,l=np.shape(na)
    np.savetxt(imageToWrite, na, fmt='%d',header="TNSI 2021-22")

    with open(imageToWrite,"r") as f:
        donnees=f.read()
        f.close()

    with open(imageToWrite,"w") as f:
        donnees="P1\n"+str(l)+" "+str(h)+"\n"+donnees
        f.write(donnees)
        f.close()


m1 = matrix(180, 240)
