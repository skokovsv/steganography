import matplotlib.pyplot as plt
import random
from PIL import Image

ip = Image.open('D:\\img\\orig.jpg')
pixels1 = ip.load()
s, w = ip.size

sum = s*w*3

m = []
for i in range(sum):
    m.append(random.randrange(256))

#p_new=0
#p_old=-1

for i in range(s):
    #p_new=100*i//s
    #print(p_new,"%")
    for j in range(w):
        l=3*(i*w+j)
        Pixels1 = pixels1[i, j]
        Pixel = []
        Pixel.append(Pixels1[0] ^ m[l])
        Pixel.append(Pixels1[1] ^ m[l+1])
        Pixel.append(Pixels1[2] ^ m[l+2])

        pixels1[i, j] = Pixel[0], Pixel[1], Pixel[2]



ip.save("D:\\img\\enc_gammir.png")
plt.imshow(ip)
plt.show()

ip1 = Image.open('D:\\img\\enc_gammir.png')
pixels2 = ip1.load()
s1, w1 = ip1.size

m1 = m


for i in range(s1):
    for j in range(w1):
        l1=3*(i*w1+j)
        Pixels2 = pixels2[i, j]
        Pixel = []
        Pixel.append(Pixels2[0] ^ m1[l1])
        Pixel.append(Pixels2[1] ^ m1[l1+1])
        Pixel.append(Pixels2[2] ^ m1[l1+2])

        pixels2[i, j] = Pixel[0], Pixel[1], Pixel[2]

ip1.save("D:\\img\\dec_gammir.png")
plt.imshow(ip1)
plt.show()
