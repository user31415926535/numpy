
import numpy as np 
import matplotlib.pyplot as plt 
#polyld创建一个多项式
func = np.poly1d(np.array([1,0,0]).astype(float)) #array里的数字从右往左分别代表常数项，一次项，二次项，三次项。。。。的系数
                                                  #当前我写的函数是y=x^2
x = np.linspace(-10,10,10000)#在-10到10之间取点，取得越多越精确 
y = func(x)#把x的值放入多项式计算后赋给y 
plt.plot(x, y) #调用plot函数
plt.xlabel('x') #创建x轴轴标
plt.ylabel('y(x)') #创建y轴轴标
plt.show()#最后用show函数显示函数图像

