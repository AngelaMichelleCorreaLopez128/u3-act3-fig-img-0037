import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
# Angela Correa NC = 0037
print("Angela Correa NC = 0037")
print("UII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen= cv2.imread('Ari 0037.jpg')
plt.imshow(mi_imagen)
plt.title('Ariana Grande y Angela Correa 0037')
plt.show()
print("+--+-++-+-+-+- Puntos en la imagen -+-+-++-+-+--++-")
plt.imshow(mi_imagen)
x = [100, 100, 300]
y = [100, 400, 500]
plt.scatter(x, y, s=20,c='red')
plt.show()
print("+--+-++-+-+-+- Cuadro azul en la imagen -+-+-++-+-+--++-")
imag_Ariana = cv2.imread('Ari 0037.jpg')
plt.imshow(imag_Ariana)
# x = [100,100,500,500,100]
# y = [500,100,100,500,500]
# Coordenadas del cuadro movido 50 unidades a la derecha
x = [160, 160, 460, 460, 160]
y = [450, 150, 150, 450, 450]
plt.plot(x, y, c='blue')
plt.show()

print("-+-+-+-+ Circulo verde en la imagen +--+-+-+-+")
mi_imagen= cv2.imread('Ari 0037.jpg')
plt.imshow(mi_imagen)
N = 30 # Lados del 6ligno
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for mi_imagen in range (N+1):
    t = 2 * np . pi / N * mi_imagen
    x[mi_imagen] = xc + r*np.cos(t)
    y[mi_imagen] = yc + r*np.sin(t)

plt.plot(x, y, c = "green" )
plt.show()