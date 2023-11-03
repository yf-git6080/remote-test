# argparse{常用}

参考：[Argparse 教程 — Python 3.9.17 文档](https://docs.python.org/zh-cn/3.9/howto/argparse.html#concepts)

​			[argparse --- 命令行选项、参数和子命令解析器 — Python 3.9.17 文档](https://docs.python.org/zh-cn/3.9/library/argparse.html#the-add-argument-method)

**argparse**模块可以写出友好的 **命令行 **接口，比如 python test.py --help ......等等

现在我们将第一次使用这个包：

~~~python
import argparse
# ArgumentParser主要是做介绍	——介绍这个文件的作用
parser = argparse.ArgumentParser(description='INTRODUCE')
# 调用命令行传入的参数，有了这一行，使用--help就可以显示出文件的信息
parser.parse_args()

# 下面为显示结果
    python test.py --help
    usage: test.py [-h]

    INTRODUCE		# 这里就是介绍

    optional arguments:		# 这下面就是可以使用的指令
      -h, --help  show this help message and exit
~~~

**当我们在遇到一个使用了这个包的文件时，我们就可以使用 ` python 文件名 --help`来查看这个py文件如何使用。**（这个作用很大）



现在我们将添加参数，用来接收命令行传过来的参数:

~~~python
import argparse

parser = argparse.ArgumentParser(description='INTRODUCE')
parser.add_argument("square", help="display a square of a given number",type=int)
args = parser.parse_args()
# 可以使用args中的square，使用时得用完整名称
print(args.square**2)

# 运行结果：
python ..\test.py 2     
4
~~~



好的，我们已经学完了！

接下来就是常用的参数：

~~~python
# 1. 传入数据的默认为str，所以可以增加一个type=int...
parser.add_argument("square", help="display a square of a given number",type=int)
# 2. 可以设置一个标签 action="store_ture",这个标签不接收任何值，仅为true和False
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
# 3. 限制输入，使用choice=[0,1,2]...... 下面限制了输入为012中的一个
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
# 4. action="count"，用来计数，当使用这个参数时，只要使用对应的命令，它的次数就会+1，default=none
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
# 5. 添加一些矛盾的选项，下面的-v和-q只能二选一
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
~~~

# OS

参考：[Python3 OS 文件/目录方法 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-os-file-methods.html)

~~~python
import os 

# 修改文件工作路径
os.chdir(path)

# 返回当前工作目录
os.getcwd()
# 当前文件名
print(__file__)

# 创建单级目录
os.mkdir("")
# 创建多级级目录,exist_ok=True当文件存在时，不会报错，默认为false
os.makedirs(exist_ok=True)


# 重命名文件或目录，从 src 到 dst	
os.rename(src, dst)
#递归删除目录	
os.removedirs(path)
# 删除文件夹或者文件
os.remove(path)
# 删除path指定的空目录，如果目录非空，则抛出一个OSError异常	
os.rmdir(path)


# 返回path指定的文件夹包含的文件或文件夹的名字的列表
os.listdir(path)

# 重命名文件或者文件夹,将src重命名为dst
os.rename(src,dst)
os.place(src,dst)


# 遍历某个文件夹下的所有文件，root为当前目录，dirs为子目录，files为子文件
for root,dirs,files in os.walk(path):
    print(root,dirs,files)
    
    
## os.path中的函数

# 返回绝对路径
os.path.abspath("")
'C:\\Users\\Tyrant\\Documents\\GitHub\\python\\d2l'

# 返回文件名
os.path.basename(os.getcwd())
Out[116]: 'd2l'

# 返回文件路径
os.path.dirname(os.getcwd())
 'C:\\Users\\Tyrant\\Documents\\GitHub\\python'
    
# 判断文件是否存在
os.path.exists(path)

# 将路径拼接
os.path.join(os.getcwd(),"d2l-zh")
'C:\\Users\\Tyrant\\Documents\\GitHub\\python\\d2l\\d2l-zh'

# 把路径分割成 dirname 和 basename，返回一个元组
os.path.split(os.getcwd())
('C:\\Users\\Tyrant\\Documents\\GitHub\\python', 'd2l')

# 分割路径中的文件名与拓展名
os.path.splitext("logs\\r-50.log")
('logs\\r-50', '.log')


~~~

