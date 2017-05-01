# -*-coding:utf-8 -*-
import math
import requests
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf8')

argv='C:\Users\hasee\Desktop\zuoye\space tourist.txt'
oFilePath = 'C:/Users/hasee/Desktop/zuoye/'
filename = argv
f = open(filename,'r')                    #只读打开filename
file_read = f.read()                       #读取f，把所得内容传给file_read
f.close()
fen_list = jieba.cut(file_read,cut_all=True)   #将file_read的内容用结巴分词全部切开并传给fen_list
result = {}
for fen in fen_list:
    # sys.stdout.write(fen.encode('utf-8') + ',')
    fen = ' '.join(fen.split())                                #用空格连接切开的词赋给fen
    if(fen != ''and fen != "\n" and fen.isdigit()!=True and len(fen)>1):           #判断内容：上面fen所得内容不是空格，不是换行，不是数字且字符串长度大于1
        if result.has_key(fen):                   #通过上面fen判断rusult是否有该字符，无则存入result并初始化为1，有则在1之后再依次加1
            result[fen] += 1
        else:
            result[fen] = 1
f = open(oFilePath+'result.txt',"w")               #在oFilePath路径下建立一个result的txt文件并写入f的结果

L = sorted(result.items(),key=lambda asd:asd[1],reverse=True)#快速排序方法，把文章中关注度最高的词找出来
for keyword in L[0:5]:                                         #取最高的五个写入之前的文件
    f.write(keyword[0]+' '+'出现次数：'+str(keyword[1])+'\n')
f.close()