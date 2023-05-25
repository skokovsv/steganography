import matplotlib.pyplot as plt
from PIL import Image

ip = Image.open('D:\\img\\orig.jpg')
pixels1 = ip.load()
s, w = ip.size
print("Введите текст: ")
a = input()
mass = []
for i in a:
    mass.append((ord(i)*30)%255)

sum = s*w*3
n = sum//len(mass)+1
k = mass*n

for i in range(s):
    for j in range(w):
        m=3*(i*w+j)
        Pixels1 = pixels1[i, j]
        Pixel = []
        Pixel.append((Pixels1[0] + k[m]) % 255)
        Pixel.append((Pixels1[1] + k[m+1]) % 255)
        Pixel.append((Pixels1[2] + k[m+2]) % 255)

        pixels1[i, j] = Pixel[0], Pixel[1], Pixel[2]


ip.save("D:\\img\\enc_img.png")
plt.imshow(ip)
plt.show()

ip1 = Image.open('D:\\img\\enc_img.png')
pixels2 = ip1.load()
s1, w1 = ip1.size
print("Введите текст: ")
a1 = input()
mass1 = []
for i in a1:
    mass1.append((ord(i)*30) % 255)

sum1 = s1 * w1 * 3
n1 = sum1//len(mass1) + 1
k1 = mass1 * n1

for i in range(s1):
    for j in range(w1):
        m1 = 3 * (i * w1 + j)
        Pixels1 = pixels2[i, j]
        Pixel = []
        Pixel.append((Pixels1[0] - k1[m1] + 255) % 255)
        Pixel.append((Pixels1[1] - k1[m1+1] + 255) % 255)
        Pixel.append((Pixels1[2] - k1[m1+2] + 255) % 255)

        pixels2[i, j] = Pixel[0], Pixel[1], Pixel[2]


ip1.save("D:\\img\\dec_img.png")
plt.imshow(ip1)
plt.show()
