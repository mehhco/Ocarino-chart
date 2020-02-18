import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# 对应关系：
# 0: 0      1: 1      2: 2     3: 3      4: 4       5: 5
# 6: 6      7: 7     8: '^1'    9: '5.'    10: '6.'    11: '7.'      12: '|'

def generate_chart(title1, list6):
    f = open(title1+"简谱",'a+')
    f.write(list6)
    f.close()
    colomn = 20
    list6 = list6.split(' ')
    list1 = []
    for i in list6:
        list1.append(int(i))


    n = int(len(list1) / colomn)
    n2 = len(list1) % colomn

    canvas_width = 210 * colomn + 200
    canvas_height = 210 * (n+2) + 1800
    img = np.zeros((canvas_height, canvas_width, 3), np.uint8)
    # 使用白色填充图片区域,默认为黑色
    img.fill(250)
    cv2.imwrite('hhc.jpg', img)

    # 使用Image module打开文件
    img2 = Image.open('hhc.jpg')
    # 设置图片参数
    title = title1
    instruction = ". ───> 低八度   ^ ───> 高八度  全按为5低八度 F调指法"
    font_face1 = ImageFont.truetype('C:/windows/fonts/STXINGKA.TTF', 80)
    font_face2 = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 30)
    font_color = (0, 0, 0)
    # 在canvas上写出曲名和注释
    draw = ImageDraw.Draw(img2)
    size1 = draw.textsize(title, font_face1)
    size2 = draw.textsize(instruction, font_face2)
    draw.text((int((canvas_width - size1[0]) / 2), 70), title, font_color, font_face1)
    draw.text((int(canvas_width - size2[0] - 15), 70), instruction, font_color, font_face2)
    # 生成文件名
    fig_file = []
    for i in range(13):
        str1 = 'C:/Users/huhai/Desktop/ocarina/fig' + str(i) + '.jpg'
        fig_file.append(str1)


    # 对应输入数字与乐谱数字
    kb_num2chart_num = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: '^1', 9: '5.', 10: '6.', 11: '7.', 12: '|'}
    # 输入数字与乐谱图标
    kb_num2pic_num = {}
    for i in range(13):
        png1 = cv2.imread(fig_file[i])
        png1 = cv2.resize(png1, (180, 95), Image.ANTIALIAS)  # 设置音符图片的大小
        cv2.imwrite('jpg' + str(i) + '.jpg', png1)
        kb_num2pic_num.__setitem__(i, 'jpg' + str(i) + '.jpg')

    # 输出对应的简谱数字和符号
    text = 0
    for i in range(n + 1):
        if i != n:
            for j in range(colomn):
                text += 1
                png = Image.open(kb_num2pic_num.get(list1[text - 1]))
                draw.text(((int(100 + 210 * (j % colomn))), int(200 + 210 * (i % n))),
                          str(kb_num2chart_num.get(list1[text - 1])),
                          fill=font_color, font=ImageFont.truetype('C:/windows/fonts/msyhbd.ttc', 60))
                img2.paste(png, [(int(40 + 210 * (j % colomn))), int(200 + 80 + 210 * (i % n))])
        else:
            for j in range(n2):
                text += 1
                png = Image.open(kb_num2pic_num.get(list1[text - 1]))
                draw.text(((int(100 + 210 * (j % colomn))), int(200 + 210 * n)),
                          str(kb_num2chart_num.get(list1[text - 1])),
                          fill=font_color, font=ImageFont.truetype('C:/windows/fonts/msyhbd.ttc', 60))
                img2.paste(png, [(int(40 + 210 * (j % colomn))), int(200 + 80 + 210 * n)])

    Image._show(img2)
    img2.save('C:/Users/huhai/Desktop/ocarina/chart of ' + title + '.jpg', quality=100)


title1 = input('Please insert the title of the song……')
list11 = input('please insert the corresponding number of musical note')
generate_chart(title1, list11)
