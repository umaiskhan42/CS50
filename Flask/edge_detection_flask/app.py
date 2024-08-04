from flask import Flask, render_template, request, redirect, url_for
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Apply edge detection
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            edges = cv2.Canny(image, 100, 200)
            edge_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'edges_' + filename)
            cv2.imwrite(edge_file_path, edges)
            
            return render_template('index.html', original_image=file_path, processed_image=edge_file_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
