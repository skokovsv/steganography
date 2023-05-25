import matplotlib.pyplot as plt
from PIL import Image

ip = Image.open('D:\\img\\orig.jpg')
pixels1 = ip.load()
s, w = ip.size
print("Введите 3 ключа сдвига: ")
a = int(input())
b = int(input())
c = int(input())

for i in range(s):
    for j in range(w):
        Pixels1 = pixels1[i, j]
        Pixel = []
        Pixel.append((Pixels1[0] + a) % 255)
        Pixel.append((Pixels1[1] + b) % 255)
        Pixel.append((Pixels1[2] + c) % 255)

        pixels1[i, j] = Pixel[0], Pixel[1], Pixel[2]


ip.save("D:\\img\\enc_img.png")
plt.imshow(ip)
plt.show()

ip1 = Image.open('D:\\img\\enc_img.png')
pixels2 = ip1.load()
s1, w1 = ip1.size
print("Введите 3 ключа сдвига")
a1 = int(input())
b1 = int(input())
c1 = int(input())

for i in range(s1):
    for j in range(w1):
        Pixels1 = pixels2[i, j]
        Pixel = []
        Pixel.append((Pixels1[0] - a + 255) % 255)
        Pixel.append((Pixels1[1] - b + 255) % 255)
        Pixel.append((Pixels1[2] - c + 255) % 255)

        pixels2[i, j] = Pixel[0], Pixel[1], Pixel[2]

ip1.save("D:\\img\\dec_img.png")
plt.imshow(ip1)
plt.show()
