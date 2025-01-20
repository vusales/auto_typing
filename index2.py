import time
import pyautogui
from docx import Document
import PyPDF2
import os
import pygetwindow as gw  # For checking active windows

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])

def type_text(text):
    print("Typing will begin in 5 seconds. Ensure the text area is focused.")
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

# Function to check if the desired window is active
def wait_for_text_area_window():
    print("Waiting for the text area window to be active...")
    while True:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:  # Check if there is an active window
            print(f"Current active window: {active_window.title}")
            if "Notepad" in active_window.title or "Editor" in active_window.title:  # Replace with your text editor name
                print("Text area window detected!")
                break
        time.sleep(1)

# Wait until the text area window is active
wait_for_text_area_window()

# Simulate typing
type_text(text_to_type)
