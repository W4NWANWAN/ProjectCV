# app.py
from flask import Flask, render_template, Response
import cv2
import time
from ultralytics import YOLO

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model YOLOv8 yang sudah Anda latih
# Pastikan file 'best.pt' berada di folder yang sama dengan app.py
# atau berikan path lengkapnya.
try:
    model = YOLO('best.pt')
    print("Model YOLOv8 berhasil dimuat.")
except Exception as e:
    print(f"Error memuat model: {e}")
    model = None

def generate_frames():
    """
    Generator function untuk membaca frame dari kamera, melakukan deteksi objek,
    dan mengirimkannya sebagai stream.
    """
    camera = None
    while camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Gagal membuka kamera. Mencoba lagi dalam 2 detik...")
            time.sleep(2)
    
    print("Kamera berhasil diakses.")

    while True:
        # Baca frame dari kamera
        success, frame = camera.read()
        if not success:
            print("Gagal membaca frame dari kamera.")
            break
        
        if model:
            # Lakukan deteksi objek pada frame menggunakan YOLOv8
            results = model(frame, stream=True)

            # Loop melalui hasil deteksi
            for r in results:
                # Dapatkan kotak pembatas dan nama kelas
                boxes = r.boxes
                for box in boxes:
                    # Koordinat kotak
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Gambar kotak pada frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # Dapatkan kepercayaan (confidence) dan nama kelas
                    confidence = round(float(box.conf[0]), 2)
                    cls = int(box.cls[0])
                    class_name = model.names[cls]

                    # Tulis label kelas dan confidence
                    label = f'{class_name} {confidence}'
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        
        # Encode frame yang sudah dimodifikasi ke format JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Gagal melakukan encode frame.")
            continue

        # Ubah frame menjadi bytes
        frame_bytes = buffer.tobytes()

        # Kirim frame sebagai bagian dari response multipart
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    # Lepaskan kamera saat loop berakhir
    print("Melepaskan kamera.")
    camera.release()


@app.route('/')
def index():
    """
    Route untuk halaman utama. Akan me-render file index.html.
    """
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """
    Route untuk video stream.
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Jalankan aplikasi Flask
    app.run(host='0.0.0.0', port=5000, debug=False)
