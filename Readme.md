
# Hill Chiper with Web GUI

### 🛡️ Hill Cipher Implementation

Implementasi algoritma Hill Cipher untuk enkripsi dan dekripsi teks menggunakan metode kriptografi berbasis matriks.

### 🔍 Apa Itu Hill Cipher?

**Hill Cipher** adalah algoritma kriptografi klasik yang menggunakan operasi matriks (perkalian matriks dan invers matriks) untuk mengenkripsi dan mendekripsi pesan. Metode ini dikembangkan oleh Lester S. Hill pada tahun 1929.

Karakteristik:  
- Termasuk ke dalam polyalphabetic cipher  
- Menggunakan matriks kunci persegi (n x n) untuk transformasi  
- Cocok untuk blok teks dengan panjang tertentu sesuai ukuran matriks

### 🧠 Cara Kerja Singkat
Enkripsi:  
- Teks dipotong menjadi blok-blok sesuai ukuran matriks.  
- Setiap karakter diubah menjadi angka (A=0, B=1, ..., Z=25).  
- Dikalikan dengan matriks kunci modulo 26.  
- Hasilnya dikonversi kembali ke huruf.

Dekripsi:    
- Matriks kunci harus memiliki invers dalam modulo 26.  
- Cari invers dari matriks kunci.  
- Kalikan ciphertext dengan invers matriks kunci.  
- Hasilnya dikonversi kembali ke plaintext.

### 🛠️ Teknologi / Tools
- Python 3.x  
- numpy  
- flask

## Deployment

▶️ Cara Menjalankan Program

1. Install Depedencies
```bash
  pip install -r requirements.txt
```
2. Jalankan Program
```bash
  python app.py
```

## Screenshots

![App Screenshot](/images/SS1.png)  
![App Screenshot](/images/SS2.png)
![App Screenshot](/images/SS3.png)
![App Screenshot](/images/SS4.png)
![App Screenshot](/images/SS5.png)
![App Screenshot](/images/SS6.png)