import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

#Carregar a imagem
image = cv2.imread("regua-test.jpg")
#Lista das coordenadas da marcação da régua
cap_area_verde = []

#Imprimir as propriedades da imagem escolhida
print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {}".format(image.shape[2]))


'''h, bin_edge = np.histogram(image.ravel(),64,(0,255))
w=256./64
bin_center = bin_edge[1:]-(w/2)
plt.subplot(2,3,4)
plt.bar(bin_center,h,width=w)
plt.title('Historiograma')
plt.imshow(image,cmap='gray')
# "Pega" as propriedades.
'''
altura,largura,bytesPorPixel = np.shape(image)

#Metodo para calcular a distância euclidiana
def dist_euclidiana(v1, v2):
	v1, v2 = np.array(v1), np.array(v2)
	print("Y: "+str(v1))
	print("X: "+str(v2))
	diff = v1 - v2
	#print("Diferença: "+str(diff))
	quad_dist = np.dot(diff, diff)
	return math.sqrt(quad_dist)



# percorre toda a imagem.
for py in range(0,altura):
	for px in range(0,largura):
		#b, g, r = cv2.split(image[py][px])
		print("Azul: "+b+" Verde: "+g+" Vermelho: "+r)
		#if image[py][px] == [36 244 2]:
		#	cap_area_verde.append([py,px])
		#print(image[px])
		print("Distancia Euclidiana: "+'%.2f' % dist_euclidiana(px, py))
		print (image[py][px])

print("A régua está: "+cap_area_verde)