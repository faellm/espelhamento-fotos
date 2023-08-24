import os
import shutil
from PIL import Image

def flip_images(source_dir, destination_dir):
    # Verifica se o diretório de destino existe e cria-o, se necessário
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Percorre todas as imagens no diretório de origem
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # Copia o arquivo original para o destino
        shutil.copy(source_path, destination_path)

        # Inverte a imagem (deixa de ponta cabeça)
        flipped_path = os.path.join(destination_dir, 'flipped' + filename)
        image = Image.open(destination_path)
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        flipped_image.save(flipped_path)

    print("Inversão concluída.")

# Exemplo de uso
source_directory = 'imagem' #Adicione o caminho do seu diretório incial
destination_directory = 'FotosInvertidas' # Nome do diretório final

flip_images(source_directory, destination_directory)
