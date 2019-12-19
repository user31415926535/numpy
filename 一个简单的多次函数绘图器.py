import numpy as np
import matplotlib.pyplot as plt
n=int(input("该多项式是一个几次函数:"))+1
a=[]
b=input("请输入多项式系数:").split(" ")#split函数表示输入的数用“”内的符号或空格分隔开
for i in range(0,n):
    a.append(int(b[i]))
func=np.poly1d(np.array(a).astype(float))
x=np.linspace(-100,100,1000)
y=func(x)

plt.plot(x,y,'r')
plt.xlim((-5,5))
plt.ylim((-5,5))#划定显示的范围
#plt.xlabel('x')
#plt.ylabel('y(x)')#显示x，y的轴标

#new_ticks=np.linspace(-1,2,5)
#print(new_ticks)
#plt.xticks(new_ticks)
#plt.yticks([-5,-4,2,3,4],
#           ['red','pink','red','r','w'])#通过一一对应替换掉相应的数标
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')#将上框和右框颜色设置为无色（使两条边框消失）
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')#将底边框设置为x轴，将左边框设置为y轴
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))#将x，y两条轴移到0的位置上
plt.show()