from PIL import Image

im = Image.open('D:\\img\\orig.jpg')

text =input("Введите текст: ")
mas = ""
for i in text:
    mas1 = bin(ord(i))[2:]
    mas +="0"* (11-len(mas1))+mas1

if(len(mas)%3!=0):
    mas +="0"
    if (len(mas) % 3 != 0):
        mas += "0"
pixels = im.load()
s,w=im.size

while(True):
    c = int(input("Введите количество битов (1-3):"))
    if c > 3:
        print(c,"больше 3!Введите заново")

    elif c < 1:
        print(c,"меньше 1. Попробуй еще раз.")
        continue
    else:
        break

if c==3:
    while len(mas)%9!=0:
        mas += "0"

k=0
f=True
for i in range(s):
    if f:
        for j in range(w):
            if f:
                Pixels = pixels[i,j]
                Pixels1=[]
                for h in range(3):
                    pixel = bin(Pixels[h])[2:]
                    newPix = pixel[0:len(pixel)-c]+mas[k:k+c]
                    Pixels1.append(int(newPix,2))
                    k+=c
                    if(k==len(mas)):
                        f=False
                        break
                pixels[i,j] = Pixels1[0],Pixels1[1],Pixels1[2]

im.save('secret.png')
