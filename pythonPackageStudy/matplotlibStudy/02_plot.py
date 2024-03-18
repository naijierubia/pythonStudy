"""
绘制正弦函数和余弦函数 
"""
import numpy as np
import matplotlib.pyplot as mp

# 从-π到π 取1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x) / 2

# 修改x轴刻度文本，支持LaTex表达式
# names显示内容
names = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$']
# xticks设置需要显示的刻度
mp.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], names)

# 设置坐标轴
# 创建坐标轴对象
ax = mp.gca()
# 设置四条轴的位置和颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# data为数据，0为x轴的起始位置
# set_position(('axes', 0.5))位置设置为坐标轴范围的 50% 处
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 绘制曲线，分别可以设置线型、线宽，透明度，颜色，标签
mp.plot(x, sinx, linestyle='--', linewidth=2, alpha=0.7, color='dodgerblue', label=r'$y=sin(x)$')    
mp.plot(x, cosx, linestyle='-.', linewidth=2, alpha=0.7, color='orangered', label=r'$y=\frac{1}{2}cos(x)$')

# 绘制特殊点，设置marker，edgecolors，facecolor，s，label，zorder
# marker: 点的形状，D为圆点，o为圆圈，s为正方形，*为星形，+为加号，x为叉形，^为倒三角形，v为倒三角形
# edgecolors: 边缘颜色，facecolor: 填充颜色
# s: 点的大小
# zorder为图层的优先级，值越大，越靠前
xs, ys = [np.pi/2, np.pi/2], [1, 0]
mp.scatter(xs, ys, marker='D', edgecolors='red', facecolor='green', s=100, label='Points', zorder=3)

# 设置备注文本
# 第一个参数为注释的文本内容
# xycoords为注释的坐标系，data为数据坐标系
# xy为注释的坐标，textcoords相对偏移参考系，xytext为注释的偏移量
# fontsize为注释的字体大小
# arrowprops为箭头的属性，arrowstyle为箭头的样式，connectionstyle为箭头的连接方式
mp.annotate(r'$[\frac{\pi}{2}, 1]$', xycoords='data', xy=(np.pi/2, 1), 
            textcoords='offset points', xytext=(30, 20), fontsize=14,
            arrowprops=dict(arrowstyle='->', connectionstyle='angle3'))

# 显示图例
mp.legend()
mp.show()
