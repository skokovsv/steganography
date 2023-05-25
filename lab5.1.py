from PIL import Image

img = Image.open('D:\\img\\secret.png')

pixels = img.load()
s, w = img.size
k = 0
masb = ''
for i in range(s):
    for j in range(w):
        Pixels = pixels[i, j]
        #print(Pixels)
        #print(Pixels1)
        for h in range(3):
            pixel = bin(Pixels[h])[2:]
            #print(pixel)
            #print(pixel[len(pixel)-1])
            masb += pixel[len(pixel) - 1]
masB = [masb[i:i + 11] for i in range(0, len(masb), 11)]

Text = ""

for i in range(len(masB)):
    Text += chr(int(masB[i], 2))

k = 500

print(Text[0:k])

while (1):
    t = input("Показать больше?(y/n)")
    if t == "y":
        print(Text[k:k + 500])
        k += 500

    else:
        exit()