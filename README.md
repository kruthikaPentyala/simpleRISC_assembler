# SimpleRISC Assembler Web Application

This project provides a web-based SimpleRISC assembler where users can upload an `.asm` file, process it, and download the output files in binary (`.bin`) and hexadecimal (`.hex`) formats.

## ✨ Features
- Web interface for uploading `.asm` files.
- Backend processes the file and generates:
  - **Binary output** (`.bin`)
  - **Hexadecimal output** (`.hex`)
- Python-based backend using Flask.
- Converts binary output to hexadecimal.

---

## 🛠 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/simpleRISC_assembler.git
cd simpleRISC_assembler

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install the required dependencies.

### 3️⃣ Run the Application
Start the Flask backend.
python app.py
Open your browser and go to http://127.0.0.1:5000/ to access the web app.

### 🚀 Usage Instructions
Open the web app.
Click the "Upload File" button to select a .asm (SimpleRISC assembly) file.
Click "Assemble" to process the file.
Download the generated .bin and .hex output files.

### 📄 Input File Format (SimpleRISC Assembly)
The assembler expects an input .asm file following these rules:

Comments must use //.
Labels must be placed on a separate line, without instructions on the same line.
### ✅ Example Input (example.asm):

      mov r1, 1       // fact = 1
      mov r2, r0      // the number is stored in input port register r0

loop: 
      mul r1, r1, r2  // fact = fact * i
      sub r2, r2, 1   // decrement i
      cmp r2, 1       // compare i > 1
      bgt loop        // if i > 1 then remain in loop
      mov r3, r1      // else the result is stored in output port register r3
      hlt            // stops program counter to be incremented

#### 🎯 Expected Output:
example.bin (Binary format)
example.hex (Hexadecimal format)

#### 📂 Project Structure
simpleRISC_assembler/
│── static/
│   ├── styles.css         # Frontend styling
│── templates/
│   ├── index.html         # Web interface (frontend)
│── uploads/               # Folder for storing uploaded files
│── outputs/               # Folder for storing generated output files
│── assembler.py           # Core assembler logic
│── convert_bin_to_hex.py  # Converts binary to hex
│── app.py                 # Flask backend to handle file uploads and processing
│── requirements.txt       # Dependencies
│── README.md              # Documentation

### 🏗 Code Overview
🔹 app.py
Flask-based backend.
Handles file uploads.
Runs assembler.py to generate a binary output file.
Runs convert_bin_to_hex.py to convert the binary output to hex.
Allows users to download the output files.
🔹 assembler.py
Reads SimpleRISC assembly instructions.
Converts them into binary machine code.
Ensures labels are on a separate line.
Saves the binary output to a .bin file.
🔹 convert_bin_to_hex.py
Reads the binary file.
Converts binary instructions to hexadecimal format.
Saves the output to a .hex file.
🔹 templates/index.html
Provides the user interface for uploading .asm files and downloading output files.
🔹 static/styles.css
Styles the web interface.

