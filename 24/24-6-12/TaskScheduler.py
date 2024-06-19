from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
from docx import Document
from docx.oxml.ns import qn

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['IMAGE_FOLDER'] = 'images'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Ensure the images folder exists inside the upload folder
image_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], app.config['IMAGE_FOLDER'])
if not os.path.exists(image_folder_path):
    os.makedirs(image_folder_path)

def get_font_size(run):
    if run.font.size:
        return run.font.size.pt
    return None

def get_font_name(run):
    if run.font.name:
        return run.font.name
    return None

def get_run_formatting(run):
    return {
        "text": run.text,
        "bold": run.bold,
        "italic": run.italic,
        "underline": run.underline,
        "font_size": get_font_size(run),
        "font_name": get_font_name(run),
        "font_color": run.font.color.rgb if run.font.color.rgb else None
    }

def is_list_item(para):
    p = para._p  # Access the internal XML representation of the paragraph
    numPr = p.find(qn('w:numPr'))
    return numPr is not None

def extract_images(doc, blog_name_folder):
    images = []
    rels = doc.part.rels
    for rel in rels:
        if "image" in rels[rel].target_ref:
            img = rels[rel].target_part
            img_data = img.blob
            img_filename = os.path.basename(rels[rel].target_ref)
            img_path = os.path.join(blog_name_folder, img_filename)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
            images.append({
                "filename": img_filename,
                "path": img_path
            })
    return images

def extract_text_with_formatting(file_path):
    doc = Document(file_path)
    content = []
    current_list = None

    for para in doc.paragraphs:
        style = para.style.name
        runs = [get_run_formatting(run) for run in para.runs]
        is_list = is_list_item(para)

        if is_list:
            if current_list is None:
                current_list = {
                    "style": "List",
                    "items": []
                }
            current_list["items"].append({"runs": runs})
        else:
            if current_list is not None:
                content.append(current_list)
                current_list = None
            element = {
                "style": style,
                "runs": runs
            }
            content.append(element)
    
    # If the document ends with a list, make sure to add it to the content
    if current_list is not None:
        content.append(current_list)

    # Extract images
    blog_name = os.path.splitext(os.path.basename(file_path))[0]
    blog_name_folder = os.path.join(app.config['UPLOAD_FOLDER'], app.config['IMAGE_FOLDER'], blog_name)
    if not os.path.exists(blog_name_folder):
        os.makedirs(blog_name_folder)
    images = extract_images(doc, blog_name_folder)

    return content, images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.docx'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text with formatting and save to JSON
        content, images = extract_text_with_formatting(file_path)
        json_data = {
            "content": content,
            "images": images
        }
        json_file_path = os.path.splitext(file_path)[0] + '.json'
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        
        return jsonify({"message": "File uploaded and processed successfully", "json_file": json_file_path}), 200
    else:
        return jsonify({"error": "Invalid file type, only .docx is allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)

import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        dic={}
        for i in tasks:
            if i not in dic:
                dic[i]=-1
            else:
                dic[i]-=1
        val=[]
        for i in dic:
            val.append(dic[i])
        heapq.heapify(val)
        c=0
        q=deque()
        while len(val)!=0 or len(q)!=0:
            if len(val)!=0:
                v=heapq.heappop(val)
                if v+1!=0:
                    q.append([v+1,c+n])
            while len(q)!=0:
                va,co=q[0]
                if co>c:
                    break
                else:
                    q.popleft()
                    heapq.heappush(val , va)
            c+=1
            
                    
        return c