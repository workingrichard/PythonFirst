#coding=utf-8
#檔案有中文字，使用 Big5 可以，utf-8 不行。必須將檔案 encoding 也另存成 utf-8 才行。
import os
#import codecs

def outputFile(n):
    strs = list()
    for i in range(0, n):
        strs.append("str" + str(i))
    for s in strs:
        print(s)

    print(strs)

    dir = os.getcwd() #os.path.dirname(os.path.abspath(__file__))
    dir = os.path.join(dir, "_data")
    if not os.path.exists(dir):
        os.mkdir(dir)

    fname = os.path.join(dir, "test.txt")
    print(fname)

    f = None
    with open(fname, 'w', encoding="utf-8") as f:
    #with codecs.open(fname, 'w', 'utf-8') as f:
        for i in range(0, len(strs)):
            f.write(str(i) + "\t" + strs[i] + "\t測試\r\n")

    return fname

def readFile(fname):
    contents = list()
    if not os.path.exists(fname):
        print("file not exist: " + fname)
        return contents

    with open(fname, encoding = "utf-8") as sr:
        for line in sr:
            contents.append(line)
    return contents

def readFileYield(fname):
    if not os.path.exists(fname):
        return;

    with open(fname, encoding = "utf-8") as sr:
        for line in sr:
            yield line