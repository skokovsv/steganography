import shutil
def Text():
    x = input("Введите текст: ")
    x = x.encode('utf-8')
    shutil.copyfile('img1.jpg', 'img2.jpg')
    with open('img2.jpg', 'ab') as f:
        f.write(x)
    with open('img2.jpg', 'rb') as d:
        content = d.read()
        offset = content.index(bytes.fromhex('FFD9'))
        d.seek(offset + 2)
        g = d.read().decode('utf-8')
        print(g)
def File():
    shutil.copyfile('img1.jpg', 'img3.jpg')
    with open('img3.jpg', 'ab') as f, open('test.jpg', 'rb') as s:
        f.write(s.read())
    with open('img3.jpg', 'rb') as d:
        content = d.read()
        offset = content.index(bytes.fromhex('FFD9'))
        d.seek(offset + 2)
        with open('new.jpg', 'wb') as h:
            h.write(d.read())

l = int(input("Выберете текст 1 или файл 2: "))
if l == 1:
    Text()
elif l == 2:
    File()
else:
    print("Некорректный ввод")
