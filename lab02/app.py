from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailfenceCipher


app = Flask(__name__)

#caesar
@app.route("/")
def homt():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text} <br/> key: {key} <br/> encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text} </br> key: {key}  decrypted text: {decrypted_text}"


#vigenere
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return f"text: {text} <br/> key: {key} <br/> encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return f"text: {text} <br/> key: {key} <br/> decrypted text: {decrypted_text}"

#playfair
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")
@app.route("/playfair/matrix", methods=["POST"])
def playfair_matrix():
    key = request.form["matrixKey"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    matrix_html = "<br/>".join([" ".join(row) for row in matrix])
    return f"Key: {key} <br/> Matrix:<br/>{matrix_html}"
@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return f"text: {text} <br/> key: {key} <br/> encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return f"text: {text} <br/> key: {key} <br/> decrypted text: {decrypted_text}"

#railfence
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    rails = int(request.form["inputRailsPlain"])
    cipher = RailfenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, rails)
    return f"text: {text} <br/> rails: {rails} <br/> encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    rails = int(request.form["inputRailsCipher"])
    cipher = RailfenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, rails)
    return f"text: {text} <br/> rails: {rails} <br/> decrypted text: {decrypted_text}"

#main function
if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5050, debug=True)