from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Fungsi Hill Cipher
def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv

def text_to_matrix(text, n):
    text = text.upper().replace(" ", "")
    while len(text) % n != 0:
        text += "X"
    matrix = [ord(c) - ord("A") for c in text]
    return np.reshape(matrix, (-1, n)).T

def matrix_to_text(matrix, n):
    text = ""
    for col in matrix.T:
        for num in col:
            text += chr((num % 26) + ord("A"))
    return text

def encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    plain_matrix = text_to_matrix(plain_text, n)
    cipher_matrix = np.dot(key_matrix, plain_matrix) % 26
    return matrix_to_text(cipher_matrix, n)

def decrypt(cipher_text, key_matrix):
    n = key_matrix.shape[0]
    cipher_matrix = text_to_matrix(cipher_text, n)
    key_inv = mod_inverse(key_matrix, 26)
    plain_matrix = np.dot(key_inv, cipher_matrix) % 26
    return matrix_to_text(plain_matrix, n)

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted_text = ""
    decrypted_text = ""

    if request.method == "POST":
        if "encrypt" in request.form:
            plaintext = request.form["plaintext"]
            keytext = request.form["key"]
            try:
                key = np.array([int(x) for x in keytext.split()]).reshape(2, 2)
                encrypted_text = encrypt(plaintext, key)
            except:
                encrypted_text = "Key tidak valid atau panjang teks tidak sesuai."

        elif "decrypt" in request.form:
            ciphertext = request.form["ciphertext"]
            keytext = request.form["key"]
            try:
                key = np.array([int(x) for x in keytext.split()]).reshape(2, 2)
                decrypted_text = decrypt(ciphertext, key)
            except:
                decrypted_text = "Key tidak valid atau panjang teks tidak sesuai."

    return render_template(
        "index.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text
    )

if __name__ == "__main__":
    app.run(debug=True)