import matplotlib.pyplot as mp
"""
绘制多个窗口，设置属性时在哪个绘图后面就是在设置哪个窗口 
"""

# 创建一个灰色背景的图形窗口
mp.figure('Figure A', facecolor='gray')
# 在窗口中绘制一条直线，起点为(0, 0)，终点为(1, 1)
mp.plot([0, 1], [0, 1])

# 创建一个浅灰色背景的图形窗口
mp.figure('Figure B', facecolor='lightgray')
# 在窗口中绘制一条直线，起点为(0, 1)，终点为(1, 0)
mp.plot([0, 1], [1, 0])

# 设置窗口的常用属性参数
mp.title('Test Title', fontsize=16)  # 设置窗口的标题字体大小为16
mp.xlabel('Date', fontsize=14)  # 设置x轴标签字体大小为14
mp.ylabel('Price', fontsize=14)  # 设置y轴标签字体大小为14
mp.grid(linestyle=':')  # 绘制网格线，线条样式为虚线
mp.tight_layout()  # 调整图形布局，使图像更加美观

# 重新绘制第一个窗口
mp.figure('Figure A')
# 在窗口中绘制一条直线，起点为(1, 2)，终点为(3, 3)
mp.plot([1, 2, 3], [2, 1, 3])

mp.show()