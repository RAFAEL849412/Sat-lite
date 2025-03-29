# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import gdal, sys, cv2
from os import walk, path
import zipfile
import os

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Arquivos extraídos para {}".format(extract_to))

def read_images_from_folder(folder_path):
    images = []
    for (dirpath, dirnames, filenames) in walk(folder_path):
        for filename in filenames:
            if filename.endswith('.jp2') and 'TCI' in filename:
                image_path = path.join(dirpath, filename)
                print("Loading image: {}".format(image_path))
                image_ds = gdal.Open(image_path)
                image_band = image_ds.GetRasterBand(1)
                images.append(image_band.ReadAsArray())
    return images

def adaptative_hist_eq(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

def detect_white_spots(image):
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    blur = cv2.GaussianBlur(image, (9, 9), 0)
    thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=5)
    thresh = cv2.dilate(thresh, element, iterations=3)
    return 1 * (thresh == 255)

def otsu(image):
    ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img


def process_canny(image, equalize, correct, remove_white):
    if equalize == 1:
        image = adaptative_hist_eq(image)
    if correct == 1:
        image = gamma_correction(image, 2.0)
    if remove_white == 1:
        image = image * (1 - detect_white_spots(image))
    image = cv2.GaussianBlur(image.astype('uint8'), (5, 5), 0)
    image = cv2.Canny(image.astype('uint8'), 100, 200)
    return image


def process_morphological(image):
    equalized = adaptative_hist_eq(image)
    gamma_corrected = gamma_correction(equalized, 1.5)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    blurred = cv2.GaussianBlur(gamma_corrected, (5, 5), 0)
    otsu_image = otsu(blurred)
    eroded = cv2.erode(otsu_image, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)
    return dilated


def gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = cv2.LUT(image, np.array([((i / 255.0) ** invGamma) * 255
                                     for i in range(256)]).astype("uint8"))
    return table


def segment_roads(image, equalize, correct_gamma, detect_white):
    X, Y = image.shape
    smallx, smally = (round(X / 40), round(Y / 40))
    for x in range(0, X - smallx, smallx):
        for y in range(0, Y - smally, smally):
            plt.imshow(image[x:x + smallx, y:y + smally], cmap='gray')
            plt.show()
            plt.imshow(process_canny(image[x:x + smallx, y:y + smally], equalize, correct_gamma, detect_white), cmap='gray')
            plt.show()


def main():
    folder_path = "solvers"  # pasta 'solvers'
    zip_filename = "solvers.zip"  # Nome do arquivo zip
    zip_path = os.path.join(folder_path, zip_filename)
    
    # Verifica se o arquivo zip existe e extrai os arquivos
    if os.path.exists(zip_path):
        extracted_folder = os.path.join(folder_path, "extracted")
        if not os.path.exists(extracted_folder):
            os.makedirs(extracted_folder)
        extract_zip(zip_path, extracted_folder)
    else:
        print("Arquivo {} não encontrado na pasta {}.".format(zip_filename, folder_path))
        sys.exit(1)
    
    print("Script will proceed with default parameters. Use this way: python canny.py [equalize] [correct_gamma] [detect_white]")
    print("Every value must be 0 or 1.")
    
    images = read_images_from_folder(extracted_folder)  # Carrega todas as imagens extraídas
    
    if len(sys.argv) == 4:
        equalize = int(sys.argv[1])
        correct_gamma = int(sys.argv[2])
        detect_white = int(sys.argv[3])
    else:
        equalize = 1
        correct_gamma = 1
        detect_white = 1

    for image in images:
        segment_roads(image.astype('uint8'), equalize, correct_gamma, detect_white)

# Garante que o código abaixo só será executado quando o script for rodado diretamente
if __name__ == "__main__":
    main()
