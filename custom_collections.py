1| # -*- coding: utf-8 -*-
2| import subprocess
3| import sys
4| from matplotlib import pyplot as plt
5| import cv2
6| import numpy as np
7| from os import walk, path
8| 
9| def install(package):
10|     """Instala o pacote especificado usando pip."""
11|     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
12| 
13| def ensure_package_installed(package_name):
14|     """Verifica se o pacote está instalado e, se não estiver, instala-o."""
15|     try:
16|         __import__(package_name)
17|     except ImportError:
18|         install(package_name)
19| 
20| ensure_package_installed("matplotlib")
21| ensure_package_installed("skyfield")
22| 
23| def read_images_from_folder(folder_path):
24|     """Lê imagens de uma pasta especificada e retorna uma lista de arrays de imagens."""
25|     images = []
26|     for dirpath, _, filenames in walk(folder_path):
27|         for filename in filenames:
28|             if filename.endswith('.jp2') and 'TCI' in filename:
29|                 image_path = path.join(dirpath, filename)
30|                 print(f"Loading image: {image_path}")
31|                 # image_ds = gdal.Open(image_path)
32|                 # image_band = image_ds.GetRasterBand(1)
33|                 # images.append(image_band.ReadAsArray())
34|     return images
35| 
36| def adaptative_hist_eq(image):
37|     """Aplica equalização de histograma adaptativa à imagem."""
38|     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
39|     return clahe.apply(image)
40| 
41| def detect_white_spots(image):
42|     """Detecta manchas brancas na imagem."""
43|     element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
44|     blur = cv2.GaussianBlur(image, (9, 9), 0)
45|     thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
46|     thresh = cv2.erode(thresh, None, iterations=5)
47|     thresh = cv2.dilate(thresh, element, iterations=3)
48|     return 1 * (thresh == 255)
49| 
50| def otsu(image):
51|     """Aplica a binarização de Otsu à imagem."""
52|     ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
53|     return img
54| 
55| def gamma_correction(image, gamma):
56|     """Aplica correção gamma à imagem."""
57|     invGamma = 1.0 / gamma
58|     table = np.array([((i / 255.0) ** invGamma) * 255 for i in range(256)]).astype("uint8")
59|     return cv2.LUT(image, table)
60| 
61| def process_canny(image, equalize, correct, remove_white):
62|     """Processa a imagem usando o algoritmo de Canny."""
63|     if equalize:
64|         image = adaptative_hist_eq(image)
65|     if correct:
66|         image = gamma_correction(image, 2.0)
67|     if remove_white:
68|         image = image * (1 - detect_white_spots(image))
69|     image = cv2.GaussianBlur(image.astype('uint8'), (5, 5), 0)
70|     image = cv2.Canny(image.astype('uint8'), 100, 200)
71|     return image
72| 
73| def process_morphological(image):
74|     """Processa a imagem usando operações morfológicas."""
75|     equalized = adaptative_hist_eq(image)
76|     gamma_corrected = gamma_correction(equalized, 1.5)
77|     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
78|     blurred = cv2.GaussianBlur(gamma_corrected, (5, 5), 0)
79|     otsu_image = otsu(blurred)
80|     eroded = cv2.erode(otsu_image, kernel, iterations=1)
81|     dilated = cv2.dilate(eroded, kernel, iterations=1)
82|     return dilated
83| 
84| def segment_roads(image, equalize, correct_gamma, detect_white):
85|     """Segmenta as estradas na imagem."""
86|     x_len, y_len = image.shape
87|     smallx, smally = (round(x_len / 40), round(y_len / 40))
88|     for x in range(0, x_len - smallx, smallx):
89|         for y in range(0, y_len - smally, smally):
90|             plt.imshow(image[x:x + smallx, y:y + smally], cmap='gray')
91|             plt.show()
92|             plt.imshow(process_canny(image[x:x + smallx, y:y + smally], equalize, correct_gamma, detect_white), cmap='gray')
93|             plt.show()
94| 
95| def correct_satellite_name(image_path):
96|     """Corrige o nome do satélite na imagem."""
97|     return image_path.replace("OldSatelliteName", "NewSatelliteName")
98| 
99| def send_location_info(image):
100|     """Envia informações de localização conectadas à imagem."""
101|     location_info = "Informações de localização conectadas à imagem."
102|     print(location_info)
103|     # Adicione aqui o código para enviar as informações para um servidor ou salvá-las em um arquivo
104| 
105| def main():
106|     """Função principal do script."""
107|     print("Script will proceed with default parameters. Use this way: python canny.py [equalize] [correct_gamma] [detect_white]")
108|     print("Every value must be 0 or 1.")
109| 
110|     folder_path = "starlink_match_plots.png"  # Corrigir o caminho da pasta
111|     folder_path2 = "visualization.png"  # Adiciona a variável folder_path2
112|     images = read_images_from_folder(folder_path)
113| 
114|     if len(sys.argv) == 4:
115|         equalize = int(sys.argv[1])
116|         correct_gamma = int(sys.argv[2])
117|         detect_white = int(sys.argv[3])
118|     else:
119|         equalize = 1
120|         correct_gamma = 1
121|         detect_white = 1
122| 
123|     for image in images:
124|         corrected_image_path = correct_satellite_name("image_path_placeholder")  # Substituir pelo caminho real da imagem
125|         send_location_info(image)
126|         segment_roads(image.astype('uint8'), equalize, correct_gamma, detect_white)
127| 
128| if __name__ == "__main__":
129|     main()
130| 
