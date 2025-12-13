# gui_app.py
import tkinter as tk
from tkinter import filedialog, messagebox

from src.caeser_cipher import CaesarCipher
from src.symmetric import SymmetricCipher
from src.asymmetric import AsymmetricCipher
from src.file_cipher import FileCipher


class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Encrypted_Decrypted-app GUI")
        master.geometry("650x550")

        # =========================
        # Encryption type selection
        # =========================
        tk.Label(master, text="Choose encryption type:", font=("Arial", 11, "bold")).pack(pady=5)

        self.encryption_var = tk.StringVar(value="Caesar")
        options = ["Caesar", "Symmetric", "Asymmetric", "File"]
        tk.OptionMenu(master, self.encryption_var, *options).pack()

        self.encryption_var.trace("w", self.update_fields)

        # =========================
        # Message input
        # =========================
        self.label_message = tk.Label(master, text="Message:")
        self.message_text = tk.Text(master, height=5, width=60)

        # =========================
        # Key / Shift input
        # =========================
        self.label_key = tk.Label(master, text="Key / Shift:")
        self.key_entry = tk.Entry(master, width=60)

        # =========================
        # Buttons
        # =========================
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)

        # RSA generate keys button (NEW)
        self.generate_keys_button = tk.Button(
            master,
            text="Generate RSA Keys",
            command=self.generate_rsa_keys
        )

        self.file_button = tk.Button(master, text="Select File", command=self.select_file)

        # =========================
        # Result
        # =========================
        tk.Label(master, text="Result:", font=("Arial", 11, "bold")).pack(pady=5)
        self.result_text = tk.Text(master, height=10, width=60)
        self.result_text.pack()

        self.selected_file = None

        # Initial UI
        self.update_fields()

    # =========================
    # UI helpers
    # =========================
    def hide_all_fields(self):
        self.label_message.pack_forget()
        self.message_text.pack_forget()
        self.label_key.pack_forget()
        self.key_entry.pack_forget()
        self.encrypt_button.pack_forget()
        self.decrypt_button.pack_forget()
        self.file_button.pack_forget()
        self.generate_keys_button.pack_forget()

    def update_fields(self, *args):
        self.hide_all_fields()
        enc_type = self.encryption_var.get()

        # Caesar
        if enc_type == "Caesar":
            self.label_message.config(text="Enter message:")
            self.label_key.config(text="Enter shift value:")
            self.label_message.pack()
            self.message_text.pack()
            self.label_key.pack()
            self.key_entry.pack()
            self.encrypt_button.pack(pady=5)
            self.decrypt_button.pack(pady=5)

        # Symmetric
        elif enc_type == "Symmetric":
            self.label_message.config(text="Enter message / encrypted text:")
            self.label_key.config(text="Enter key (required for decryption):")
            self.label_message.pack()
            self.message_text.pack()
            self.label_key.pack()
            self.key_entry.pack()
            self.encrypt_button.pack(pady=5)
            self.decrypt_button.pack(pady=5)

        # Asymmetric
        elif enc_type == "Asymmetric":
            self.label_message.config(text="Enter message / encrypted text:")
            self.label_key.config(text="Paste public key (encrypt) or private key (decrypt):")
            self.label_message.pack()
            self.message_text.pack()
            self.label_key.pack()
            self.key_entry.pack()
            self.generate_keys_button.pack(pady=5)   # 👈 هنا الزر
            self.encrypt_button.pack(pady=5)
            self.decrypt_button.pack(pady=5)

        # File
        elif enc_type == "File":
            self.file_button.pack(pady=5)
            self.label_key.config(text="Enter key (required for decryption):")
            self.label_key.pack()
            self.key_entry.pack()
            self.encrypt_button.pack(pady=5)
            self.decrypt_button.pack(pady=5)

    # =========================
    # File selection
    # =========================
    def select_file(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file:
            messagebox.showinfo("File Selected", self.selected_file)

    # =========================
    # RSA Key Generation
    # =========================
    def generate_rsa_keys(self):
        try:
            cipher = AsymmetricCipher()
            private_key, public_key = cipher.generate_keys()

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(
                tk.END,
                f"Private Key:\n{private_key.decode()}\n\nPublic Key:\n{public_key.decode()}"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # =========================
    # Encrypt
    # =========================
    def encrypt(self):
        enc_type = self.encryption_var.get()
        msg = self.message_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        try:
            if enc_type == "Caesar":
                shift = int(key) if key else 3
                cipher = CaesarCipher()
                result = cipher.encrypt_caesar_cipher(msg, shift)

            elif enc_type == "Symmetric":
                cipher = SymmetricCipher()
                encrypted = cipher.encrypt(msg)
                result = f"{encrypted.decode()}\n\nKey:\n{cipher.get_key().decode()}"

            elif enc_type == "Asymmetric":
                if not key:
                    raise ValueError("Public key is required for encryption.")
                cipher = AsymmetricCipher()
                encrypted = cipher.encrypt(msg, key.encode())
                result = encrypted

            elif enc_type == "File":
                if not self.selected_file:
                    raise ValueError("Please select a file first.")
                file_cipher = FileCipher()
                key = file_cipher.encrypt_file(self.selected_file)
                result = f"File encrypted successfully.\n\nKey:\n{key}"

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # =========================
    # Decrypt
    # =========================
    def decrypt(self):
        enc_type = self.encryption_var.get()
        msg = self.message_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        try:
            if enc_type == "Caesar":
                shift = int(key) if key else 3
                cipher = CaesarCipher()
                result = cipher.decrypt_caesar_cipher(msg, shift)

            elif enc_type == "Symmetric":
                if not key:
                    raise ValueError("Key is required for decryption.")
                cipher = SymmetricCipher(key.encode())
                result = cipher.decrypt(msg.encode())

            elif enc_type == "Asymmetric":
                if not key:
                    raise ValueError("Private key is required.")
                cipher = AsymmetricCipher()
                result = cipher.decrypt(msg, key.encode())

            elif enc_type == "File":
                if not self.selected_file or not key:
                    raise ValueError("File and key are required.")
                file_cipher = FileCipher()
                file_cipher.decrypt_file(self.selected_file, key.encode())
                result = "File decrypted successfully."

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
