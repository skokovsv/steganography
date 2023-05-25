import matplotlib.pyplot as plt
from PIL import Image

ip2 = Image.open('D:\\img\with_znak.jpg')
ip1 = Image.open('D:\\img\\orig.jpg')

pixels1 = ip1.load()
pixels2 = ip2.load()

s1, w1 = ip1.size
s2, w2 = ip2.size

s = min(s1, s2)
w = min(w1, w2)

for i in range(s):
    for j in range(w):
        Pixels1 = pixels1[i, j]
        Pixels2 = pixels2[i, j]
        Pixel = []
        Pixel.append(int(Pixels1[0] - Pixels2[0]) * 200)
        Pixel.append(int(Pixels1[1] - Pixels2[1]) * 200)
        Pixel.append(int(Pixels1[2] - Pixels2[2]) * 200)

        pixels1[i, j] = Pixel[0], Pixel[1], Pixel[2]

ip1.save("qr.png")
plt.imshow(ip1)
plt.show()