"""
设置坐标轴的刻度定位器
"""
import matplotlib.pyplot as mp

# 储存一些刻度定位器命令，分别为不设置，每1个刻度一个主刻度，最多4个刻度，以及自定义刻度
# 此外还有对数、线性、等等的刻度定位器
locators = ['mp.NullLocator()', 'mp.MultipleLocator(1)', 'mp.MaxNLocator(nbins=4)', 'mp.FixedLocator(locs=[2,4,8,10])']

mp.figure('Locators', facecolor='lightgray')
mp.title('Locators', fontsize=16)

for i, locator in enumerate(locators):
    # enumerate能同步获取索引和值
    mp.subplot(len(locators), 1, i+1)
    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0.5))
    mp.yticks([])
    # 设置x轴的可视区域
    mp.xlim(1, 10)

    # 设置刻度定位器，每隔1一个主刻度，每隔0.1一个次刻度。
    ax.xaxis.set_major_locator(eval(locator))
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))


mp.show()