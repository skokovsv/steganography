from PIL import Image

im = Image.open('D:\\img\\orig.jpg')

text = input()
mas = ""

for i in text:
    mas1 = bin(ord(i))[2:]
    mas += "0" * (11 - len(mas1)) + mas1
if (len(mas) % 3 != 0):
    mas += "0"
    if (len(mas) % 3 != 0):
        mas += "0"

pixels = im.load()
s, w = im.size
k = 0
f = True

for i in range(s):
    if f:
        for j in range(w):
            if f:
                Pixels = pixels[i, j]
                Pixels1 = []
                for h in range(3):
                    pixel = bin(Pixels[h])[2:]
                    newPix = pixel[0:len(pixel) - 1] + mas[k]
                    Pixels1.append(int(newPix, 2))
                    k += 1
                    if (k == len(mas)):
                        f = False
                        break
                pixels[i, j] = Pixels1[0], Pixels1[1], Pixels1[2]

im.save('secret.png')