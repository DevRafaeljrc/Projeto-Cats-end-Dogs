# Importar bibliotecas necessárias
import cv2
import numpy as np


# Carregar imagem colorida
imagem = cv2.imread(r'C:\Projeto Colabi\Projeto-Cats-end-Dogs\Pequena_Dormindo.jpeg')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
	raise FileNotFoundError("A imagem não foi encontrada. Verifique o caminho do arquivo.")

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Definir limiar para binarização
limiar = 127
_, imagem_binarizada = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)

# Exibir imagens
cv2.imshow('Imagem Cinza', imagem_cinza)
cv2.imshow('Imagem Binarizada', imagem_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar as imagens processadas
cv2.imwrite('imagem_cinza.jpg', imagem_cinza)
cv2.imwrite('imagem_binarizada.jpg', imagem_binarizada)