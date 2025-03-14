from flask import Flask, render_template, request, send_file
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            binary_output_path = os.path.join(OUTPUT_FOLDER, "output.bin")
            hex_output_path = os.path.join(OUTPUT_FOLDER, "output.hex")

            file.save(input_path)

            # Run the assembler
            subprocess.run(["python", "assembler.py", input_path, binary_output_path])

            # Convert binary to hex
            subprocess.run(["python", "convert_bin_to_hex.py", binary_output_path, hex_output_path])

            return render_template("index.html", bin_file="output.bin", hex_file="output.hex")

    return render_template("index.html", bin_file=None, hex_file=None)

@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(OUTPUT_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
