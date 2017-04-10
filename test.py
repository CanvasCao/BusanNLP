# coding:utf-8

import codecs
import json
import jieba
import jieba.posseg as posseg



res=posseg.cut('呼唤')
for l in res:
    print l.word,l.flag