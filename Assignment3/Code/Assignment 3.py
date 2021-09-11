import numpy as np
import matplotlib.pyplot as plt
# assigning the vectors
A = np.array([0,4])
A.resize((2,1))
B = np.array([4,0])
B.resize((2,1))
C = np.array([0,-2])
C.resize((2,1))
D = np.array([2,0])
D.resize((2,1))
E = np.array([2,6])
E.resize((2,1))
F = np.array([0,0])
F.resize((2,1))

plt.scatter(A[0],A[1],marker="o")
plt.scatter(B[0],B[1],marker="o")
plt.scatter(C[0],C[1],marker="o")
plt.scatter(D[0],D[1],marker="o")
plt.scatter(E[0],E[1],marker="o")
plt.scatter(F[0],F[1],marker="o")

plt.text(A[0],A[1], "A", color='black')
plt.text(B[0],B[1], "B", color='black')
plt.text(C[0],C[1], "C", color='black')
plt.text(D[0],D[1], "D", color='black')
plt.text(E[0],E[1], "E", color='black')
plt.text(F[0],F[1], "F", color='black')

x1 = np.linspace(0, 4, 100)
y1 = 4-x1
plt.plot(x1, y1,label="AB") 
x2 = np.linspace(0, 2, 100)
y2 = x2-2
plt.plot(x2, y2,label="CD") 
x3 = np.linspace(0, 2, 100)
y3 = 3*x3
plt.plot(x3, y3,label="EF") 
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend(bbox_to_anchor=(1, 1), loc='lower center')
plt.grid()
plt.show()