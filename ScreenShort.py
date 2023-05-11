import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import uuid
import os

# Función para capturar una región de la pantalla
def screen_capture():
    # capturamos la pantalla completa
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)

    # creamos una ventana y mostramos la captura de pantalla
    cv2.namedWindow('Screen Capture', cv2.WINDOW_NORMAL)
    cv2.imshow('Screen Capture', screenshot_np)

    print("Presiona 'r' para seleccionar una región, luego 'c' para confirmar o 'q' para salir.")
    
    # inicializamos el ROI selector
    roi = cv2.selectROI(screenshot_np)

    # una vez seleccionada la región, presionamos 'c' para confirmar
    if roi != (0,0,0,0):
        # recortamos la imagen
        imCrop = screenshot_np[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

        # generamos un nombre de archivo aleatorio
        filename = str(uuid.uuid4()) + ".png"
        filepath = os.path.join(os.path.expanduser("~"), "Desktop", filename)

        # guardamos el archivo en el escritorio
        cv2.imwrite(filepath, imCrop)
        print(f"Screenshot guardado en {filepath}")

    # cerramos la ventana
    cv2.destroyAllWindows()

if __name__ == "__main__":
    screen_capture()
