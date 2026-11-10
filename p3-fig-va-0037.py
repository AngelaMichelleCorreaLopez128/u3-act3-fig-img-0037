import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
# Angela Correa NC = 0037
print("Angela Correa NC = 0037")
print("UII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen= cv2.imread('Ariana Grande 0037.jpg')
plt.imshow(mi_imagen)
plt.title('Ariana Grande y Angela Correa 0037')
plt.show()
print("+--+-++-+-+-+- Puntos en la imagen -+-+-++-+-+--++-")
plt.imshow(mi_imagen)
x = [100,100,300,553.2]
y = [100,400,500,138]
plt.scatter(x, y, s=20,c='red')
plt.show()