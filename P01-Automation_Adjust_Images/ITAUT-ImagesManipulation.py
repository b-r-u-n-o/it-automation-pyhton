# Repita cada arquivo da pasta
# Para cada arquivo:
# Girar a imagem 90 ° no sentido horário (270)
# Redimensione a imagem de 192x192 para 128x128
# Salve a imagem em uma nova pasta no formato .jpeg
# Você pode nomear o arquivo como quiser.
# E certifique-se de salvar as imagens atualizadas na pasta:/opt/icons/

#!/usr/bin/env python3

from PIL import Image
import sys
import os


def AdjustImages():

    size = (128, 128)
    graus = 270

    for root, dirs, file in os.walk("<pathimages>"):

        print(dirs)

        for infile in file:
            f, e = os.path.splitext(infile)
            outfile = '/opt/icons/' + f
            try:
                im = Image.open(infile)
                im.rotate(graus).resize(size).convert(
                    "RGB").save(outfile, "jpeg")
                print('Success record!')

            except OSError as e:
                print("Not possible converted {} {}".format(infile, e))
                pass

        return 'Finally process with success'


if __name__ == '__main__':
    AdjustImages()
