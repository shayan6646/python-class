import matplotlib.pyplot as plt
import numpy as np


'''1 and 2'''
x = 3
square=np.square(x)


'''3 and 4'''
angle=30
degree_value1= np.sin(angle)
degree_value2= np.cos(angle)
radian_value3= np.radians(angle) 

'''5 and 6'''
y= np.linspace(-1,1,500)
y_53th= y[53]

'''7'''
plt.plot(y,np.sin(2*np.pi*y))
plt.show()




'''EX2'''
vec1 = np.array([-1,4,-9])
mat1 = np.array([[1,3,5],[7,-9,2],[4,6,8]])
'''1'''
vec2=(np.pi/4)*vec1

'''2'''
vec3=np.cos(vec1)

'''3'''
vec4=vec1+2*vec2

'''5'''
vec5=np.matrix(mat1)*np.matrix(vec4)

'''6'''
transpose=np.transpose(mat1)

'''7'''
det=np.linalg.det(mat1)

'''8'''
Trace=np.trace(mat1)

'''9'''
minimum=np.min(vec1)

'''10'''
position_of_smallest = np.argmin(vec1)

'''11'''
minimum=np.min(mat1)

'''12'''
A=np.array([[17,24,1,8,15],
            [23,5,7,14,16],
            [4,6,13,20,22],
            [11,18,25,2,9]])
B=np.sum(A,axis=0)
C=np.sum(A,axis=1)

B_min=B.min(axis=0)
B_max=B.max(axis=0)
c_min=C.min(axis=0)
c_max=C.max(axis=0)

A_diag=np.diag(A)
A_diag_sum=np.sum(A_diag)

A_flip=np.fliplr(A)
A_flip_diag=np.sum(A_flip)


if B_min==B_max==c_min==c_max=A_diag_sum=A_flip_diag:
    print("True") 

'''13'''
np.random.rand(10,10)

'''14'''



'''EX3'''

'''1''' 
x = np.linspace(0, 10, 1)

f = np.exp(-x/10)*np.sin(np.pi*x) 
g = x*np.exp(-x/3)

plt.plot(x,f,x,g)

plt.title('title')
plt.xlable('x')
plt.ylable('y')
plt.grid()

plt.show() 


'''2'''

phi = np.linspace(0, 2.*np.pi, 400)
r1 = 0.8 + np.cos(phi)
x1 = r1 * np.cos(phi)
y1 = r1 * np.sin(phi)

r2 = 1 + np.cos(phi)
x2 = r2 * np.cos(phi)
y2 = r2 * np.sin(phi)

r3 = 1.2 + np.cos(phi)
x3 = r3 * np.cos(phi)
y3 = r3 * np.sin(phi)

plt.subplot(3,1,1)
plt.plot(x1, y1, 'ro')
plt.subplot(3,1,2)
plt.plot(x2, y2, 'ro')
plt.subplot(3,1,3)
plt.plot(x3, y3, 'ro')

plt.show()















