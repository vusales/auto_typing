import time
import keyboard
from docx import Document
import PyPDF2
import os

def read_docx(file_path):
    """Reads text from a .docx file."""
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def type_text(text):
    """Simulates typing Azerbaijani text using the keyboard library."""
    print("Typing will begin in 5 seconds. Place the cursor where you want the text.")
    time.sleep(5)  # Wait 5 seconds to allow the user to place the cursor
    for char in text:
        try:
            if char in AZERBAIJANI_MAP:
                keyboard.write(AZERBAIJANI_MAP[char])
            else:
                keyboard.write(char)
        except Exception as e:
            print(f"Error typing character '{char}': {e}")
        time.sleep(0.02)  # Add a slight delay between keystrokes

# Azerbaijani character mapping
AZERBAIJANI_MAP = {
    "ə": "ə",
    "ı": "ı",
    "ğ": "ğ",
    "ö": "ö",
    "ü": "ü",
    "ç": "ç",
    "ş": "ş",
    "Ə": "Ə",
    "İ": "İ",
    "Ğ": "Ğ",
    "Ö": "Ö",
    "Ü": "Ü",
    "Ç": "Ç",
    "Ş": "Ş",
}

# Define the file path
file_path = r"C:\Users\hp\Desktop\temp\word.docx"  # Adjust this to your actual path
file_format = "docx"  # Change to "pdf" for PDFs

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}")
else:
    print(f"File found: {file_path}")

# Read the text from the file
if file_format == "docx":
    text_to_type = read_docx(file_path)
elif file_format == "pdf":
    text_to_type = read_pdf(file_path)
else:
    raise ValueError("Unsupported file format!")

# Wait for Ctrl + T to start typing
print("Press Ctrl + T to start typing the text.")
keyboard.wait("ctrl+t")  # Wait until Ctrl + T is pressed
type_text(text_to_type)
