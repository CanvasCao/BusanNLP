# coding:utf-8
import codecs
import jieba
import jieba.posseg as posseg

# 我理解的加载dict.txt的作用： load_userdict可以正确的判断分词金常务而不会被切割成 金-常务 且盛京不会被判断成人名nr
# dict.txt的nr是词性【人名】的意思
jieba.load_userdict('resource/dict.txt')
bfile = codecs.open('resource/busan.txt', "r", "utf8")

# 微信的文章说lineNames记录每一行出现的人名 我认为是个二维数组
lineNames = []
relationship = {}
while (True):
    line = bfile.readline()

    if (line == ''):
        break
    elif (line == '\r\n'):
        continue
    else:
        # print line
        wordArray = posseg.cut(line)

        # 每读一行就给lineNames加入一个数组
        lineNames.append([])
        for w in wordArray:
            if (w.flag == 'nr'):
                print w.word
                lineNames[-1].append(w.word)

for i in range(len(lineNames)):
    print '-'.join(lineNames[i])