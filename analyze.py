# coding:utf-8

import codecs
import json
import jieba
import jieba.posseg as posseg

# 我理解的加载dict.txt的作用： load_userdict可以正确的判断分词金常务而不会被切割成 金-常务 且盛京不会被判断成人名nr
# dict.txt的nr是词性【人名】的意思
jieba.load_userdict('resource/dict.txt')
bfile = codecs.open('resource/busan.txt', "r", "utf8")

# 微信的文章说lineNames记录每一行出现的人名 我认为是个二维数组
lineNames = []
relationships = {}
# names{} 这里没有必要定义names对象 原文中names统计了所有人名出现的次数 对制作关系图没有帮助

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
            if (w.flag == 'nr' and len(w.word) >= 2):
                lineNames[-1].append(w.word)

# 打印lineNames的结果
# for i in range(len(lineNames)):
# print '-'.join(lineNames[i])

for line in lineNames:
    # 双层for循环
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships.get(name1) is None:
                relationships[name1] = {}

            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1


# !!仔细看json.石宇.尚华=61
# !!仔细看json.石宇.秀安=81
# 原文中的这两个关系的次数也是61和81 说明大部分的统计是写对了
print json.dumps(relationships, ensure_ascii=False, encoding='UTF-8')
