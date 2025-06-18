import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_create_matrix.clicked.connect(self.create_matrix)
        
    def create_matrix(self):
        key = self.ui.txt_matrix_key.text().strip()
        if not key:
            QMessageBox.warning(self, "Warning", "Please enter a key for matrix creation")
            return
            
        try:
            # Create matrix using the same logic as in cipher implementation
            key = key.replace("J", "I").upper()
            key_set = set(key)
            alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            remaining_letters = [letter for letter in alphabet if letter not in key_set]
            
            matrix = list(key)
            for letter in remaining_letters:
                if letter not in matrix:
                    matrix.append(letter)
                if len(matrix) == 25:
                    break
                    
            # Format matrix as 5x5 grid
            playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
            
            # Display matrix in text area
            matrix_text = ""
            for row in playfair_matrix:
                matrix_text += " ".join(row) + "\n"
                
            self.ui.txt_matrix_display.setPlainText(matrix_text)
            QMessageBox.information(self, "Success", "Matrix created successfully")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error creating matrix: {str(e)}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_text"])
                QMessageBox.information(self, "Success", "Encrypted successfully")
            else:
                print("Error while calling api")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted successfully")
            else:
                print("Error while calling api")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
