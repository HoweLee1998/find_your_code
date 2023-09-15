import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# 先建立一个文件夹用以存放所有的R文件
path = filedialog.askdirectory()  # 文件来源
dest_dir = filedialog.askdirectory()
lst_files = os.walk(path)  # lst_files其实是一个迭代系对象
for dirpath, dirname, filename in lst_files:  # lst_files包括路径、目录以及文件名
    for file in filename:
        with open(os.path.join(dirpath, file), 'rb') as src_file:  # with三行代码复制
            if file.endswith('.R'):  # 当需要从多个文件夹中提取文章或需要在一个杂乱的文件夹中筛选
                with open(os.path.join(dest_dir, file), 'wb') as target_file:  # 目标文件夹
                    target_file.write(src_file.read())
# 但是需要注意，重名的文件会被覆盖
# 话说，这个代码难道就只可以寻找R文件吗？pdf不行？
