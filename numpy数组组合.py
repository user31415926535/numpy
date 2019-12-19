import numpy as np

a=np.arange(9).reshape(3,3)#reshape：把数按三个一组分成三组，形成3*3的矩阵，这样就成了三维数组，numpy里的维度叫秩
b=2*a
print(b)


#numpy的切片截取操作与Python一样，而numpy多了水平组合数组
#的操作hskack和垂直组合数组vstack
c=np.hstack((a,b))
print(c)
#hstack能做到的事俺concatenate也能做到
d=np.concatenate((a,b,c),axis=1)#这里axis=1可以将多组矩阵水平拼接
                                #当axis=0时可实现垂直组合，功能和vstack一样
print(d)



e=np.vstack((a,b))
print(e)
f=np.concatenate((a,b),axis=0)
print(f)
#但不管是vstack还是concatenate  axis=0，都只能垂直组合两组矩阵，不能多组组合

#OK接下来是深度组合,就是将一系列数组沿着纵轴（深度）方向进行层叠组合。举个例子，有若干张二维平
#面内的图像点阵数据，我们可以将这些图像数据沿纵轴方向层叠在一起，这就形象地解释了什么
#是深度组合。（感觉书上的比喻很形象就搬过来了）
g=np.dstack((a,b))
print(g)
h=np.dstack((g,a))
print(h)

#列组合
i=np.column_stack((a,b))
print(i)
a1=np.arange(2)
a2=a1+2
j=np.column_stack((a1,a2))
print(j)
#column_stack函数对于一维数组将按列方向进行组合
#对于二维数组，column_stack与hstack的效果是相同的

#以下是numpy中数组的比较
k=np.column_stack((a, b)) == np.hstack((a, b))
print(k)

#行组合
l=np.row_stack((a,b))
print(l)

#分割和组合使用方法类似，只是用的函数不一样（《numpy学习指南》数组的分割）