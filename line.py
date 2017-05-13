# -*- encoding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
# 调整字体大小
matplotlib.rcParams.update({'font.size': 16})
# 横坐标x
x = np.array([10, 20, 25, 30, 33, 36, 38])
# 纵坐标y1到y4
y1 = np.array([0.55,
0.562,
0.566,
0.57,
0.572,
0.573,
0.573
])
y2 = np.array([0.51,
0.566,
0.587,
0.606,
0.619,
0.627,
0.629
])
y3 = np.array([0.705,
0.715,
0.725,
0.735,
0.737,
0.738,
0.738
])
y4 = np.array([0.625,
0.643,
0.657,
0.675,
0.689,
0.697,
0.698
])
# 限制y的距离从0.3到0.8
plt.ylim(0.3, 0.8)
# x轴标记
plt.xticks(np.array([10, 20, 25, 30, 33, 36, 38]), [10, 20, 25, 30, 33, 36, 38])
# y轴标记
plt.yticks(np.linspace(0.3, 0.8, 6))
# 画图 
# c short for color
# marker 是点标记的形状
plt.plot(x, y1, c = 'b', marker = 'o', label = 'T-Modality')
plt.plot(x, y2, c = 'g', marker = 's', label = 'V-Modality')
plt.plot(x, y3, c = 'c', marker = 'D', label = 'E-Modality')
plt.plot(x, y4, c = 'orange', marker = 'x', label = 'Overall')
# x，y轴名称
plt.xlabel('Epoch')
plt.ylabel('Validation Accuracy')
# 显示图例
plt.legend()
# 保存图片
plt.savefig('line1.eps', format='eps', dpi=1000)
# 显示图片
plt.show()