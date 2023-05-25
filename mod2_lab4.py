# import random
# import matplotlib.pyplot as plt
# from math import gcd
# from PIL import Image
#
# ip = Image.open("D:\\img\\orig.jpg")
# pixels = ip.load()
# w, h = ip.size
# print(w, h)
# a1 = random.randint(1, 1000)
# while (gcd(a1, 255) != 1):
#     a1 = random.randint(1, 1000)
# a2 = random.randint(1, 1000)
# while (gcd(a2, 255) != 1):
#     a1 = random.randint(1, 1000)
# b1 = random.randint(1, 1000)
# b2 = random.randint(1, 1000)
# while (b1 == b2):
#     b2 = random.randint(1, 1000)
#
# for i in range(w):
#     for j in range(h):
#         Pixels1 = pixels[i, j]
#         Pixels = []
#         Pixels.append((Pixels1[0] * a1 + b1) % 255)
#         Pixels.append((Pixels1[1] * a1 + b1) % 255)
#         Pixels.append((Pixels1[2] * a1 + b1) % 255)
#         print(Pixels)
#         pixels[i, j] = Pixels[0], Pixels[1], Pixels[2]
#
# for i in range(w):
#     for j in range(h):
#         Pixels1 = pixels[i, j]
#         Pixels = []
#         Pixels.append((Pixels1[0] * a2 + b2) % 255)
#         Pixels.append((Pixels1[2] * a2 + b2) % 255)
#         Pixels.append((Pixels1[1] * a2 + b2) % 255)
#         print(Pixels)
#         pixels[i, j] = Pixels[0], Pixels[1], Pixels[2]
#
# ip.save("D:\\img\\enc.jpg")
# plt.imshow(ip)
# plt.show()
# print(a1, a2, b1, b2)


from PIL import Image
import matplotlib.pyplot as plt

ip = Image.open("D:\\img\\enc.jpg")
pixels = ip.load()
w, h = ip.size
a1 = 673
a2 = 304
b1 = 465
b2 = 238

for i in range(w):
    for j in range(h):
        Pixels1 = pixels[i, j]
        Pixels = []
        Pixels.append(((Pixels1[0] - b2 + 255) * pow(a2, -1, 255)) % 255)
        Pixels.append(((Pixels1[1] - b2 + 255) * pow(a2, -1, 255)) % 255)
        Pixels.append(((Pixels1[2] - b2 + 255) * pow(a2, -1, 255)) % 255)
        print(Pixels)
        pixels[i, j] = Pixels[0], Pixels[1], Pixels[2]

for i in range(w):
    for j in range(h):
        Pixels1 = pixels[i, j]
        Pixels = []
        Pixels.append(((Pixels1[0] - b1 + 255) * pow(a1, -1, 255)) % 255)
        Pixels.append(((Pixels1[1] - b1 + 255) * pow(a1, -1, 255)) % 255)
        Pixels.append(((Pixels1[2] - b1 + 255) * pow(a1, -1, 255)) % 255)
        print(Pixels)
        pixels[i, j] = Pixels[0], Pixels[1], Pixels[2]
ip.save("D:\\img\\dec.jpg")
plt.imshow(ip)
plt.show()

