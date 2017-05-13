# -*- encoding:utf-8 -*-
# 条形图
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib 
# 调整字体大小
matplotlib.rcParams.update({'font.size': 13})
# 图像大小
plt.figure(figsize=(9,6))
n = 4
X = np.arange(n)+1
# X是1,2,3,4柱的个数
Y1 = [0.571,0.552,0.529,0.571]
Y2 = [0.510,0.614,0.633,0.623]
Y3 = [0.703,0.698,0.716,0.741]
Y4 = [0.656,0.666,0.672,0.695]
width = 0.2#width:柱的宽度
for x,y in zip(X, [Y1, Y2, Y3, Y4]):
    l1 = plt.bar(x-width*2,  y[0],   width = width, facecolor = 'lightskyblue',  edgecolor = 'white')
    l2 = plt.bar(x-width,    y[1],   width = width, facecolor = 'yellowgreen',   edgecolor = 'white')
    l3 = plt.bar(x,          y[2],   width = width, facecolor = 'blue',          edgecolor = 'white')
    l4 = plt.bar(x+width,    y[3],   width = width, facecolor = 'orange',        edgecolor = 'white')
# 限制y的距离从0.3到0.8
# plt.ylim(0, 0.8)
# x，y轴标记
plt.xticks(np.arange(1,5,1), ('Text Modality', 'Visual Modality', 'Emoticon Modality', 'Overall'))
plt.yticks(np.linspace(0.3, 0.8, 6))
# y轴名称
plt.ylabel("Classification Accuracy")
# 显示图例
lightskyblue_patch = mpatches.Patch(color='lightskyblue', label='CBM-LR')
yellowgreen_patch = mpatches.Patch(color='yellowgreen', label='CBM-SVM')
blue_patch = mpatches.Patch(color='blue', label='HGL')
orange_patch = mpatches.Patch(color='orange', label='WS-MDL')
plt.legend(handles=[lightskyblue_patch,yellowgreen_patch,blue_patch,orange_patch])
# plt.legend(('rect' ,),('CBM-LR','CBM-SVM','HGL','WS_MDL',))
plt.savefig('bar1.eps', format='eps', dpi=1000)
plt.show()