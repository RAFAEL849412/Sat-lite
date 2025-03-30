# -*- coding: utf-8 -*-
import subprocess
import sys
from matplotlib import pyplot as plt
import cv2
import numpy as np
from os import walk, path

def install(package):
    """Instala o pacote especificado usando pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def ensure_package_installed(package_name):
    """Verifica se o pacote está instalado e, se não estiver, instala-o."""
    try:
        __import__(package_name)
    except ImportError:
        install(package_name)

ensure_package_installed("matplotlib")
ensure_package_installed("skyfield")

def read_images_from_folder(folder_path):
    """Lê imagens de uma pasta especificada e retorna uma lista de arrays de imagens."""
    images = []
    for dirpath, _, filenames in walk(folder_path):
        for filename in filenames:
            if filename.endswith('.jp2') and 'TCI' in filename:
                image_path = path.join(dirpath, filename)
                print(f"Loading image: {image_path}")
                # image_ds = gdal.Open(image_path)
                # image_band = image_ds.GetRasterBand(1)
                # images.append(image_band.ReadAsArray())
    return images

def adaptative_hist_eq(image):
    """Aplica equalização de histograma adaptativa à imagem."""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(image)

def detect_white_spots(image):
    """Detecta manchas brancas na imagem."""
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    blur = cv2.GaussianBlur(image, (9, 9), 0)
    thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=5)
    thresh = cv2.dilate(thresh, element, iterations=3)
    return 1 * (thresh == 255)

def otsu(image):
    """Aplica a binarização de Otsu à imagem."""
    ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img

def gamma_correction(image, gamma):
    """Aplica correção gamma à imagem."""
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

def process_canny(image, equalize, correct, remove_white):
    """Processa a imagem usando o algoritmo de Canny."""
    if equalize:
        image = adaptative_hist_eq(image)
    if correct:
        image = gamma_correction(image, 2.0)
    if remove_white:
        image = image * (1 - detect_white_spots(image))
    image = cv2.GaussianBlur(image.astype('uint8'), (5, 5), 0)
    image = cv2.Canny(image.astype('uint8'), 100, 200)
    return image

def process_morphological(image):
    """Processa a imagem usando operações morfológicas."""
    equalized = adaptative_hist_eq(image)
    gamma_corrected = gamma_correction(equalized, 1.5)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    blurred = cv2.GaussianBlur(gamma_corrected, (5, 5), 0)
    otsu_image = otsu(blurred)
    eroded = cv2.erode(otsu_image, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)
    return dilated

def segment_roads(image, equalize, correct_gamma, detect_white):
    """Segmenta as estradas na imagem."""
    x_len, y_len = image.shape
    smallx, smally = (round(x_len / 40), round(y_len / 40))
    for x in range(0, x_len - smallx, smallx):
        for y in range(0, y_len - smally, smally):
            plt.imshow(image[x:x + smallx, y:y + smally], cmap='gray')
            plt.show()
            plt.imshow(process_canny(image[x:x + smallx, y:y + smally], equalize, correct_gamma, detect_white), cmap='gray')
            plt.show()

def correct_satellite_name(image_path):
    """Corrige o nome do satélite na imagem."""
    return image_path.replace("OldSatelliteName", "NewSatelliteName")

def send_location_info(image):
    """Envia informações de localização conectadas à imagem."""
    location_info = "Informações de localização conectadas à imagem."
    print(location_info)
    # Adicione aqui o código para enviar as informações para um servidor ou salvá-las em um arquivo

def main():
    """Função principal do script."""
    print("Script will proceed with default parameters. Use this way: python canny.py [equalize] [correct_gamma] [detect_white]")
    print("Every value must be 0 or 1.")

    folder_path = "starlink_match_plots.png"  # Corrigir o caminho da pasta
    folder_path2 = "visualization.png"  # Adiciona a variável folder_path2
    images = read_images_from_folder(folder_path)

    if len(sys.argv) == 4:
        equalize = int(sys.argv[1])
        correct_gamma = int(sys.argv[2])
        detect_white = int(sys.argv[3])
    else:
        equalize = 1
        correct_gamma = 1
        detect_white = 1

    for image in images:
        corrected_image_path = correct_satellite_name("image_path_placeholder")  # Substituir pelo caminho real da imagem
        send_location_info(image)
        segment_roads(image.astype('uint8'), equalize, correct_gamma, detect_white)

if __name__ == "__main__":
    main()
