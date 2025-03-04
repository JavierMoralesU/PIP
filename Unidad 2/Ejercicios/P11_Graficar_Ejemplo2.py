

from matplotlib import pyplot as plt
import math

lim_inferior = -10
lim_superior = 10
funcion = "math.sin(x)"
val = 45
funcion = funcion.replace("x", str(val) )
resultado = eval(funcion)
print(resultado)

x = []
for i in range (lim_inferior , lim_superior+1,1):
    x.append(i)
print("X:",x)

y = []
for i in range ( len(x) ):
    funcion = "math.sin(x)"
    funcion = funcion.replace("x", str(i) )
    resultado = eval(funcion) #ejecuta cadena de caracteres
    y.append(resultado)
print("Y:",y)

plt.plot(x,y)
plt.show()


