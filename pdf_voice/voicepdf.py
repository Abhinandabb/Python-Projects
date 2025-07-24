
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar
from tkinter import ttk
import fitz  # PyMuPDF
import pyttsx3
from gtts import gTTS
from playsound import playsound
import re
import socket
import threading


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False


def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        content = page.get_text()
        if content.strip():
            text += content + "\n"
    return text.strip()


def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()


def txt_speech(text, rate=150, volume=1.0):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()


def txts(text, lang='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    playsound(filename)


def select_pdf():
    return filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])


def main():
    def convert_pdf():
        file_path = select_pdf()
        if not file_path:
            return
        status_var.set("Extracting text...")
        root.update()

        text = extract_text_from_pdf(file_path)
        if not text:
            messagebox.showinfo("Info", "No text found in the PDF.")
            return

        cleaned = clean_text(text)
        mode = mode_var.get()

        def run_tts():
            try:
                if mode == "Offline (pyttsx3)":
                    status_var.set("Speaking (offline)...")
                    txt_speech(cleaned)
                    status_var.set("Done.")
                else:
                    if not is_connected():
                        messagebox.showerror("Network Error", "No internet connection available.")
                        status_var.set("Idle")
                        return
                    status_var.set("Converting with gTTS...")
                    txts(cleaned)
                    status_var.set("Done. Audio saved as output.mp3")
                    messagebox.showinfo("Done", "Audio saved and played.")
            except Exception as e:
                status_var.set("Error")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=run_tts).start()

    root = tk.Tk()
    root.title("📖 PDF to Audiobook Converter")
    root.geometry("430x250")
    root.resizable(False, False)

    ttk.Style().configure("TButton", font=("Segoe UI", 11))
    ttk.Style().configure("TLabel", font=("Segoe UI", 11))

    tk.Label(root, text="Select TTS Mode:", font=("Segoe UI", 12)).pack(pady=10)

    mode_var = StringVar(value="Offline (pyttsx3)")
    ttk.OptionMenu(root, mode_var, "Offline (pyttsx3)", "Offline (pyttsx3)", "Online (gTTS)").pack(pady=5)

    ttk.Button(root, text="📂 Select PDF and Convert", command=convert_pdf).pack(pady=15)

    status_var = tk.StringVar(value="Voice PDF Converter is ready.")
    ttk.Label(root, textvariable=status_var, foreground="blue").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
