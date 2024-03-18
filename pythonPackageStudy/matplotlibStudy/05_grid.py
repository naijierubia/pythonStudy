"""
网格布局，和css中的网格布局类似
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('GridSpec', facecolor='lightgray')
gs = mg.GridSpec(3, 3)

mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36, alpha=0.8)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, 2, ha='center', va='center', size=36, alpha=0.8)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 3, ha='center', va='center', size=36, alpha=0.8)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, 4, ha='center', va='center', size=36, alpha=0.8)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[2, 1:])
mp.text(0.5, 0.5, 5, ha='center', va='center', size=36, alpha=0.8)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

# 自由布局
mp.figure('Free Layout', facecolor='lightgray')
# 和左下角的距离为0.13倍
mp.axes([0.13, 0.13, 0.34, 0.24])

mp.show()
