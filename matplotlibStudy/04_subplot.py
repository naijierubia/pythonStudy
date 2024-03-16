import matplotlib.pyplot as mp
"""
绘制多个子图 
"""
mp.figure('Subplot', facecolor='lightgray')

for i in range(1, 10):
    mp.subplot(3, 3, i)
    mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.6)
    mp.xticks([])
    mp.yticks([])
    # 自动调整子图间距
    mp.tight_layout()

mp.show()