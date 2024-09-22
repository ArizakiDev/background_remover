from flask import Flask, request, render_template, send_file
import os
from rembg import remove
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Aucun fichier téléchargé."
    
    file = request.files['file']
    if file.filename == '':
        return "Nom de fichier vide."
    
    # Enregistrer l'image téléchargée
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)
    
    # Supprimer le fond
    with open(input_path, "rb") as i:
        input_data = i.read()
    output_data = remove(input_data)

    output_path = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(file.filename)[0]}_no_bg.png")
    with open(output_path, "wb") as o:
        o.write(output_data)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
