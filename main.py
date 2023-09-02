import cv2
from pyzbar.pyzbar import decode
import random
import time
from zonas import zonas  # Importa las zonas desde el archivo zonas.py
from usuarios import usuarios  # Importa los usuarios desde el archivo usuarios.py
from database import main as database_main
from datetime import datetime

class BarcodeScanner:
    def __init__(self, zonas):
        self.cap = cv2.VideoCapture(0)
        self.zonas = zonas
        self.last_detection_time = 0


    def process_scan(self, barcode_data, selected_zona):
        user = next((user for user in usuarios if user.id == barcode_data), None)
        if user:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            allowed_zones = [zona.nombre for zona in self.zonas if user.rol in zona.roles_permitidos]

            if selected_zona.nombre in allowed_zones:
                permiso = "Sí"
            else:
                permiso = "No"

            return {
                "Nombre": user.nombre,
                "Zona": user.zonas_permiso,
                "Hora": current_time,
                "Permiso": permiso
            }
        else:
            return None

    def detect_barcodes(self):
        ret, frame = self.cap.read()
        if time.time() - self.last_detection_time >= 2:
            barcodes = decode(frame)

            for barcode in barcodes:
                x, y, w, h = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                barcode_data = barcode.data.decode('utf-8')
                selected_zona = random.choice(self.zonas)

                scan_result = self.process_scan(barcode_data, selected_zona)

                if scan_result:
                    print("Resultado del escaneo:")
                    print(f"Nombre: {scan_result['Nombre']}")
                    print(f"Zona: {selected_zona.nombre}")
                    print(f"Hora: {scan_result['Hora']}")
                    print(f"Tiene Permiso: {scan_result['Permiso']}")
                else:
                    print("Código de barras no reconocido.")

                self.last_detection_time = time.time()

                cv2.putText(frame, f'Barcode: {barcode_data}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f'Zona: {selected_zona.nombre}', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Barcode Scanner', frame)

    def run(self):
        while True:
            self.detect_barcodes()
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    database_main()
    scanner = BarcodeScanner(zonas)
    scanner.run()
