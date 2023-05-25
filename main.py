from PIL import Image
import numpy as np
#
def dvoich(s):
    l = []
    s1=""
    for i in s:
        d = ord(i)
        b = bin(d)
        c = b[2:]
        tmp = c[::-1]
        while len(tmp) < 7:
            tmp += '0'
        c = tmp[::-1]
        l.append(c)
        s1+=c

    #print(l)
    #print(s1)
    #print(len(s1))
    return s1


def dec(s1):
    res=" ".join(s1[i*7:i*7+7] for i in range(len(s1)//7))
    l=[]
    s=""
    new_l=[]
    l=res.split(" ")
    #print(l)
    for i in l:
        d=int(i,2)
        #c=chr(d)
        new_l.append(d)
    print(new_l)
    return new_l

def dec1(s1):
    res=" ".join(s1[i*7:i*7+7] for i in range(len(s1)//7))
    l=[]
    s=""
    new_l=[]
    l=res.split(" ")
    print(l)
    for i in l:
        d=int(i,2)
        c=chr(d)
        new_l.append(c)
    print(new_l)

s=input()
s1=dvoich(s)
#dec(s1)


image=Image.open('D:\cat.jpg')
size=width,heght=image.size
print(size)
#image.show()









# image.putpixel(coordinate,(255, 0, 0))
# print((image.getpixel(coordinate)))

# l=[1,2,3]
# s = tuple(l)
# print(s)
# image.putpixel(coordinate,s)
# print((image.getpixel(coordinate)))

# x=180
# y=69
# coordinate=x,y
coordinate=x,y,=180,69
pixel=image.getpixel(coordinate)
# print("pixel: ",image.getpixel(coordinate))
# print("pixel: ",bin(pixel[0])[2:],bin(pixel[1])[2:],bin(pixel[2])[2:])

count =0
i=0
new_l = []
while count<len(s1):
    #если i делится на 3 без остатка, то увеличиваем x y  и повторяем
    if count%3==0:
        if count!=0:
            sp = ''.join(new_l)
            val = dec(sp)
            t = tuple(val)
            image.putpixel(coordinate, t)
            print(f'val ={t}')
            x+=1
            y+=1
            new_l = []
            coordinate = x, y
            print(f'x={x} y={y}')
            pixel = image.getpixel(coordinate)
            print("pixel: ",image.getpixel(coordinate))
    if i>2:
        i=0

    l = []
    b = bin(pixel[0])[2:]
    l.append(b)
    b = bin(pixel[1])[2:]
    l.append(b)
    b = bin(pixel[2])[2:]
    l.append(b)
    print(f'l= {l}')
    tmp = l[i][::-1]
    while len(tmp) < 7:
        tmp += '0'
    l[i] = tmp[::-1]

    li = list(l[i])

    li[6] = s1[count]
    res = ''.join(li)
    new_l.append(res)
    count+=1
    i+=1
    #print(new_l)




print("Расшифровка------------------------------------------------------")
coordinate=x,y,=180,69

pixel=image.getpixel(coordinate)
count =0
i=0
seek=""
while count<len(s1):
    #если i делится на 3 без остатка, то увеличиваем x y  и повторяем
    if count%3==0:
        if count!=0:
            x+=1
            y+=1
            coordinate = x, y
            print(f'x={x} y={y}')
            pixel = image.getpixel(coordinate)
            print("pixel: ",image.getpixel(coordinate))
    if i>2:
        i=0

    l = []
    b = bin(pixel[0])[2:]
    l.append(b)
    b = bin(pixel[1])[2:]
    l.append(b)
    b = bin(pixel[2])[2:]
    l.append(b)
    print(f'l= {l}')

    new_l = []
    tmp = l[i][::-1]
    while len(tmp) < 7:
        tmp += '0'
    l[i] = tmp[::-1]

    li = list(l[i])
    seek+=li[6]
    count+=1
    i+=1
    #print(seek)
    #print(len(seek))

print(f'seek={seek}')
res=" ".join(seek[i*7:i*7+7] for i in range(len(seek)//7))
print(res)
l=res.split(" ")
print(l)
new_l=[]
for i in l:
    d = int(i, 2)
    c=chr(d)
    new_l.append(c)
print(new_l)
#dec1(seek)





