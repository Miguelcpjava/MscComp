import cv2
import numpy as np

#Carregar a imagem
image = cv2.imread("regua-test.jpg")

#Imprimir as propriedades da imagem escolhida
print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {}".format(image.shape[2]))

# "Pega" as propriedades.
altura,largura,bytesPorPixel = np.shape(image)

# percorre toda a imagem.
for py in range(0,altura):
	for px in range(0,largura):
		print (image[py][px])