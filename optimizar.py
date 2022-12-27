from PIL import Image
import os

"""
 * download image weights 
 * @author: Luis Avila
 * @version: 1.0.0
"""


def progressBar(progress, total):
    if total == 0:
        total = 1

    percent = 100 * (progress / float(total))
    bar = '▓' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
    if (progress == total):
        print("\n")


def optimizar(quality=60):
    pathOptimizar = './para-optimizar/'
    pathOptimizado = './optimizado/'

    if __name__ == '__main__':
        listFiles = os.listdir(pathOptimizar)
        if (len(listFiles)):
            progressBar(0, len(listFiles))

        it = 0
        for filename in listFiles:
            name, extension = os.path.splitext(pathOptimizar + filename)

            if extension in ['.jpeg', '.jpg', '.png']:
                picture = Image.open(pathOptimizar + filename)
                picture.save(pathOptimizado + filename,
                             optimize=True, quality=quality)
                os.remove(pathOptimizar + filename)

            """if extension in ['.mp3']:
                music = 'dir/music/'
                os.rename(pathOptimizar + filename, music + filename)
            """
            it = it + 1
            progressBar(it, len(listFiles))


print('''
==============================================
||             Luis Ávila                   || 
==============================================

Este proceso no mantiene las imágenes origínales 
Seleccione una acción a realizar:
1: Optimizar las imágenes (recomendado) 
2: Optimizar personalizado
3: Salir
''')

option = input('Ingrese la acción a ejecutar ')
if (option == '1'):
    optimizar()
if (option == '2'):
    try:
        quality = int(input('Digite un numero entre 1 y 100 '))
        if (quality >= 0 and quality <= 100):
            optimizar(quality)
        else:
            print(f'Valor no valido "{quality}"')
    except:
        print("Valor no valido")
