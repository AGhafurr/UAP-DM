---
# 💧 **Classification Water for Healthy Life** 💦
---

## ✨ **Overview**

Klasifikasi kandungan air mineral merupakan pendekatan penting dalam industri air minum untuk memastikan kualitas, keamanan, dan kecocokan air bagi konsumsi manusia. Proses ini melibatkan analisis terhadap berbagai komponen kimia dan fisik yang ada dalam air mineral, yang meliputi mineral terlarut, serta keberadaan zat-zat lain yang dapat mempengaruhi rasa, aroma, dan keseluruhan kualitas air.

Dengan mengetahui kandungan air mineral, kita dapat mengkategorikan air berdasarkan manfaat kesehatannya, rasa, dan bahkan kecocokan bagi kondisi kesehatan tertentu. Pendekatan ini juga sangat relevan dalam memenuhi standar kualitas air yang ditetapkan oleh badan pengawas dan mengurangi risiko pencemaran atau kontaminasi.

---

## 📊 **Dataset**

- **Sumber**: [Water Quality Dataset on Kaggle](https://www.kaggle.com/datasets/mssmartypants/water-quality)
- **Deskripsi**: Dataset ini mencakup informasi tentang kualitas air dengan total 20 fitur, termasuk kandungan alumunium, dan berbagai mineral terlarut, serta 1 target untuk klasifikasi kualitas air. Dataset ini memberikan gambaran yang luas tentang karakteristik fisik dan kimia air di berbagai lokasi.

---

##  🔍**Instalasi**

1. **Clone Repositori:**
   Buka terminal Anda dan clone repositorinya menggunakan git:
   ```bash
   git clone https://github.com/AGhafurr/UAP-ML.git
   cd UAP-ML
   ```

2. **Siapkan Lingkungan Virtual (Opsional tapi Disarankan):**
   Sangat dianjurkan untuk membuat lingkungan virtual untuk mengelola ketergantungan. Anda bisa menggunakan `venv` atau `conda`.

   Menggunakan `venv`:
   ```bash
   python -m venv venv
   source venv\Scripts\activate 
   ```

   Menggunakan `conda`:
   ```bash
   conda create -n uap-ml python=3.8  # atau versi yang Anda inginkan
   conda activate uap-ml
   ```

3. **Instal Ketergantungan:**
   Jika terdapat file `requirements.txt` di repositori, Anda bisa menginstal ketergantungan yang diperlukan menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Proyek:**
   Tergantung pada struktur proyek, Anda mungkin perlu menjalankan skrip atau perintah tertentu untuk mengeksekusi fungsionalitas. Periksa dokumentasi untuk instruksi tentang cara menjalankan program utama atau pengujian.
---

## 🛠️ **Feedforward Neural Network (FNN)**

Model **Feedforward Neural Network (FNN)** digunakan untuk menganalisis data kualitas air secara komprehensif dan menyajikan wawasan yang relevan. FNN, yang terdiri dari beberapa lapisan tersembunyi, dilatih untuk mempelajari pola kompleks antara fitur input dan kategori output kualitas air.

Terima kasih atas klarifikasinya! Berikut adalah pembaruan langkah-langkah pengembangan model dengan penekanan pada **augmentasi menggunakan SMOTE** dan **standarisasi menggunakan StandardScaler**:

---

## **Langkah-langkah Pengembangan Model (Data Tabular)**:

### 1. **Data Preprocessing**

Pada tahap ini, dilakukan beberapa teknik untuk mempersiapkan data tabular sebelum dimasukkan ke dalam model **Feedforward Neural Network (FNN)**:

- **Pengecekan Missing Value**:

  - Mengecek apakah ada nilai yang hilang dalam dataset dan menanganinya dengan cara imputasi atau menghapus baris dengan missing value.

- **Augmentasi Data dengan SMOTE (Synthetic Minority Over-sampling Technique)**:
  - SMOTE digunakan untuk menangani masalah **ketidakseimbangan kelas** dalam dataset, yaitu ketika jumlah sampel dari satu kelas jauh lebih sedikit dibandingkan kelas lainnya.
  - SMOTE bekerja dengan cara menciptakan sampel baru yang sintetik dari kelas minoritas berdasarkan kedekatannya dengan data yang sudah ada. Teknik ini menghasilkan data buatan yang "mirip" dengan data asli dan memperbaiki distribusi kelas sehingga model tidak condong ke kelas mayoritas.
- **Standarisasi dengan StandardScaler**:
  - Setelah menangani missing value dan augmentasi, **StandardScaler** digunakan untuk menstandarisasi fitur numerik dalam dataset.
  - Standarisasi dilakukan dengan mengubah data agar memiliki **mean (rata-rata) = 0** dan **deviasi standar (standard deviation) = 1**. Proses ini penting agar fitur yang memiliki skala yang sangat berbeda (misalnya, pH 7 vs TDS 3000) tidak mendominasi pelatihan model.

### 2. **Model Training**

Setelah data diproses, langkah selanjutnya adalah pelatihan model **Feedforward Neural Network (FNN)**:

- **Pembagian Dataset**: Dataset dibagi menjadi dua bagian utama, yaitu **data pelatihan** (training set) dan **data pengujian** (test set). Misalnya, pembagian 70% untuk pelatihan dan 30% untuk pengujian.
- **Arsitektur Model**: Model FNN terdiri dari beberapa lapisan input, satu atau lebih lapisan tersembunyi, dan lapisan output. Setiap lapisan tersembunyi menggunakan fungsi aktivasi **ReLU (Rectified Linear Unit)**, sedangkan lapisan output menggunakan **Sigmoid** untuk target kelas merupakan biner.
- **Algoritma Optimisasi**: Pelatihan dilakukan menggunakan algoritma optimisasi **Stochastic Gradient Descent (SGD)** untuk memperbarui bobot dan bias jaringan. seperti pada gambar dibawah:
  ![image](https://github.com/user-attachments/assets/e95fe282-a2d2-4bef-a13a-ca8a741c11a7)

### 3. **Evaluasi Model**

Setelah model dilatih, evaluasi dilakukan dengan menggunakan data uji yang belum pernah dilihat oleh model sebelumnya:
Hasil Fitting Pelatihan mode FNN:

![image](https://github.com/user-attachments/assets/fa3d9210-88a4-4bf3-8785-1588109698be)

Grafik menunjukkan peningkatan akurasi pada data train dan validasi selama 100 epoch, dengan akurasi validasi yang stabil dan lebih tinggi dibandingkan train, menandakan model generalisasi dengan baik.

![image](https://github.com/user-attachments/assets/9bda3b9d-704c-4645-901b-957e05a2e43c)

Grafik diatas menunjukkan penurunan loss pada data train dan validasi selama 100 epoch, mengindikasikan model mengalami proses training yang baik dengan validasi yang stabil.

![image](https://github.com/user-attachments/assets/d2690f2c-8957-48f9-bc41-7cbeb802dd28)

Berdasarkan laporan klasifikasi, model memiliki performa yang sangat baik dalam mendeteksi kelas "Not Safe" (0) dengan F1-score 0.97, tetapi performa dalam mendeteksi kelas "Safe" (1) lebih rendah dengan F1-score 0.75. Hal ini menunjukkan bahwa model lebih efektif dalam mendeteksi situasi "Not Safe," namun perlu perbaikan dalam mengenali situasi "Safe" untuk menghindari under-representation.

### 4. **Implementasi**

Setelah evaluasi model, langkah selanjutnya adalah implementasi model ke dalam aplikasi nyata:

- **Prediksi dengan Data Baru**: Model dapat digunakan untuk memprediksi kualitas air pada data yang baru, seperti data yang dikumpulkan dari sensor atau sampel baru.
- **Integrasi ke Aplikasi**: Model dapat diintegrasikan ke dalam aplikasi web atau mobile, memungkinkan pengguna untuk memeriksa kualitas air secara real-time berdasarkan input data yang dimasukkan.
- **Pemeliharaan dan Pembaruan Model**: Secara berkala, model dapat diperbarui dengan data baru untuk memastikan kinerja tetap optimal.

---

## 📝 **Overview Live Demo**

### **Main Page**

Halaman utama ini dirancang untuk memberikan edukasi kepada pengguna tentang pentingnya air bagi kehidupan manusia serta memberikan gambaran mengenai karakteristik air yang sehat.

#### **Fitur Utama**

1. **Informasi Edukatif**

   - Pada halaman utama, pengguna dapat menemukan informasi mengenai pentingnya konsumsi air sehat untuk mendukung kesehatan manusia.
   - Selain itu, ditampilkan juga contoh air yang memenuhi standar kesehatan, memberikan pemahaman visual kepada pengguna.

   ![image](https://github.com/user-attachments/assets/f54063b4-9836-4f41-8148-45e8de73f72e)

2. **Navigasi ke Halaman Lain**

   - Di bagian bawah halaman utama, terdapat dua tombol navigasi:
     - **Tombol Pertama:** Mengarahkan pengguna ke halaman klasifikasi, di mana pengguna dapat memulai proses pengklasifikasian air untuk mengecek tingkat keamanannya.
     - **Tombol Kedua:** (Jika ada fungsi tambahan) Dapat diarahkan untuk fitur atau informasi lain terkait.

   ![image](https://github.com/user-attachments/assets/129c0310-0982-4a72-ba5c-022d2d3e7de5)

---

### **Classification Page**

Pada halaman ini, pengguna dapat mengecek apakah air mineral dengan berbagai kandungan di dalamnya memenuhi syarat untuk dikonsumsi atau tidak. Halaman ini dirancang untuk memberikan kemudahan dalam mengklasifikasikan tingkat keamanan air berdasarkan parameter tertentu.

#### **Fitur Utama**

1. **Tampilan Awal**

   - Halaman awal menunjukkan antarmuka untuk memasukkan data kandungan air yang akan diuji.
   - Pengguna dapat melihat informasi dan petunjuk terkait parameter kualitas air yang perlu diperhatikan.

   ![image](https://github.com/user-attachments/assets/bf9ac593-3c6e-4c3b-a559-b34a663bf897)

2. **Tombol Mulai Pengklasifikasian**

   - Terdapat tombol untuk memulai proses pengklasifikasian.
   - Tombol ini memungkinkan sistem untuk menganalisis data yang dimasukkan dan memberikan hasil secara instan.

   ![image](https://github.com/user-attachments/assets/dd9c76f5-3845-4c03-826e-1c11a4cd0f4b)

3. **Hasil Klasifikasi**

   - **Air Aman Dikonsumsi:** Jika hasil analisis menunjukkan bahwa air mineral aman untuk dikonsumsi, halaman akan menampilkan notifikasi yang menyatakan bahwa air tersebut layak diminum.

     ![image](https://github.com/user-attachments/assets/6b30cedc-3cca-4e8a-a941-72cc20f4218b)

   - **Air Tidak Aman Dikonsumsi:** Jika air dinyatakan tidak aman untuk dikonsumsi, sistem akan memberikan pemberitahuan yang menjelaskan parameter yang melebihi batas aman. Selain itu, ditampilkan juga informasi tentang bahaya potensial jika air tersebut dikonsumsi melebihi ambang batas.

     ![image](https://github.com/user-attachments/assets/99318e44-8fab-4e90-902d-52be037eca18)

---

## 🌟 **Manfaat**

Penerapan klasifikasi kualitas air ini memiliki banyak manfaat, baik di industri pengolahan air, penelitian kesehatan, maupun bagi konsumen yang ingin memastikan kualitas air yang mereka konsumsi. Beberapa manfaat utamanya adalah:

- **Keamanan Konsumsi**: Memastikan air yang dikonsumsi aman dan bebas dari kontaminan berbahaya seperti logam berat, mikroorganisme patogen, atau bahan kimia beracun.
- **Kesehatan yang Lebih Baik**: Mengidentifikasi kandungan mineral yang mendukung kesehatan tubuh, seperti kalsium, magnesium, dan elektrolit lainnya, yang penting untuk fungsi tubuh optimal.
- **Efisiensi Pengolahan Air**: Membantu produsen air dan industri pengolahan air minum untuk mengelola sumber daya air dengan lebih efisien, mengurangi limbah, dan memastikan proses produksi sesuai dengan standar kualitas.
- **Mendukung Industri Air Mineral**: Membantu produsen air mineral dalam:
  - Mengembangkan produk dengan kandungan mineral yang ideal untuk berbagai kebutuhan konsumen, seperti air mineral untuk hidrasi sehari-hari atau air dengan kandungan khusus untuk olahraga.
  - Memastikan produk memenuhi standar kesehatan dan peraturan yang berlaku, sehingga meningkatkan kepercayaan konsumen terhadap merek mereka.
- **Meningkatkan Standar Hidup**: Memberikan informasi kepada masyarakat umum untuk memilih air yang sesuai dengan kebutuhan kesehatan mereka, sehingga secara langsung meningkatkan kualitas hidup dan kesejahteraan.
- **Pengembangan Teknologi dan Penelitian**: Mendukung penelitian lebih lanjut dalam pengembangan alat dan teknologi pengolahan air, serta membantu ilmuwan untuk memahami lebih dalam hubungan antara kualitas air dan kesehatan.
- **Peningkatan Reputasi Industri**: Dengan mengadopsi klasifikasi kualitas air, perusahaan dapat meningkatkan kepercayaan publik dan membangun reputasi sebagai produsen yang peduli terhadap kesehatan dan lingkungan.

---

## 📬 **Developed By**

## [Abdul Ghafur](https://github.com/AGhafurr) - 202110370311109
