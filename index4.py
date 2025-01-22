import time
import pyautogui
from docx import Document
import PyPDF2
import os
import keyboard  # Library for detecting key presses

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])

def type_text(text):
    print("Typing will begin in 5 seconds. Place the cursor where you want the text.")
    time.sleep(5)  # Wait 5 seconds to allow the user to place the cursor
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(0.02)  # Add a slight delay between keystrokes

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
