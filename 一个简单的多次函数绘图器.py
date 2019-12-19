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

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()