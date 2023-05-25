from PIL import Image

im = Image.open('D:\\img\\secret.png')
pixels = im.load()
c = int(input("Количество использованных бит:"))
s, w = im.size
k = 0
masb = ''
for i in range(s):
    for j in range(w):
        Pixels = pixels[i, j]
        for h in range(3):
            pixel = bin(Pixels[h])[2:]
            masb += pixel[len(pixel)-c:]
masB = [masb[i:i+11] for i in range(0, len(masb), 11)]
Text = ""
for i in range(len(masB)):
    Text += chr(int(masB[i],2))

k = 500
print(Text[0:k])
