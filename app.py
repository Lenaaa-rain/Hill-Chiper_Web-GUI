from flask import Flask, render_template, request, jsonify
import numpy as np #pip install flask numpy

app = Flask(__name__)

# Fungsi untuk mengenkripsi teks menggunakan Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(key_matrix)
    
    # Membersihkan plaintext dari karakter non-alfabet
    plaintext = ''.join([char.upper() for char in plaintext if char.isalpha()])
    
    # Menambahkan padding jika panjang plaintext tidak habis dibagi n
    while len(plaintext) % n != 0:
        plaintext += 'X'
    
    # Konversi plaintext ke angka (A=0, B=1, ..., Z=25)
    numeric_text = [alphabet.index(char) for char in plaintext]
    
    # Membagi plaintext menjadi blok-blok berukuran n
    blocks = [numeric_text[i:i+n] for i in range(0, len(numeric_text), n)]
    
    # Enkripsi setiap blok
    ciphertext = ""
    for block in blocks:
        block_vector = np.array(block)
        encrypted_block = np.dot(key_matrix, block_vector) % 26
        for num in encrypted_block:
            ciphertext += alphabet[num]
    
    return ciphertext

# Fungsi untuk memeriksa apakah matrix invertible modulo 26
def is_invertible_mod(matrix):
    det = int(round(np.linalg.det(matrix))) % 26
    return det != 0 and all(det % i != 0 for i in [2, 13])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Mendapatkan data dari form
            plaintext = request.form.get("plaintext")
            matrix_size = int(request.form.get("matrix_size"))
            matrix_data = request.form.getlist("matrix[]")
            
            # Mengonversi matrix_data ke matriks numerik
            key_matrix = np.array([int(num) for num in matrix_data]).reshape(matrix_size, matrix_size)
            
            # Memeriksa apakah matriks valid
            if not is_invertible_mod(key_matrix):
                return jsonify({"error": "Matrix tidak valid! Determinan harus coprime dengan 26."})
            
            # Melakukan enkripsi
            ciphertext = hill_encrypt(plaintext, key_matrix)
            return jsonify({"ciphertext": ciphertext})
        
        except Exception as e:
            return jsonify({"error": f"Terjadi kesalahan: {str(e)}"})
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)