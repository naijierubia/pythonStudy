# argparse模块

argparse可以让用户在运行python程序时传入参数

## 最简单的例子

```python
import argparse

parser = argparse.ArgumentParser(description="program description")
# 接收一个名为echo的参数
parser.add_argument("echo")
# 解析传递的参数
args = parser.parse_args()
print(args.echo)
```

## parser.add_argument()

### 基础使用

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
```

这样在输入下面命令行时就会出现提示

```bash
$ python prog.py -h
usage: prog.py [-h] echo

positional arguments:
  echo        echo the string you use here

options:
  -h, --help  show this help message and exit
```

### 指定输入类型

通常接收的参数默认为字符串类型，你也可以指定为其他类型

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
```

这样程序就会正确输出，并且对于非法参数会给出提示

```bash
$ python prog.py 4
16
$ python prog.py four
usage: prog.py [-h] square
prog.py: error: argument square: invalid int value: 'four'
```

### 可选参数

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

关于输出：

```bash
$ python prog.py --verbosity 1
verbosity turned on
$ python prog.py
$ python prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]

options:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity
$ python prog.py --verbosity
usage: prog.py [-h] [--verbosity VERBOSITY]
prog.py: error: argument --verbosity: expected one argument
```

即--前缀的参数名为可选参数，如果没有指定值，则默认为None

### action指定为布尔值

但是我们也可以通过action参数改变默认行为，让可选参数默认值为False，传入后为True

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

但是需要注意当设置了store_true后，该参数不允许再传入值，否则报错

store_false与之相反

### 短选项

使用-v可指定短选项

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

输出为：

```bash
$ python3 prog.py -v
verbosity turned on
$ python3 prog.py --help
usage: prog.py [-h] [-v]

options:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```

### 限制输入

```py
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
```

```bash
$ python3 prog.py -v 3
usage: prog.py [-h] [-v {0,1,2}] square
prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)
```

### action 统计出现次数

可通过指定为count统计参数的出现次数，返回int值

```py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
print(args.verbosity,type(args.verbosity))
```

```bash
$ python3 prog.py 
None <class 'NoneType'>
$ python3 prog.py -vv
2 <class 'int'>
```

### default 制定默认值

```py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
print(args.verbosity,type(args.verbosity))
```

```bash
$ python3 prog.py 
0 <class 'int'>
```



## 案例

```py
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
```

```bash
$ python3 prog.py 4 2
4^2 == 16
$ python3 prog.py 4 2 -q
16
$ python3 prog.py 4 2 -v
4 to the power 2 equals 16
$ python3 prog.py 4 2 -vq
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
$ python3 prog.py 4 2 -v --quiet
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
```