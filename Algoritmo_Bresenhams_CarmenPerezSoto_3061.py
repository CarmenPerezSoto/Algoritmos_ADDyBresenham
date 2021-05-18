#importamos la libreria para poder graficar
import matplotlib.pyplot as plt
#Declaramos las variables que recibiran los valores
x1 = int( input("Introduce el valor de X1 ") )
y1 = int( input("Introduce el valor de Y1 ") )
x2 = int( input("Introduce el valor de X2 ") )
y2 = int( input("Introduce el valor de Y2 ") )
x=x1
y=y2
#calculamos la diferencia
dx = x2-x1
dy = y2-y1
#calculamos a p
p = 2*dy - x
#calculamos los nuevos valores de x y y
while(x<=x2):
    plt.scatter(x,y)
    x=x+1
    if p<0:
        p=p+2*dy
    else:
        p=p + (2*dy)-(2*dx)
        y=y+1
    print(x,y)
plt.show()