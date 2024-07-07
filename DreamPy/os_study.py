import os
import stat
# 获取当前工作目录
cwd = os.getcwd()
print(cwd)

# 更改当前工作目录
# os.chdir('/path/to/new/directory')

# 获取目录下所有文件和目录
path = 'D:\python_study\python_study1\Python_Study\DreamPy'
dir_list = os.listdir(path)
print(dir_list)

# 删除文件
# path = '/path/to/file'
# os.remove(path)

#删除制定空目录
# os.rmdir(path)

#递归删除目录
# os.rmtree(path)

# 重命名文件或目录
# src = '/path/to/old/name'
# dst = '/path/to/new/name'
# os.rename(src, dst)

# 获取文件或目录属性
# path = '/path/to/file_or_directory'
info = os.stat(path)
print(info)

# 遍历目录树
for root, dirs, files in os.walk(path):
    print('目录路径：', root)
    print('子目录列表：', dirs)
    print('文件列表：', files)

# 列出目录下的文件和目录
# path = '/path/to/directory'
with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.is_dir())

# 获取文件或目录的访问和修改时间
atime = os.path.getatime(path)
mtime = os.path.getmtime(path)
print('最后访问时间：', atime)
print('最后修改时间：', mtime)

# 获取文件或目录的大小
size = os.path.getsize(path)
print('大小为：', size, '字节')

# 获取文件或目录的权限
mode = os.stat(path).st_mode
print('权限为：', oct(stat.S_IMODE(mode)))

# 获取文件名和目录名
path = '/path/to/file_or_directory'
filename = os.path.basename(path)
dir_name = os.path.dirname(path)
print('文件名为：', filename)
print('目录名为：', dir_name)

# 拼接路径
path1 = '/path/to/'
path2 = 'file_or_directory'
path = os.path.join(path1, path2)
print('拼接后的路径为：', path)

# 分离路径和扩展名
path = 'file.txt'
name, ext = os.path.splitext(path)
print('文件名为：', name)
print('扩展名为：', ext)

# 判断路径是否存在
path = '/path/to/file_or_directory'
if os.path.exists(path):
    print('路径存在')
else:
    print('路径不存在')

# 判断路径是否为文件或目录
path = '/path/to/file_or_directory'
if os.path.isfile(path):
    print('路径为文件')
elif os.path.isdir(path):
    print('路径为目录')
else:
    print('路径不存在')
