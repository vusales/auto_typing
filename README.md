# auto_typing
# Auto Typing Script
This script reads text from a .docx or .pdf file and types it into any text area on your screen after pressing Ctrl + T. Follow the instructions below to set it up.

### Prerequisites

1. Install Python:

Download Python from python.org.
During installation, check the box "Add Python to PATH".
Verify installation by running python --version in a terminal.
Install Required Libraries: Open a terminal or command prompt and run:


``` pip install pyautogui python-docx pypdf2 keyboard ```

2. Clone or Copy the Script:

Copy the script index.py provided below to the desired directory.
Save the text file you want to type (.docx or .pdf) in the same directory as the script.

Adjust the File Path:

Open the index.py script in a text editor.
Modify the file_path variable to point to your .docx or .pdf file:
python
Kopyala
Düzenle
file_path = r"C:\path\to\your\file.docx"

3. Usage
Run the Script:

Open a terminal in the script directory.
Run the script with:

``` python index.py ```

Start Typing:

Once the script starts, you will see the message:

"Press Ctrl + T to start typing the text."

Open the text editor or document where you want the text to appear.
Place the cursor in the desired text area.
Press Ctrl + T.

Observe Typing:

The script will simulate typing the content of your file in the active text area.
Troubleshooting

File Not Found Error:

Ensure the file_path in the script is correct.
Use raw string formatting (r"C:\path\to\file.docx") for the file path.

Library Not Found Error:

Ensure all required libraries are installed using:

``` pip install pyautogui python-docx pypdf2 keyboard ```

Script Doesn’t Type:

Ensure you’ve placed the cursor in a text-editable area.
Check for active antivirus or permissions blocking the script.# auto_typing
# auto_typing
# auto_typing
