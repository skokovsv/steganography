import matplotlib.pyplot as plt

from PIL import Image

ip1 = Image.open('D:\\bro.jpg')

ip2 = Image.open('D:\\qr.png')

pixels1 = ip1.load()
pixels2 = ip2.load()

s1, w1 = ip1.size
s2, w2 = ip2.size

s = min(s1, s2)
w = min(w1, w2)
p = 0.01

for i in range(s):
    for j in range(w):
        Pixels1 = pixels1[i, j]
        Pixels2 = pixels2[i, j]

        Pixel = []

        Pixel.append(int(Pixels1[0] * (1 - p) + Pixels2[0] * p))
        Pixel.append(int(Pixels1[1] * (1 - p) + Pixels2[1] * p))
        Pixel.append(int(Pixels1[2] * (1 - p) + Pixels2[2] * p))

        pixels1[i, j] = Pixel[0], Pixel[1], Pixel[2]

ip1.save("res.png")

plt.imshow(ip1)

plt.show()