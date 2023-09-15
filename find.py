import os
import tkinter as tk
from tkinter import filedialog
import re
import chardet

root = tk.Tk()
root.withdraw()


def catlines(file, pattern):
    a = file.readlines()
    b = []
    for i in range(len(a)):
        if re.search(pattern=pattern, string=a[i]) != None:
            b.append(a[i])
    return (b)


def catlist(a):
    for i in range(len(a)):
        regex = re.compile('\n')
        print(regex.sub('', a[i]))


path = filedialog.askdirectory()  # 使用对话框的方式选择文件夹
a = os.listdir(path)

for file in a:
    if file.endswith('.R'):
        with open(os.path.join(path, file), 'rb') as src_file:
            text = src_file.read()
            encode = chardet.detect(text)
            print(encode)
        if encode['confidence'] > 0.7:
            with open(os.path.join(path, file), 'r', encoding=encode['encoding']) as src_file:
                print(file)
                c = []
                c = catlines(src_file, 'lib')  # !!!!看这里！！！这里引号里的是关键词，注意修改
                if c != []:
                    catlist(c)
                    print('\n')

# 注意，这个代码只会寻找该文件夹下的所有R文件，不会递归去遍历子文件夹中的R文件
# 如果需要寻找子文件夹中的所有的R文件，使用另一个脚本
# 虽然现在大家写的基本都是utf-8编码的，但是大家往往存了一大堆别人的代码，或者古早的代码
# 由于中文编码繁杂，所以我用了一个库：chardet。需要自行安装一下，在终端中输入：pip3 install chardet
# 部分文件由于无法识别编码格式就放弃了。如果还有报错可以联系我
