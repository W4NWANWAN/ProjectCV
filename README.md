# Sistem Deteksi Objek Real-time

Sebuah aplikasi web Flask yang menggunakan model YOLOv8 untuk mendeteksi objek dari feed webcam secara real-time.

## Deskripsi

Proyek ini adalah aplikasi web yang dibangun menggunakan Flask (framework Python) yang mampu melakukan deteksi objek secara real-time melalui feed webcam pengguna. Aplikasi ini memanfaatkan kekuatan model YOLOv8 dari Ultralytics untuk mengidentifikasi dan melokalisasi berbagai objek dalam frame video. Hasil deteksi ditampilkan langsung di antarmuka web, memberikan pengalaman interaktif kepada pengguna.

## Fitur Utama

*   **Deteksi Objek Real-time:** Mampu mendeteksi objek dari feed webcam secara langsung.
*   **Model YOLOv8:** Menggunakan model deteksi objek state-of-the-art YOLOv8 untuk akurasi dan kecepatan tinggi.
*   **Antarmuka Web Interaktif:** Dibangun dengan Flask dan HTML/CSS sederhana untuk menampilkan feed video dan hasil deteksi.
*   **Mudah Digunakan:** Proses instalasi dan penggunaan yang relatif sederhana.

## Teknologi yang Digunakan

*   **Python:** Bahasa pemrograman utama yang digunakan.
*   **Flask:** Framework web micro untuk membangun aplikasi.
*   **OpenCV (cv2):** Library untuk pemrosesan gambar dan video, termasuk pengambilan feed webcam.
*   **Ultralytics YOLOv8:** Library untuk implementasi model YOLOv8.
*   **HTML/CSS:** Untuk membangun antarmuka pengguna di sisi klien.

## Instalasi

1.  **Clone Repositori:**
    ```bash
    git clone https://github.com/USERNAME/NAMA-REPOSITORI.git
    cd NAMA-REPOSITORI
    ```

2.  **Buat dan Aktifkan Virtual Environment (Direkomendasikan):**
    ```bash
    python -m venv venv
    # Untuk Windows
    venv\Scripts\activate
    # Untuk macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Catatan: Pastikan file `requirements.txt` berisi semua paket yang dibutuhkan seperti `flask`, `opencv-python`, `ultralytics`)*

## Cara Penggunaan

1.  **Jalankan Aplikasi Flask:**
    ```bash
    python app.py
    ```
    *(Catatan: Nama file utama mungkin berbeda, sesuaikan jika perlu)*

2.  **Buka Browser:**
    Buka browser web Anda dan akses alamat `http://127.0.0.1:5000/` (atau alamat lain yang ditampilkan di terminal).

3.  **Izinkan Akses Webcam:**
    Browser akan meminta izin untuk mengakses webcam Anda. Izinkan akses tersebut.

4.  **Lihat Deteksi:**
    Feed webcam Anda akan ditampilkan di halaman web, dan objek yang terdeteksi akan ditandai dengan bounding box beserta label kelasnya.

## Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi, silakan fork repositori ini dan buat pull request. Anda juga dapat membuka issue jika menemukan bug atau memiliki saran fitur.

## Lisensi

Proyek ini dilisensikan di bawah [NAMA LISENSI, cth: MIT License]. Lihat file `LICENSE` untuk detail lebih lanjut.
---

**Catatan Tambahan:**

*   Pastikan Anda memiliki webcam yang terhubung dan berfungsi dengan baik.
*   Kinerja deteksi dapat bervariasi tergantung pada spesifikasi perangkat keras komputer Anda.
*   Anda mungkin perlu menginstal driver tambahan untuk webcam Anda tergantung pada sistem operasi yang digunakan.
*   File `requirements.txt` harus dibuat dan berisi daftar semua dependensi Python yang diperlukan. Contoh isi `requirements.txt`:
    ```
    Flask
    opencv-python
    ultralytics
    # Tambahkan library lain jika ada
    ```
