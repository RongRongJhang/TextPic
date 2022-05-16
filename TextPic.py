from PIL import Image
import re

im = Image.open("test.jpg")
letters = '보라해'

#用正規表達式檢查文字是否為非英文
#中文簡體和繁體： ^[\u4E00-\u9FFF]+$
#日文平假名： ^[\u3040-\u309f]+$
#日文片假名： ^[\u30a0-\u30ff]+$
#韓文： ^[\uac00-\ud7ff]+$
re_words = re.compile(r'[\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7FF]+')
m = re_words.search(letters,0)

#im.save("V.png","png")

imRGB = im.convert('RGB')
imRgbPixels = imRGB.getdata()
imRgbPixelsList = list(imRgbPixels) #各像素點的rgb色碼

rows = im.size[0] #圖片寬度
cols = im.size[1] #圖片長度

f = open('test.html', 'w', encoding="utf-8")
f.write('<HTML>\n')
f.write('<style>\n')

if (m != None):
    f.write('pre {font-size:8pt; line-height:9pt; font-weight:bold;}\n')
else:
    f.write('pre {font-size:8pt; letter-spacing:4px; line-height:8pt; font-weight:bold;}\n')

f.write('</style>')
f.write('<pre>\n')

index = 0
letterIndex = 0
for i in range(0, cols):
    for j in range(0, rows):
        f.write('<span style="color:')
        rgb2hex = '#%02x%02x%02x' % imRgbPixelsList[index] #convert RGB color tuple to hex
        f.write(rgb2hex)
        f.write('">')
        f.write(letters[letterIndex])
        f.write('</span>')
        index += 1
        letterIndex += 1
        if letterIndex > len(letters)-1: letterIndex = 0
    f.write('\n')
f.write('</pre>\n')
f.write('</HTML>\n')
f.close()