"""
散点图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 200
x = np.random.normal(175, 5, n)
y = np.random.normal(65, 10, n)

mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=16)
mp.grid(linestyle=':')
# 绘制散点图，其中 marker 为圆圈，alpha 为透明度，label 为图例，s 为大小，c 为颜色，cmap 为颜色映射
mp.scatter(x, y, marker='o', alpha=0.7, label='Samples', s=80, c=x, cmap='jet')
mp.legend()
mp.show()

